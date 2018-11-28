#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>

#define	N	10000

using namespace std;

/*getline(cin,s);
istringstream ss(s);
ss >> nrtest;*/

int main(void)
{
	string s;
	
	int nrtest,nrmusicos,fh,fl,freq;
	int freqs[N];
	bool encontre,posible;
	
	getline(cin,s);
	istringstream ss(s);
	ss >> nrtest;
	
	for(int i=0;i<nrtest;i++)
	{
		getline(cin,s);
		istringstream sss(s);
		sss >> nrmusicos >> fl >> fh;
		
		getline(cin,s);
		istringstream ssss(s);
		
		for(int j=0;j<nrmusicos;j++)
		{
			ssss >> freqs[j];
		}
		
		encontre=false;
		
		for(freq=fl;(freq<=fh)&&(!encontre);freq++)
		{
			posible=true;
		
			for(int k=0;(k<nrmusicos)&&posible;k++)
			{
				if(((freq%freqs[k])!=0)&&((freqs[k]%freq)!=0))
				{
					posible=false;
				}
			}
			
			encontre=posible;
		}
		
		if(encontre)
		{
			cout << "Case #" << (i+1) << ": " << (freq-1) << endl;
		}
		else
		{
			cout << "Case #" << (i+1) << ": NO" << endl;
		}
	}
}
