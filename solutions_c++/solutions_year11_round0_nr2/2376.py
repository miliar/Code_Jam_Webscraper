#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>

#define	C	36
#define	D	28
#define	N	100

using namespace std;

/*getline(cin,s);
istringstream ss(s);
ss >> nrtest;*/

int main(void)
{
	string s;
	
	bool combined,opposed;
	
	char combine[C][3];
	char oppose[D][2];
	char ein[N];
	char eout[N];;
	
	int nrtest,nrcombine,nroppose,nrelement,n;
	
	getline(cin,s);
	istringstream ss(s);
	ss >> nrtest;
	
	for(int i=0;i<nrtest;i++)
	{
		getline(cin,s);
		istringstream ss(s);
		
		ss >> nrcombine;
		
		for(int j=0;j<nrcombine;j++)
		{
			ss >> combine[j];
		}
		
		ss >> nroppose;
		
		for(int j=0;j<nroppose;j++)
		{
			ss >> oppose[j];
		}
		
		ss >> nrelement >> ein;
		
		n=0;
		
		for(int j=0;j<nrelement;j++)
		{
			if(n==0)
			{
				eout[n++]=ein[j];
			}
			else
			{
				combined=false;
				
				for(int k=0;k<nrcombine;k++)
				{
					if(((ein[j]==combine[k][0])&&(eout[n-1]==combine[k][1]))||((ein[j]==combine[k][1])&&(eout[n-1]==combine[k][0])))
					{
						eout[n-1]=combine[k][2];
						combined=true;
					}
				}
				
				if(!combined)
				{
					opposed=false;
					
					for(int k=0;k<nroppose;k++)
					{
						for(int l=0;l<n;l++)
						{
							if(((ein[j]==oppose[k][0])&&(eout[l]==oppose[k][1]))||((ein[j]==oppose[k][1])&&(eout[l]==oppose[k][0])))
							{
								n=0;
								opposed=true;
							}
						}
					}
					
					if(!opposed)
					{
						eout[n++]=ein[j];
					}
				}
			}
		}
		
		cout << "Case #" << i+1 << ": [";
		
		for(int j=0;j<n;j++)
		{
			if(j==0)
			{
				cout << eout[j];
			}
			else
			{
				cout << ", " << eout[j];
			}
		}
		
		cout << "]" << endl;
	}
}
