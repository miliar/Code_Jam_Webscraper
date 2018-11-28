#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
using namespace std;
typedef pair<int,int> pi;
typedef double lf;
typedef long double llf;
typedef long long int lld;
typedef vector<int> vi;

int t,tt,n,T[1111],nwd,lol;

int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		tt++;
		for(int i=1;i<=n;i++)
			scanf("%d",&T[i]);
		nwd=abs(T[1]-T[2]);
		//printf("%d\n",nwd);
		for(int i=2;i<n;i++)
			nwd=__gcd(nwd,abs(T[i]-T[i+1]));
	//	printf("%d\n",nwd);
		lol=T[1]%nwd;
		if(lol==0) printf("Case #%d: 0\n",tt);
		else printf("Case #%d: %d\n",tt,nwd-lol);
	}
}
