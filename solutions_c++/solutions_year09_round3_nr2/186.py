#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <iomanip>
#include <cmath>

using namespace std;
typedef long long int64;

int main (int argc, char * const argv[]) {
	
	fstream INP("input.txt",fstream::in);
	fstream OUT("output.txt",fstream::out);
		
	int T;
	INP>>T;
	
	for(int c=0;c<T;c++)
		{
		
		int N;
		INP>>N;
		
		vector<double> Xs(N,0);
		vector<double> Ys(N,0);
		vector<double> Zs(N,0);
		vector<double> VXs(N,0);
		vector<double> VYs(N,0);
		vector<double> VZs(N,0);
		
		for(int i=0;i<N;i++)
			INP>>Xs[i]>>Ys[i]>>Zs[i]>>VXs[i]>>VYs[i]>>VZs[i];
		
		vector<double> CDM_S(3,0);
		vector<double> CDM_V(3,0);
		
		for(int i=0;i<N;i++)
			{
			CDM_S[0]+=Xs[i];
			}
		for(int i=0;i<N;i++)
			{
			CDM_S[1]+=Ys[i];
			}
		for(int i=0;i<N;i++)
			{
			CDM_S[2]+=Zs[i];
			}
		for(int i=0;i<N;i++)
			{
			CDM_V[0]+=VXs[i];
			}
		for(int i=0;i<N;i++)
			{
			CDM_V[1]+=VYs[i];
			}
		for(int i=0;i<N;i++)
			{
			CDM_V[2]+=VZs[i];
			}
		
		for(int i=0;i<3;i++)
			{
			CDM_V[i]/=N;
			CDM_S[i]/=N;
			}
		
		double prodscal=0;
		double norma=0;
		
		for(int i=0;i<3;i++)
			{
			prodscal+=CDM_S[i]*CDM_V[i];
			norma+=CDM_V[i]*CDM_V[i];
			}
		
		double tempo;
		
		if(norma!=0)
			tempo=-prodscal/norma;
		else
			tempo=0;
		
		if(tempo<0)
			tempo=0;
		
		vector<double> POSFIN(3,0);
		
		for(int i=0;i<3;i++)
			POSFIN[i]=CDM_V[i]*tempo+CDM_S[i];
		
		double distfin=0;
		
		for(int i=0;i<3;i++)
			distfin+=POSFIN[i]*POSFIN[i];
		
		distfin=pow(distfin,1.0/2);
		
		OUT>>fixed>>setprecision(8);
		
		OUT<<"Case #"<<c+1<<": "<<distfin<<" "<<tempo<<endl;
		
		}
		
		
	
	
    return 0;
}
