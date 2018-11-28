#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;

int A[1010],n;

/*int solve(int i,int s1,int s2,bool us) {
	if(i==n) {
		if(s1==s2 && us)
			return 0;
		return -(1<<30);
	}
	return max(A[i]+solve(i+1,s1^A[i],s2,us),solve(i+1,s1,s2^A[i],1));
}*/

int solve() {
	int t=0,rpta=0,min=A[0];
	for(int i=0;i<n;i++) {
		t^=A[i];
		rpta+=A[i];
		if(A[i]<min)
			min=A[i];
	}
	if(t)
		return -1;
	return rpta-min;
}

int main() {
	int t;
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++) {
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%d",&A[i]);
		printf("Case #%d: ",caso);
/*		int rpta=solve(0,0,0,0);*/
		int rpta=solve();
		if(rpta>0)
			printf("%d\n",rpta);
		else
			printf("NO\n");
	}
	return 0;
}
