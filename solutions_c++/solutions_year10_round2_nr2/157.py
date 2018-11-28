#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<queue>
#include<complex>
#include<numeric>
#include<bitset>

using namespace std;
typedef long long Int;
typedef vector<int> vint;
typedef vector<vint> vvint;
typedef pair<Int,Int> pint;

int main(){
	int t;
	cin >> t;
	for(int l=0;l<t;l++){
		int n,k,b,T;
		cin >> n >> k >> b >> T;
		int x[60];
		int v[60];
		int i,j;
		for(i=0;i<n;i++){
			scanf("%d",&x[i]);
		}
		for(i=0;i<n;i++){
			scanf("%d",&v[i]);
		}
		int f[60];
		for(i=0;i<n;i++){
			if((b-x[i])>v[i]*T) f[i]=0;
			else f[i]=1;
		}
		int ans=0;
		for(i=n-1,j=0;i>=0&&j<k;i--){
			if(f[i]==1){
				j++;
				for(int m=i+1;m<n;m++){
					if(f[m]==0) ans++;
				}
			}
		}
		if(j==k) printf("Case #%d: %d\n",l+1,ans);
		else printf("Case #%d: IMPOSSIBLE\n",l+1);
	}
	return 0;
}


