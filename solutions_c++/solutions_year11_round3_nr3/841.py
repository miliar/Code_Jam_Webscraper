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
#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps (1e-9)
#define inf (1<<29)
#define i64 long long
#define u64 unsigned i64

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c.ans","w",stdout);
	int t,i,cs =1,j,a[105],L,H,n;
	cin>>t;
	while(t--){
		cin>>n>>L>>H;
		for(i = 0;i<n;i++){
			cin>>a[i];
		}
		for(i = L;i<=H;i++){
			for(j = 0;j<n;j++){
				if(a[j]%i && i%a[j]) break;
			}
			if(j==n) break;
		}
		printf("Case #%d: ",cs++);
		if(i<=H) printf("%d\n",i);
		else puts("NO");
	}
	return 0;
}