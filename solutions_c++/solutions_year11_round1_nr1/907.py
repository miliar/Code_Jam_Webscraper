#include<cstdio>
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<queue>

using namespace std;

#define rep(i,n) for(int i=0;i<n;i++)
#define reps(i,n) for(int i=1;i<=n;i++)

int gcd(int a,int b){
	if(a<b)swap(a,b);
	if(a==0 || b==0)return 100;
	while(1){
		if(a%b==0)break;
		int bin=b;
		b = a%b;
		a = bin;
	}
	return b;
}
int main(){
	int t;
	scanf("%d",&t);
	reps(p,t){
		__int64 a;
		int b,c;
		scanf("%I64d%d%d",&a,&b,&c);
		
		int d = gcd(b,100);
		int e = 100/d;
		
		printf("Case #%d: ",p);
		if(e>a){
			printf("Broken\n");
			continue;
		}
		
		if(b!=100 && c==100){
			printf("Broken\n");
			continue;
		}
		if(b!=0 && c==0){
			printf("Broken\n");
			continue;
		}
		
		printf("Possible\n");
	}
}