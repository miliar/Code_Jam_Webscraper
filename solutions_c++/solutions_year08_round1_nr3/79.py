#include <stdio.h>
#include <string.h>

class Mat{
public:
	int v[2][2];
	Mat(){
		memset(v,0,sizeof(v));
	}
	friend Mat operator * (const Mat&A,const Mat&B){
		int i,j,k;
		Mat C;
		for (k=0;k<2;k++) for (i=0;i<2;i++) for (j=0;j<2;j++){
			C.v[i][j]+=A.v[i][k]*B.v[k][j];
			C.v[i][j]%=1000;
		}
		return C;
	}
};

void solve(int cas){
	int n;
	Mat A,B;
	A.v[0][0]=6;
	A.v[0][1]=-4;
	A.v[1][0]=1;
	B.v[0][0]=B.v[1][1]=1;
	scanf("%d",&n);
	while (n){
		if (n&1) B=B*A;
		A=A*A;
		n>>=1;
	}
//	printf("%d %d\n%d %d\n",B.v[0][0],B.v[0][1],B.v[1][0],B.v[1][1]);
	n=B.v[1][0]*6+B.v[1][1]*2-1;
	n%=1000;
	if (n<0) n+=1000;
	printf("Case #%d: %03d\n",cas,n);
}

int main(){
	int t,cas;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	for (cas=1;cas<=t;cas++)
		solve(cas);
	return 0;
}

