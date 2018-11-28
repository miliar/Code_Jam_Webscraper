#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<bitset>
#include<cassert>

using namespace std;

typedef long long ll;
typedef pair<int,int> pint;
typedef vector<int> vint;

#define mp make_pair
#define pb push_back
#define REP(i,a,b) for(int i=a;i<b;++i)
#define rep(i,n) REP(i,0,n)

int t,n;
char a[45][45];
int b[45];
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>t;
	REP(cas,1,t+1){
		cin>>n;
		rep(y,n){
			scanf("%s",a[y]);
//			printf("%s\n",a[y]);
			int i=n-1;
			b[y]=n-1;
			while(i>=0 && a[y][i--]=='0')--b[y];
//			cout<<b[y]<<endl;
		}
		int cnt=0;
		rep(y,n){
			if(b[y]<=y)continue;
			int i;
			for(i=y;b[i]>y;++i,++cnt);
			for(int j=i;j>=y+1;--j)swap(b[j],b[j-1]);
		}
		printf("Case #%d: %d\n",cas,cnt);
	}
	return 0;
}
