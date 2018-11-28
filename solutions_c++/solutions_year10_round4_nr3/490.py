#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char b[2][210][210];
int R;

int chg(int f,int t){
	int i,j,x;
	bool ret=false;
	for (i=1;i<210;i++) for (j=1;j<210;j++){
		x=b[f][i-1][j] + b[f][i][j-1];
		if (x==0) b[t][i][j]=0;
		else if (x==2){
			b[t][i][j]=1;
			ret = true;
		}else{
			b[t][i][j]=b[f][i][j];
			if (b[t][i][j]) ret=true;
		}
	}
	return ret;
}

void sol(int cas){
	int i,j,X1,X2,Y1,Y2;
	memset(b,0,sizeof(b));
	scanf("%d",&R);
	while (R--){
		scanf("%d%d%d%d",&X1,&Y1,&X2,&Y2);
		for (i=X1;i<=X2;i++) for (j=Y1;j<=Y2;j++)
			b[0][i][j]=1;
	}
	int rd=0;
	while (chg(rd&1,1-(rd&1))) rd++;
	printf("Case #%d: %d\n",cas, rd+1);
}

int main(){
	int t,cas;
	scanf("%d",&t);
	for (cas=1;cas<=t;cas++)
		sol(cas);
	return 0;
}

