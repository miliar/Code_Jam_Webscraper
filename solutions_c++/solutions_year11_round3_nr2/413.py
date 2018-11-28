#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>

#define	N	1000000
#define	C	1000

using namespace std;

/*getline(cin,s);
istringstream ss(s);
ss >> nrtest;*/

int main(void)
{
	string s;
	
	long int nrtest,nrsb,t,nrestrella,nrdistintos,suma,n;
	int dist[C],estrella[N],ep[N];
	
	getline(cin,s);
	istringstream ss(s);
	ss >> nrtest;
	
	for(int i=0;i<nrtest;i++)
	{
		getline(cin,s);
		istringstream sss(s);
		sss >> nrsb >> t >> nrestrella >> nrdistintos;
		
		for(int j=0;j<nrdistintos;j++)
		{
			sss >> dist[j];
		}
		
		for(int j=0;j<nrestrella;j++)
		{
			estrella[j]=dist[j%nrdistintos];
		}
		
		suma=0;
		n=0;
		for(int j=0;j<nrestrella;j++)
		{
			if((2*suma)>=t)
			{
				ep[n++]=estrella[j];
			}
			else
			{
				if((2*(suma+estrella[j]))>=t)
				{
					ep[n++]=(suma+estrella[j]-(t/2));
				}
			}
			
			suma+=estrella[j];
		}
		
		suma*=2;
		
		sort(&ep[0],&ep[n]);
		
		for(int j=0;j<min(nrsb,n);j++)
		{
			suma-=ep[n-1-j];
		}
		
		cout << "Case #" << (i+1) << ": " << suma << endl;
	}
}
