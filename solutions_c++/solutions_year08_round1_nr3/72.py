#include <cstdio>
#include <cstring>
using namespace std;

struct matrix {
	int a[5][5];
};

int n;
matrix base;

matrix operator * (matrix a,matrix b) {
	matrix tmp;
	memset(tmp.a,0,sizeof(tmp.a));
	for (int i=1;i<=2;i++)
		for (int j=1;j<=2;j++)
			for (int k=1;k<=2;k++)
				tmp.a[i][j]=(tmp.a[i][j]+a.a[i][k]*b.a[k][j])%1000;
	return tmp;
}

matrix hyper(int k) {
	if (k==1) return base;
	matrix tmp=hyper(k/2);
	tmp=tmp*tmp;
	if (k%2==1) tmp=tmp*base;
	return tmp;
}

int main() {
	int cases,kase=0;
	for (scanf("%d",&cases);cases>0;cases--) {
		scanf("%d",&n);
		printf("Case #%d: ",++kase);
		if (n==2) {
			printf("027\n");
			continue;
		}
		base.a[1][1]=0;base.a[1][2]=-4;
		base.a[2][1]=1;base.a[2][2]=6;
		matrix ans=hyper(n-2);
		int ot=28*ans.a[2][2]+6*ans.a[1][2];
		ot=ot-1;
		while (ot<0) ot=ot+1000;
		ot=ot%1000;
		if (ot<100) printf("0");
		if (ot<10) printf("0");
		printf("%d\n",ot);
	}
}
