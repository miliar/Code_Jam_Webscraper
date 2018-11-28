#include<iostream>
#include<list>
#include<queue>
#include<vector>
#include<set>
#include<map>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<cstring>
#include<algorithm>
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,a,b) for(i=(a);i<(b);++i)
#define PB push_back
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<LL> VLL;
const int dx[]={-1,0,1,0,-1,-1,1,1};
const int dy[]={0,1,0,-1,-1,1,-1,1};
int g[1000];
int p[1000];
LL w[1000];
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int i,T;
	scanf("%d",&T);
	REP(i,T) {
		cout<<"Case #"<<i+1<<": ";
		int r,k,n;
		scanf("%d%d%d",&r,&k,&n);
		int j;
		REP(j,n) scanf("%d",&g[j]);
		memset(p,-1,sizeof(p));
		p[0]=0;
		w[0]=0;
		j=0;
		int cnt=0;
		LL v=0;
		int cur=0;
		bool flag=false;
		do {
			++cnt;
			cur=0;
			int lastj=j;
			while (cur+g[j]<=k) {
				cur+=g[j];
				j++;
				if (j==n) j=0;
				if (j==lastj) break;
			}
			v+=cur;
			if (flag) continue;
			if (p[j]==-1) {
				p[j]=cnt;
				w[j]=v;
			} else {
				flag=true;
				int t=(r-cnt)/(cnt-p[j]);
				cnt+=t*(cnt-p[j]);
				v+=(v-w[j])*t;
			}
		} while (cnt<r);
		cout<<v<<endl;
	}
	
}
