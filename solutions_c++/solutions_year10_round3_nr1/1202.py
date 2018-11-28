#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>
#include <set>
#include <algorithm>
#include <map>
#include <sstream>
#include <cfloat>
//# define INP cin
//# define OUT cout

using namespace std;

typedef long long int64;
typedef long double ld;



int main (int argc, char * const argv[]) {
    
	fstream INP("input.txt", fstream::in);
	fstream OUT("output.txt",fstream::out);
	
	int T;
	
	INP>>T;
	
	for(int cont=1;cont<=T;cont++)
	{
		int N;
		INP>>N;
		
		vector<int> A(N,0);
		vector<int> B(N,0);
		for(int i=0;i<N;i++)
			INP>>A[i]>>B[i];
		
		
		set< pair<double, double> > pts;
		
		
		for(int i=0;i<N;i++)
			for(int j=i+1;j<N;j++)
			{
				double m1=(double)(B[i]-A[i])/2;
				double q1=(double)(B[i]+A[i])/2;
				double m2=(double)(B[j]-A[j])/2;
				double q2=(double)(B[j]+A[j])/2;
				
				if(m1==m2)
					continue;
				
				double x=(q2-q1)/(m1-m2);
				double y=m1*x+q1;
				
				
				
				if(x>-1 and x<1)
					pts.insert(make_pair(x,y));
				
			}
		
		OUT<<"Case #"<<cont<<": "<<pts.size()<<endl;	
	}
	
	
    return 0;
}
