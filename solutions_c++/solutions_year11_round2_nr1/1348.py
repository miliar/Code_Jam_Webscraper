#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>

using namespace std;

#define	N	100
#define	G	'1'
#define	P	'0'
#define	NJ	'.'

/*getline(cin,s);
istringstream ss(s);
ss >> nrtest;*/

int main(void)
{
	string s;
	
	int nrtest,nrequipo,nrjugados,nrj;
	char tabla[N][N];
	double wp[N],owp[N],oowp[N],rpi[N];
	double wpt;
	
	getline(cin,s);
	istringstream ss(s);
	ss >> nrtest;
	
	for(int i=0;i<nrtest;i++)
	{
		getline(cin,s);
		istringstream sss(s);
		sss >> nrequipo;
		
		for(int j=0;j<nrequipo;j++)
		{
			getline(cin,s);
			istringstream ssss(s);
			
			for(int k=0;k<nrequipo;k++)
			{
				ssss >> tabla[j][k];
			}
		}
		
		for(int j=0;j<nrequipo;j++)
		{
			nrjugados=0;
			wp[j]=0;
			
			for(int k=0;k<nrequipo;k++)
			{
				if(tabla[j][k]!=NJ)
				{
					wp[j]+=(tabla[j][k]-P);
					nrjugados++;
				}
			}
			
			wp[j]/=nrjugados;
		}
		
		for(int j=0;j<nrequipo;j++)
		{
			nrjugados=0;
			owp[j]=0;
			
			for(int k=0;k<nrequipo;k++)
			{
				if(tabla[j][k]!=NJ)
				{
					nrj=0;
					wpt=0;
		
					for(int m=0;m<nrequipo;m++)
					{
						if((tabla[k][m]!=NJ)&&(m!=j))
						{
							wpt+=(tabla[k][m]-P);
							nrj++;
						}
					}
		
					wpt/=nrj;
				
					owp[j]+=wpt;
					nrjugados++;
				}
			}
			
			owp[j]/=nrjugados;
		}
		
		for(int j=0;j<nrequipo;j++)
		{
			nrjugados=0;
			oowp[j]=0;
			
			for(int k=0;k<nrequipo;k++)
			{
				if(tabla[j][k]!=NJ)
				{
					oowp[j]+=owp[k];
					nrjugados++;
				}
			}
			
			oowp[j]/=nrjugados;
		}
		
		for(int j=0;j<nrequipo;j++)
		{
			rpi[j]=0.25*wp[j]+0.5*owp[j]+0.25*oowp[j];
		}
		
		cout << "Case #" << i+1 << ":" << endl;
		
		for(int j=0;j<nrequipo;j++)
		{
			cout << rpi[j] << endl;
		}
	}
}
