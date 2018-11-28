#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;


int T;

char a[4][4];

int x,y;

int main(void){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d\n",&T);
	int cc=0;
	while (T--){
		for (int i=0;i<4;i++){
			for (int j=0;j<4;j++){
				scanf("%c",&a[i][j]);
				if (a[i][j]=='T'){
					x=i,y=j;
				}
			}
			scanf("\n");
		}

		int res=0;

		a[x][y]='O';
		for (int i=0;i<4;i++) if ((a[i][0]==a[i][1]) && (a[i][1]==a[i][2]) && (a[i][1]==a[i][3]) && (a[i][1]=='O')) res=1;
		for (int i=0;i<4;i++) if ((a[0][i]==a[1][i]) && (a[1][i]==a[2][i]) && (a[1][i]==a[3][i]) && (a[1][i]=='O')) res=1;
		int kol=0;
		for (int i=0;i<4;i++) if (a[i][i]=='O') kol++;
		if (kol==4) res=1;
		kol=0;
		for (int i=0;i<4;i++) if (a[3-i][i]=='O') kol++;
		if (kol==4) res=1;


		a[x][y]='X';
		for (int i=0;i<4;i++) if ((a[i][0]==a[i][1]) && (a[i][1]==a[i][2]) && (a[i][1]==a[i][3]) && (a[i][1]=='X')) res=2;
		for (int i=0;i<4;i++) if ((a[0][i]==a[1][i]) && (a[1][i]==a[2][i]) && (a[1][i]==a[3][i]) && (a[1][i]=='X')) res=2;
		kol=0;
		for (int i=0;i<4;i++) if (a[i][i]=='X') kol++;
		if (kol==4) res=2;
		kol=0;
		for (int i=0;i<4;i++) if (a[3-i][i]=='X') kol++;
		if (kol==4) res=2;

		if (res==0){
			res=4;
			for (int i=0;i<4;i++) for (int j=0;j<4;j++) if (a[i][j]=='.') res=3;
		}
		cc++;
		printf("Case #%d:",cc);

		if (res==1) printf(" O won\n");else
		if (res==2) printf(" X won\n");else
		if (res==3) printf(" Game has not completed\n");else
		if (res==4) printf(" Draw\n");
		scanf("\n");
	}


}