/// In The Name Of God

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstring>


using namespace std;

#define REP(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

const int maxn=2000*1000+5;
vector<int> v[maxn];

inline void f(int n,int ten,int r){
	int i,t,j,tmp=ten,k;
	bool flag=true;
	for(i=0;i<r-1;i++){
		if((n%tmp) >= tmp/10){
			flag=true;
			k= (n%tmp)*(ten/tmp)*10 + n/tmp;
			if(k>n){
				for(j=0;j<v[n].size();j++)
					if(v[n][j]==k){
						flag=false;
						break;
					}
				if(flag)
					v[n].push_back(k);
			}
		}
		tmp/=10;
	}
}

int main(){
	ios::sync_with_stdio(false);
	int n,t,i,j,tsc,k,ten,r;
	int a,b;
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	cin>>tsc;
	ten=10;r=1;
	for(i=11;i<maxn;i++){
		if(i>ten){
			ten*=10;
			r++;
		}
		f(i,ten/10,r);
	}
	int ans;
	REP(t,tsc){
		ans=0;
		cin>>a>>b;
		for(i=a;i<b;i++){
			REP(r,v[i].size())
				if(v[i][r]<=b)
					ans++;
		}
		printf("Case #%d: ",t+1);
		cout<<ans<<endl;
	}
	return 0;
}
