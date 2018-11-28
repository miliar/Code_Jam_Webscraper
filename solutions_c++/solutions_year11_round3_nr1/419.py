#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>

#define	R	50
#define	C	50

#define	A	'#'
#define	B	'.'
#define	RA	'/'
#define	RB	'\\'
#define	RC	'\\'
#define	RD	'/'

using namespace std;

/*getline(cin,s);
istringstream ss(s);
ss >> nrtest;*/

int main(void)
{
	string s;
	
	int nrtest,nrfila,nrcolumna;
	char tabla[R][C];
	bool posible;
	
	getline(cin,s);
	istringstream ss(s);
	ss >> nrtest;
	
	for(int i=0;i<nrtest;i++)
	{
		getline(cin,s);
		istringstream sss(s);
		sss >> nrfila >> nrcolumna;
		
		for(int j=0;j<nrfila;j++)
		{
			getline(cin,s);
			istringstream ssss(s);
			
			for(int k=0;k<nrcolumna;k++)
			{
				ssss >> tabla[j][k];
			}
		}
		
		posible=true;
		
		for(int j=0;j<nrfila;j++)
		{
			for(int k=0;k<nrcolumna;k++)
			{
				if(tabla[j][k]==A)
				{
					tabla[j][k]=RA;
					
					if(((k+1)<nrcolumna)&&(tabla[j][k+1]==A))
					{
						tabla[j][k+1]=RB;
					}
					else
					{
						posible=false;
					}
					if(((j+1)<nrcolumna)&&(tabla[j+1][k]==A))
					{
						tabla[j+1][k]=RC;
					}
					else
					{
						posible=false;
					}
					if(((j+1)<nrcolumna)&&((k+1)<nrcolumna)&&(tabla[j+1][k+1]==A))
					{
						tabla[j+1][k+1]=RD;
					}
					else
					{
						posible=false;
					}
				}
			}
		}
		
		cout << "Case #" << i+1 << ":" << endl;
		
		if(posible)
		{
			for(int j=0;j<nrfila;j++)
			{
				for(int k=0;k<nrcolumna;k++)
				{
					cout << tabla[j][k];
				}
				
				cout << endl;
			}
		}
		else
		{
			cout << "Impossible" << endl;
		}
	}
}
