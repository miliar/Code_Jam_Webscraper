#include<stdio.h>

char s[6][6];

bool check(char C)
{
	int i,j;
	for(i=1;i<=4;i++){
		for(j=1;j<=4;j++){
			if(s[i][j]!=C)break;
		}
		if(j==5){
			printf("%c won\n",C);
			return true;
		}
	}
	for(i=1;i<=4;i++){
		for(j=1;j<=4;j++){
			if(s[j][i]!=C)break;
		}
		if(j==5){
			printf("%c won\n",C);
			return true;
		}
	}
	for(j=1;j<=4;j++){
		if(s[j][j]!=C)break;
	}
	if(j==5){
		printf("%c won\n",C);
		return true;
	}
	for(j=1;j<=4;j++){
		if(s[j][5-j]!=C)break;
	}
	if(j==5){
		printf("%c won\n",C);
		return true;
	}
	return false;
}

void solve()
{
	int i,j;
	for(i=1;i<=4;i++){
		for(j=1;j<=4;j++)if(s[i][j]=='T')break;
		if(j!=5)break;
	}
	s[i][j]='X';
	if(check('X'))return;
	s[i][j]='O';
	if(check('O'))return;
	for(i=1;i<=4;i++){
		for(j=1;j<=4;j++){
			if(s[i][j]=='.'){
				printf("Game has not completed\n");
				return;
			}
		}
	}
	printf("Draw\n");
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		printf("Case #%d: ",t);
		for(int i=1;i<=4;i++)scanf("%s",s[i]+1);
		solve();
	}
}