#include <iostream>
#include <cstdio>
using namespace std;
#define maxt (101)
int t,s,p;
int ti[maxt];
int dper[maxt][maxt];
void calc(){
	scanf("%d%d%d",&t,&s,&p);
	for(int i=0;i<t;i++)
		scanf("%d",&ti[i]);
	for(int i=0;i<=s;i++)
		dper[0][i]=0;
	for(int i=0;i<t;i++){
		int base = ti[i]/3;
		int r    = ti[i]%3;
		int max_xsu = base + (r!=0);
		int add = (max_xsu>=p);
		for(int j=0;j<=s;j++){
			//printf("%ld ",dper[i][j]);
			dper[i+1][j]=dper[i][j]+add;
		}
		//printf("\n");
		if(ti[i]<2 || ti[i]>28)
			continue;
		int max_su = base + 1 + (r==2);
		add = (max_su>=p);
		for(int j=0;j<s;j++)
			if(dper[i][j]+add>dper[i+1][j+1])
				dper[i+1][j+1]=dper[i][j]+add;
	}
	printf("%d\n",dper[t][s]);
}
int main(){
	int N;
	scanf("%d",&N);
	for(int I=1;I<=N;I++){
		printf("Case #%d: ",I);
		calc();
	}
	return 0;
}
