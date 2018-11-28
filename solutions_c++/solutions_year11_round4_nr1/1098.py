#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <iomanip>

#define	NMAX	1000

using namespace std;

/*getline(cin,s);
istringstream ss(s);
ss >> nrtest;*/

void quicksort(double* izq, double* der,double* derb, double* izqb,double* derc,double* izqc);
void swap(double* a, double* b);

int main(void)
{
	string s;
	
	double xcorredor,xcintas,vcaminando,vcorriendo,tcorriendo,ttotal;
	double xic[NMAX];
	double xfc[NMAX];
	double vc[NMAX];
	double temp;
	
	int nrtest,nrcintas;
	
	getline(cin,s);
	istringstream ss(s);
	ss >> nrtest;
	
	for(int i=0;i<nrtest;i++)
	{
		getline(cin,s);
		istringstream sss(s);
		sss >> xcorredor >> vcaminando >> vcorriendo >> tcorriendo >> nrcintas;
		
		xcintas=0;
		
		for(int j=0;j<nrcintas;j++)
		{
			getline(cin,s);
			istringstream ssss(s);
			ssss >> xic[j] >> xfc[j] >> vc[j];
			xcintas+=(xfc[j]-xic[j]);
		}
		
		for (int j=nrcintas;j>0;j--)
		{
			for (int k=1;k<j;k++)
			{
				if (vc[k-1]>vc[k])
				{
					temp=vc[k-1];
					vc[k-1]=vc[k];
					vc[k]=temp;
					
					temp=xic[k-1];
					xic[k-1]=xic[k];
					xic[k]=temp;
					
					temp=xfc[k-1];
					xfc[k-1]=xfc[k];
					xfc[k]=temp;
				}
			}
		}
		
		if((xcorredor-xcintas)<=(vcorriendo*tcorriendo))
		{
			ttotal=(xcorredor-xcintas)/vcorriendo;
			tcorriendo-=ttotal;
		}
		else
		{
			ttotal=tcorriendo+(xcorredor-xcintas-vcorriendo*tcorriendo)/vcaminando;
			tcorriendo=0;
		}
		
		for(int j=0;j<nrcintas;j++)
		{
			if((xfc[j]-xic[j])<=((vc[j]+vcorriendo)*tcorriendo))
			{
				ttotal+=((xfc[j]-xic[j])/(vc[j]+vcorriendo));
				tcorriendo-=((xfc[j]-xic[j])/(vc[j]+vcorriendo));
			}
			else
			{
				ttotal+=(tcorriendo+(xfc[j]-xic[j]-(vc[j]+vcorriendo)*tcorriendo)/(vc[j]+vcaminando));
				tcorriendo=0;
			}
		}
		
		cout << "Case #" << (i+1) << ": " <<  setiosflags(ios::fixed) << setprecision(9) << ttotal << endl;
		
	}
	
	return(1);
}
