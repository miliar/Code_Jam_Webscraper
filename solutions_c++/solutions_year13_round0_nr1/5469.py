#include <cstdio>

using namespace std;



int rob(int n)
{
	int x,y,kolo=0;
	char c;
	int pole[4][4];
	for(int i=0;i<4;i++) for(int j=0;j<4;j++){
		scanf(" %c ",&c);
		if(c=='.'){ pole[i][j]=-1; kolo++;}
		if(c=='O') pole[i][j]=0;
		if(c=='X') pole[i][j]=1;
		if(c=='T') pole[i][j]=2;
	}
	/*for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			printf("%d",pole[i][j]);
		} printf("\n");
	}*/

	for(int i=0;i<4;i++){
		for(int j=0;j<=4;j++){
			if(j==4){
				printf("Case #%d: O won\n",n+1);
				return 0;
			}
			if(pole[i][j]==-1 || pole[i][j]==1) break;
		}
	}
	for(int i=0;i<4;i++){
		for(int j=0;j<=4;j++){
			if(j==4){
				printf("Case #%d: O won\n",n+1);
				return 0;
			}
			if(pole[j][i]==-1 || pole[i][j]==1) break;
		}
	}
	for(int i=0;i<=4;i++){
		if(i==4){
				printf("Case #%d: O won\n",n+1);
				return 0;
			}
		if(pole[i][i]==-1 || pole[i][i]==1) break;
	}
	for(int i=0;i<=4;i++){
		if(i==4){
				printf("Case #%d: O won\n",n+1);
				return 0;
			}
		if(pole[i][3-i]==-1 || pole[i][3-i]==1) break;
	}

	//
		for(int i=0;i<4;i++){
		for(int j=0;j<=4;j++){
			if(j==4){
				printf("Case #%d: X won\n",n+1);
				return 0;
			}
			if(pole[i][j]==-1 || pole[i][j]==0) break;
		}
	}
	for(int i=0;i<4;i++){
		for(int j=0;j<=4;j++){
			if(j==4){
				printf("Case #%d: X won\n",n+1);
				return 0;
			}
			if(pole[j][i]==-1 || pole[i][j]==0) break;
		}
	}
	for(int i=0;i<=4;i++){
		if(i==4){
				printf("Case #%d: X won\n",n+1);
				return 0;
			}
		if(pole[i][i]==-1 || pole[i][i]==0) break;
	}
	for(int i=0;i<=4;i++){
		if(i==4){
				printf("Case #%d: X won\n",n+1);
				return 0;
			}
		if(pole[i][3-i]==-1 || pole[i][3-i]==0) break;
	}

	if(kolo==0) printf("Case #%d: Draw\n",n+1);
	else printf("Case #%d: Game has not completed\n",n+1);
	return 0;
}

int main()
{
	int n;
	scanf("%d ",&n);
	for(int i=0;i<n;i++) rob(i);
	return 0;
}

