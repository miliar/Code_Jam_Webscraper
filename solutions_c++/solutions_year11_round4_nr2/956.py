#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <iomanip>

#define 	RMAX	500
#define	CMAX	500

using namespace std;

/*getline(cin,s);
istringstream ss(s);
ss >> nrtest;*/

int main(void)
{
	string s;

	int nrtest,nrfilas,nrcolumnas,mesperada,kmax;
	long int cmasa[2];
	long int centro[2];
	char desvio[RMAX][CMAX];
	bool encontre;
	
	getline(cin,s);
	istringstream ss(s);
	ss >> nrtest;
	
	for(int i=0;i<nrtest;i++)
	{
		getline(cin,s);
		istringstream sss(s);
		sss >> nrfilas >> nrcolumnas >> mesperada;
		
		for(int j=0;j<nrfilas;j++)
		{
			getline(cin,s);
			istringstream ssss(s);
		
			for(int k=0;k<nrcolumnas;k++)
			{
				ssss >> desvio[j][k];
			}
		}
		
		encontre=false;
		for(kmax=min(nrfilas,nrcolumnas);(!encontre)&&(kmax>=3);kmax--)
		{
			for(int j=0;j<=(nrfilas-kmax);j++)
			{
				for(int k=0;k<=(nrcolumnas-kmax);k++)
				{
					centro[0]=kmax+2*j;
					centro[1]=kmax+2*k;
					cmasa[0]=0;
					cmasa[1]=0;
					for(int m=j;m<(j+kmax);m++)
					{
						for(int n=k;n<(k+kmax);n++)
						{
							if(!(((m==j)&&(n==k))||((m==j)&&(n==(k+kmax-1)))||((m==(j+kmax-1))&&(n==k))||((m==(j+kmax-1))&&(n==(k+kmax-1)))))
							{
								cmasa[0]+=(2*m+1-centro[0])*(mesperada+desvio[m][n]);
								cmasa[1]+=(2*n+1-centro[1])*(mesperada+desvio[m][n]);
							}
						}
					}
					
					if((cmasa[0]==0)&&(cmasa[1]==0))
					{
						encontre=true;
					}
				}
			}
		}
		
		kmax++;
		
		if(encontre)
		{
			cout << "Case #" << (i+1) << ": " << kmax << endl;
		}
		else
		{
			cout << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
		}
	}
	
	return(1);
}
