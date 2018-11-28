#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
using namespace std;

int gcd(int a,int b){
	if(a<b){
		a=a^b;
		b=a^b;
		a=a^b;
	}
	int t;
	while(b>0){
		t=a%b;
		a=b;
		b=t;
	}
	return a;
}

int lcm(int a,int b){
	return a*b/gcd(a,b);
}

int main(){
	int T;
	int cas=1;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C1.txt","w",stdout);

	scanf("%d",&T);
	while(T--){
		int n,l,h;
		int i,j,t[105];
		int ans=1;
		scanf("%d %d %d",&n,&l,&h);
		int mm=1000000000;
		for(i=0;i<n;++i){
			scanf("%d",&t[i]);
		}

		for(i=l;i<=h;++i){
			for(j=0;j<n;++j){
				if(t[j]%i!=0 && i%t[j]!=0)
					break;
			}
			if(j==n)
				break;
		}
		if(i>h)
			printf("Case #%d: NO\n",cas++);
		else
			printf("Case #%d: %d\n",cas++,i);
	}
	return 0;
}