#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <sstream>
# include<fstream>
using namespace std;
# define FOR(i,a,n) for(int i=a;i<n;++i)
# define REP(i,n) FOR(i,0,n)
typedef long long LL;
ifstream fin("C-small-attempt0.in");
ofstream fout("out.txt");
LL ar[100000];
int main()
{
	int tc;
	fin>>tc;
	int cnt=0;
	while(tc--)
	{
		++cnt;
		LL n,l,h;
		fin>>n>>l>>h;
		REP(i,n) fin>>ar[i];
		bool done=false;
		FOR(i,l,h+1)
		{
			bool ok=true;
			REP(j,n)
				if((ar[j]%i)&&(i%ar[j]))
				{
					ok=false;
					break;
				}
			if(ok)
			{
				done=true;
				fout<<"Case #"<<cnt<<": "<<i<<endl;
				break;
			}
		}
		if(!done) fout<<"Case #"<<cnt<<": NO"<<endl;
	}
}
					
				
		
