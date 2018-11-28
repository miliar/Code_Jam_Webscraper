#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<queue>
#include<cmath>
#include<set>
#include<map>
#include<vector>
#include<complex>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define REP(a,b,c) for(int a=b; a<c; a++)
#define REPS(a,b,c) for(int a=b; a<=c; a++)
#define REPD(a,b,c) for(int a=b; a>=c; a--)
#define RESET(a,b) memset(a,b,sizeof(a))
using namespace std;

typedef long long LL;
typedef complex<double> pt;
typedef pair<int,int> pii;

const int INF = 1000000000;
const double EPS = 1e-9;

//sicasli's template

void solve(int &cas)
{
	int ganti[30][30];
	RESET(ganti,-1);
	
	vector<int> benci[30];
	int jum[30];
	
	int c;
	scanf("%d",&c);
	
	while (c--)
	{
		char s[5];
		scanf("%s",s);
		
		ganti[s[0]-'A'][s[1]-'A'] = s[2]-'A';
		ganti[s[1]-'A'][s[0]-'A'] = s[2]-'A';
	}	
	
	int d;
	scanf("%d",&d);
	
	while (d--)
	{
		char s[5];
		scanf("%s",s);
		
		benci[s[0]-'A'].pb(s[1]-'A');
		benci[s[1]-'A'].pb(s[0]-'A');
	}
	
	int n;
	scanf("%d",&n);
	
	char s[n+5];
	scanf("%s",s);
	
	RESET(jum,0);
	
	vector<char> ans;
	int sz=0;
	
	REP(i,0,n)
	{
		ans.pb(s[i]);
		jum[s[i]-'A'] += 1;
		sz ++;
		
		while (sz>1 && ganti[ans[sz-1]-'A'][ans[sz-2]-'A']!=-1)
		{
			char haha = ganti[ans[sz-1]-'A'][ans[sz-2]-'A']+'A';
			
			jum[ans[sz-1]-'A'] --;
			jum[ans[sz-2]-'A'] --;
			jum[haha-'A'] ++;
			
			ans.pop_back();
			ans.pop_back();
			ans.pb(haha);
			
			sz--;
		}
		
		REP(j,0,sz)
		{
			int zz = benci[ans[j]-'A'].size();
			REP(k,0,zz) if (jum[benci[ans[j]-'A'][k]])
			{
				RESET(jum,0);
				ans.clear();
				sz = 0;
				break;	
			}
		}
	}
	
	printf("Case #%d: [",cas);
	if (sz) printf("%c",ans[0]);
	REP(i,1,sz) printf(", %c",ans[i]);
	printf("]\n");
}

int main()
{
	int t;
	scanf("%d",&t);
	
	REPS(cas,1,t) solve(cas);
}
