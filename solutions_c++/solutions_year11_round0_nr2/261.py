#include <iostream>
#include <sstream>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(), (a).end()
#define CL(a, v) memset(a, v, sizeof(a))
#define sz(a) (int)a.size()
#define pb push_back
#define REP(i, n) for(int i=0; i<n; ++i)
#define FOR(i, a, b) for(int i=a; i<b; ++i)
#define FORD(i, a, b) for(int i=a; i>=b; --i)
#define X first
#define Y second

template <class T> void smin(T& a, const T& b) { if(a>b) a=b; }
template <class T> void smax(T& a, const T& b) { if(a<b) a=b; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a%b) : a; }
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define M 100
#define N 110

int test,t;

int used[256];
int c,d,n,cnt;
string rules[M],opp[M],s;
char res[N];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&test);
	FOR(t,1,test+1)
	{
		cin >> c;
		REP(i,c)
			cin >> rules[i];
		REP(i,c)
		{
			rules[c+i] = rules[i];
			swap(rules[c+i][0], rules[c+i][1]);
		}
		c *= 2;
		cin >> d;
		REP(i,d)
			cin >> opp[i];
		cin >> n >> s;
		CL(used, 0);
		cnt = 0;
		REP(j,n)
		{
			++cnt;
			res[cnt] = s[j];
			used[s[j]]++;
			REP(i,c)
				if(rules[i][0] == res[cnt] && rules[i][1] == res[cnt-1])
				{
					used[res[cnt]]--;
					used[res[cnt-1]]--;
					res[cnt-1] = rules[i][2];
					--cnt;
					used[res[cnt]]++;
					break;
				}
			REP(i,d)
				if(used[opp[i][0]] && used[opp[i][1]])
				{
					cnt = 0;
					CL(used,0);
					break;
				}
		}
		printf("Case #%d: [",t);
		FOR(i,1,cnt)
			printf("%c, ",res[i]);
		if(cnt > 0)
			printf("%c]\n",res[cnt]);else
			printf("%]\n");
	}
	return 0;
}
