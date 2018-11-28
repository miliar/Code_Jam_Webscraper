#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

ifstream dat ("b.in");
ofstream sol ("b.out");

int n,k,b,t;
int a[51],v[51],c[51],d[51],res;
bool fl[51];

int main()
{
	int p,tt;
	int i,j;
	dat >> tt;
	for(p=1;p<=tt;p++)
	{
		dat >> n >> k >> b >> t;
		for(i=0;i<n;i++) dat >>a[i];
		for(i=0;i<n;i++) dat >>v[i];
		
		res=0;
		int pp=0;
		for(i=0;i<n;i++)
		{
			fl[i]=false;
			int dist=b-a[i];
			if(dist/v[i]<t || (dist%v[i]==0 && dist/v[i]==t)) { pp++; fl[i]=true;}
		}
		sol << "Case #" << p << ": ";
		if (pp<k)
		{	
			sol << "IMPOSSIBLE" << endl;			
			continue;
		}
		else if (k==0)
		{
			sol << 0 << endl;			
			continue;		
		}
		pp=0; 
		int kk=0;
		for(i=n-1;i>=0;i--)
		{
			if (!fl[i]) pp++;
			else { res+=pp; kk++; if (kk==k) break; }
		}
		sol << res << endl;
	}
	return 0;
}