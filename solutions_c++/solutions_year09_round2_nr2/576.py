#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string.h>
using namespace std;
#define REP(i,n) for(int i=0,n_=(n);i<n_;i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOR(i,a,b) for (int i=a,b_=b;i<=(b);i++)
#define ALL(a) a.begin(),a.end()
#define SZ(a) (int)(a).size()
#define SORT(a) sort(ALL(a))
#define INF 1073741823
#define DEB(x) cerr<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
#define i64 long long 
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
vector<int> SplitInt(string &s)
{
	vector<int>Res;int tmp;stringstream a(s);
	while (a>>tmp){Res.push_back(tmp);}return Res;
}

vector<string> SplitStr(string &s)
{
	vector<string>Res;string tmp;stringstream a(s);
	while (a>>tmp){Res.push_back(tmp);}return Res;
}
char Pal[123];
int main ()
{
	int c;
	scanf ("%d",&c);

	FOR(cas,1,c)
	{
		
		string res;
		int n;
		scanf ("%s",Pal);
		string a,b,best;
		a=Pal;
		b=a;
		best=a;
		//SORT(b);
		
		if(next_permutation(ALL(b)))
		{
			//DEB(b);
			printf ("Case #%d: %s\n",cas,b.c_str());
			continue;
		}
		else
		{
			//DEB("asd");
			if (b.find('0')==-1)
			{
				SORT(b);
				b=b.substr(0,1)+string(1,'0')+b.substr(1);
				printf ("Case #%d: %s\n",cas,b.c_str());
				continue;
			}
			else
			{
				string z,t;
				REP(i,SZ(b))
				{
					if (b[i]=='0')
						z+='0';
					else
						t+=b[i];
				}
				SORT(t);
				z+='0';
				b=t.substr(0,1)+z+t.substr(1);
				printf ("Case #%d: %s\n",cas,b.c_str());
				continue;
			}
		}
		
		
		DEB(best);
		
		//printf ("Case #%d: %s\n",cas,best.c_str());
	}
	return 0;
}

