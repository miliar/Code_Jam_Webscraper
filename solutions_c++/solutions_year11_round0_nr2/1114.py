
#define _CRT_SECURE_NO_DEPRECATE 

#include <string> 
#include <vector> 
#include <map> 
#include <list> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <stack> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <cstdlib> 
#include <cstdio> 
#include <cctype> 
#include <algorithm> 
#include <utility> 
#include <bitset>

using namespace std; 

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
#define pb push_back
#define mp make_pair
#define EPS 1e-7
#define Pi 3.14159265358979

typedef long long Long;
typedef unsigned long long ULong;
typedef unsigned int Uint;
typedef unsigned char Uchar;
typedef vector <int> VI;
typedef pair <int, int> PI;

set<pair<char,char> > Set;
map<pair<char,char>,char> Map;
char c[1<<10];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int T;
	cin>>T;
	REP(tests,T)
	{
		Map.clear();
		int n;
		scanf("%d",&n);
		REP(i,n)
		{
			char buf[10];
			scanf(" %s",buf);
			if (buf[0]>buf[1])
				swap(buf[0],buf[1]);
			Map[mp(buf[0],buf[1])]=buf[2];
		}

		Set.clear();
		int m;
		scanf("%d",&m);
		REP(i,m)
		{
			char buf[10];
			scanf(" %s",buf);
			if (buf[0]>buf[1])
				swap(buf[0],buf[1]);
			Set.insert(mp(buf[0],buf[1]));
		}

		int len;
		scanf("%d ",&len);
		gets(c);

		vector<char> v;
		REP(i,len)
		{
			v.push_back(c[i]);
			
			while (true)
			{
				if (v.size()<2)
					break;

				char c1=v[v.size()-1];
				char c2=v[v.size()-2];
				if (c1>c2)
					swap(c1,c2);

				if (Map.count(mp(c1,c2)))
				{
					v.pop_back();
					v.pop_back();
					v.push_back(Map[mp(c1,c2)]);
					continue;
				}

				REP(i,(int)v.size()-1)
				{
					c1=v[i];
					c2=v[(int)v.size()-1];

					if (c1>c2)
						swap(c1,c2);

					if (Set.count(mp(c1,c2)))
					{
						v.clear();
						break;
					}
				}

				break;
			}
		}

		printf("Case #%d: [",tests+1);
		if (v.size()==0)
		{
			puts("]");
		} else
		{
			REP(i,(int)v.size())
			{
				printf("%c%s",v[i],i==(int)v.size()-1?"]\n":", ");
			}
		}
	}

	return 0;
}
