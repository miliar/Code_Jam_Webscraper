#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
#include <iomanip>

using namespace std;

typedef vector <int> VI;
typedef vector <string> VS;
typedef long long LL;
typedef stringstream SS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define PB push_back
#define sz size()
#define MP make_pair
#define two(x) (1<<(x))


/////////////////////////////////////////////////////////////////////////////////

int N;
string s[50];

int main()
{
	int testcases;
	cin >> testcases;
	int index=0;
	while(index<testcases)
	{
		cin>>N;
		REP(i,N) { cin>>s[i]; REP(j,s[i].rfind('1')) s[i][j]='1'; }

		int ret=0;

		REP(i,N)
		{
			string sm=s[i];
			if(sm.rfind('1')>i)
			{
				int t=i;
				for(int j=i+1; j<N; j++)
				{
					if(s[j].rfind('1')<=i)
					{ t=j; break; }
				}
				for(int k=t; k>i; k--)
				{
					swap(s[k], s[k-1]);
					ret++;
				}
			}
		}

		cout << "Case #" << ++index <<": " << ret << endl;
	}
	return 0;

}
