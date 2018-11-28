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

string a;
set <char> Q;
VI temp;
//int seen[70];

int main() {
	int cnt,p,yo=0;
	LL ans;
	for(int _=GI;_--;) {
		cin>>a;
		Q.clear();
		REP (i,a.sz) Q.insert(a[i]);
		cnt=Q.sz;
		if(cnt==1) cnt++;
//		cout<<cnt<<endl;
		
		temp.clear();
		temp.rz(a.sz,-1);
		temp[0]=1;

		p=0;
		FOR (i,1,a.sz)
			if(a[i]==a[0]) {temp[i]=1;}
		FOR (i,1,a.sz) {
			if(temp[i]!=-1) continue;
			temp[i]=p++;
			if(p==1) p=2;
			FOR (j,i+1,a.sz) {
				if(a[j]==a[i]) {temp[j]=temp[i];}
			}
		}
		ans=0;
//		REP (i,temp.sz) cout<<temp[i]<< " ";
		REP (i,temp.sz) ans=(LL)((LL)ans*(LL)cnt+(LL)temp[i]);
		printf("Case #%d: %lld\n",++yo,ans);
	}
	return 0;
}

