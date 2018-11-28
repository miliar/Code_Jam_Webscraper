#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main(){
	long long int i,j,k,l,m,n,t;
	long long int A[100000];
	scanf("%lld",&t);
	l=0;
	while(l++<t){
		printf("Case #%lld: ",l);
		scanf("%lld",&n);
		i=0;
		while(i<n) scanf("%lld",&A[i++]);
		sort(A,A+n);
		for(i=0;i<n;i++){
			k=0;
			m=0;
			int sum=0;
			for(j=0;j<n;j++){
				if(i!=j){
					k^=A[j];
					sum+=A[j];
				}
			}
			if(k==A[i]){
				printf("%lld\n",sum);
				m=1;
				break;
			}
		}
		if(m==0) printf("NO\n");
	}
	return 0;
}

