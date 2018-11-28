#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int t;scanf(" %d",&t);t;})
#define GC(x) scanf(" %c",&x)
#define sz size()
#define rz resize
#define cl clear()
#define inf (int)1e9
#define pb push_back
#define bs binary_search
#define lb lower_bound
#define ub upper_bound

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef double DD;
typedef long long LL;


struct data {
	int v,nxt;
};

int R,k,N,test[1005],seen[1005];
data D[1005];
VI temp;

int main() {
	int flag,x,y,yay=0;
	LL ans,sum;
	for (int _=GI;_--;) {
		R=GI,k=GI,N=GI;
		REP (i,N) {
			test[i]=GI;
			seen[i]=0;
		}
		REP (i,N) {
			flag=0;
			D[i].v=0;
			D[i].nxt=0;
			FOR (j,i,i+N) {
				x=j%N;
				if(D[i].v + test[x] > k) {
					D[i].nxt=x;
					flag=1;
					break;
				}
				else D[i].v += test[x];
			}
			if(flag==0) D[i].nxt=i;
		}
//		cout<<endl;
//		REP (i,N) cout<<D[i].v<<" "<<D[i].nxt<<endl;
//		cout<<endl;
		temp.cl;
		x=0;
		while(1) {
			if(seen[x]==1) break;
			seen[x]=1;
			temp.pb(x);
			x=D[x].nxt;
		}
//		REP (i,temp.sz) cout<<temp[i]<<" ";
//		cout<<endl;
//		cout<<x<<endl<<endl;
		ans=0;
		while(1) {
			if(*temp.begin() == x) break;
			ans += D[*temp.begin()].v;
			temp.erase(temp.begin());
			R--;
			if(R==0) {
				printf("Case #%d: %lld",++yay,ans);
				goto label;
			}
		}
		sum=0;
		REP (i,temp.sz) sum += D[temp[i]].v;
//		cout<<R<<" "<<temp.sz<<" "<<sum<<endl;
		ans += (R/temp.sz)*sum;
		R %= temp.sz;
		REP (i,R) ans += D[temp[i]].v;
				printf("Case #%d: %lld",++yay,ans);
		label: printf("\n");
	}
	return 0;
}

