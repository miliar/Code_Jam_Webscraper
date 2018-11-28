#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <algorithm>
#include <numeric>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <iterator>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i = 0; i < n; i++)
#define FOR(i,s,e) for(int i = s; i < e; i++)
#define FORD(i,e,s) for(int i = e; i > s; i--)
#define ALL(x) x.begin(), x.end()
#define OUT(x) cout<<#x<<" = "<<x<<endl;
#define PB push_back
typedef long long ll;

#define LETTERS ('z'-'a'+1)
char T[5000][16];
int zawiera[500][15][LETTERS];

int main()
{
	int L, D, N;
	ios_base::sync_with_stdio(0);
	cin>>L>>D>>N;
	REP(i,D)
	{
		cin>>T[i];
		//cout<<T[i]<<endl;
		REP(j,L)
			T[i][j]-='a';
	}
	
	memset(zawiera, 0, sizeof(zawiera));
	REP(i,N)
	{
		char buf[1000];
		cin>>buf;

		int pos=0;
		REP(j,L)
			if(buf[pos]=='(')
			{
				while(buf[++pos] != ')')
					zawiera[i][j][ buf[pos] - 'a' ] = 1;
				pos++;
			}
			else
			{
				zawiera[i][j][ buf[pos] - 'a'] = 1;
				pos++;
			}

		int res = 0;
		REP(j, D)
		{
			int pos = 0;
			while(zawiera[i][pos][ T[j][pos] ] != 0)
				pos++;
			if(pos==L)
				res++;
		}		
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}

	return 0;
}

