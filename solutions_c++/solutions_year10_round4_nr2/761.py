#include<cstdio>
#include<cstring>
#include<cmath>
#include<cctype>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<numeric>
#include<fstream>
using namespace std;
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define memo(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps (1e-9)
#define inf (1<<29)

int M[2000],ret;
void solve(int lf,int rt){
	int i;
	if(lf==rt){
		if(M[rt]) ret++;
		return;
	}
	for(i = lf;i<=rt;i++){
		if(M[i]) break;
	}
	if(i>rt) return;
	for(i = lf;i<=rt;i++){
		M[i] = max(M[i]-1,0);
	}
	ret++;
	solve(lf,(rt+lf)/2);
	solve((rt+lf)/2+1,rt);
}
int main(){
	freopen("B-small.in","r",stdin);
	freopen("B-small.ans","w",stdout);
	int t,cs,i,p,emni,j;
	cin>>t;
	for(cs=1;cs<=t;cs++){
		cin>>p;
		for(i = 0;i<(1<<p);i++){
			cin>>M[i];
			M[i] = p - M[i];
		}
		for(i = p-1;i>=0;i--){
			for(j = 0;j<(1<<i);j++) cin>>emni;
		}
		ret = 0;
		solve(0,(1<<p)-1);
		printf("Case #%d: %d\n",cs,ret);
	}
	return 0;
}