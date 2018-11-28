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
	int r,k,n;
	int g[1001];
	Int m[1001*1001];
	Int ans;
	Int ansc;
	for(int ii=0;ii<t;ii++){
		cin >> r >> k >> n;
		int i,j,l;
		for(i=0;i<n;i++) scanf("%d",&g[i]);
		for(i=0;i<=1000;i++) for(j=0;j<=1000;j++) m[i*j]=0;
		ans=0;
		ansc=0;
		for(i=0;;){
			for(j=0,l=0;l<n;i++,i%=n,l++){
//		cout << i << endl;
				j+=g[i];
				if(j+g[(i+1)%n]>k) break;
			}
			i++;
			i%=n;
			m[ansc++]=j;
			ans+=j;
			if(i==0) break;
		}
		Int ans2=0;
		ans2+=ans*(r/ansc);
		for(i=0;i<r%ansc;i++){
//		cout << i << " " << m[i] << endl;
			ans2+=m[i];
		}
		printf("Case #%d: %lld\n",ii+1,ans2);
	}
	return 0;
}


