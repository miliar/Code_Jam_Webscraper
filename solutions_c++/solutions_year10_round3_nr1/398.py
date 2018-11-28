#include<algorithm>
#include<iostream>
#include<cmath>
#include<string>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<list>

#define mn(a,b) ( (a) < (b) ? (a) : (b) )
#define mx(a,b) ( (a) > (b) ? (a) : (b) )
#define ab(a) ( (a) < (0) ? (-a) : (a) )

#define MP make_pair
#define PB push_back
#define F first
#define S second

#define ll long long

using namespace std;

int T,n,l[1000],r[1000];


void solve(int x){
	int ans=0;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
		scanf("%d%d",&l[i],&r[i]);	
	for(int i=0;i<n;i++)
		for(int j=i+1;j<n;j++){
			if((l[i]-l[j])*(r[i]-r[j])<0)
			ans++;
		}
	printf("Case #%d: %d\n",x,ans);
	
}

int main(){

freopen("input.txt","r",stdin);
freopen("output.out","w",stdout);
scanf("%d",&T);
for(int i=1;i<=T;i++)
	solve(i);

return 0;
}