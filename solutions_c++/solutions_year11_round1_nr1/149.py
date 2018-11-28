#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;
int Ans=0,T;
int gcd(int a,int b){
	return b ? gcd(b,a%b) : a;
}
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;
	scanf("%d", &T);
	for (int t=1;t<=T;t++){
		int p1,p2,N;
		scanf("%d %d %d", &N, &p1, &p2);
		Ans=0;
		if (p1==p2 && p1==100) Ans=1;else
		if (p1==p2 && p1==0) Ans=1;else
		if (p2!=100 && p2!=0){
			for (int i=1;i<=min(100,N);i++)
			if ((i*p1)%100==0) Ans=1;
		}
		if (Ans) printf("Case #%d: Possible\n", t);else
		printf("Case #%d: Broken\n", t);
	}
	return 0;
}
