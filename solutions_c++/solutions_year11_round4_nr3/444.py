#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
const int MaxN=1000000+50;

using namespace std;
long long N,a[MaxN],p[MaxN],Ans,T;
void preprocess(){
	p[0]=0;
	for (int i=1;i<MaxN;i++) a[i]=i;
	for (long long i=2;i<MaxN;i++){
		if (a[i]==i) p[++p[0]]=i;
		for (long long j=1;j<=p[0];j++){
			if (p[j]*i>=MaxN) break;
			a[p[j]*i]=p[j];
			if (a[i]==p[j]) break;
		}
	}
}
void work(){
	Ans=1;
	for (int i=1;i<=p[0];i++){
		if (p[i]*p[i]>N) break;
		long long add=0,now=p[i];
		while (now*p[i]<=N){
			add++;
			now*=p[i];
		}
		Ans+=add;
	}
	if (N==1) Ans=0;
}
int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	preprocess();
	cin >> T;
	for (int t=1;t<=T;t++){
		printf("Case #%d: ", t);
		scanf("%d", &N);
		Ans=0;
		work();
		cout << Ans << endl;
	}
	return 0;
}
