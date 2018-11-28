#include <stdio.h>
#include <memory.h>
#include <math.h>


int n;
int dat[152][152];

int isele(int r,int c){
	int i,j;
	for(i=0;i<2*n-1;i++){
		for(j=0;j<2*n-1;j++){
			int A,B,C,D;
			if(r-i < 0) {
				A = B = -1;
			}else {
				if(c-j < 0) {
					A = -1;
				}else {
					A = dat[r-i][c-j];
				}
				if(c+j >= 2*n-1) {
					B = -1;
				}else{
					B = dat[r-i][c+j];
				}
			}
			if(r+i >= 2*n-1) {
				C=D=-1;
			}else {
				if(c-j < 0) {
					C = -1;
				}else {
					C = dat[r+i][c-j];
				}
				if(c+j >= 2*n-1) {
					D = -1;
				}else {
					D = dat[r+i][c+j];
				}
			}
			if(A == -1 || B == -1 || A == B){
				if(B == -1 || D == -1 || D == B){
					if(C == -1 || D == -1 || D == C){
						if(C == -1 || A == -1 || A == C){
							continue;
						}
					}
				}
			}
			return 0;
		}
	}
	return 1;
}

int main(){
	int T;
	int testcase = 0;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for(testcase = 0; testcase < T; testcase ++){
		int i,j;
		memset(dat,-1,sizeof(dat));
		printf("Case #%d: ",testcase+1);
		scanf("%d",&n);
		for(i=0;i<n;i++){
			for(j=0;j<i+1;j++){
				scanf("%d",&dat[i][j*2+n-i-1]);
			}
		}
		for(i=n;i<2*n-1;i++){
			for(j=0;j<2*n-i-1;j++){
				scanf("%d",&dat[i][j*2+i-n+1]);
			}
		}
		long long ans = 9*n*n;
		int cr = n-1, cc = n-1;
		for(i=0;i<2*n-1;i++) {
			for(j=0;j<2*n-1;j++){
				if(isele(i,j)){
					if(ans > abs(n-1-i)+abs(n-1-j)+n ){
						ans = abs(n-1-i)+abs(n-1-j)+n ;
					}
				}
			}
		}
		printf("%lld\n",ans*ans - n*n);
	}
	return 0;
}
