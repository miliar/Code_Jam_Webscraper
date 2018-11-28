#include <cstdio>
#include <cstdlib>
#include <cctype>
int table[4][4];
int getachar(){
	int x;
	while (isspace(x = getchar()));
	return x;
}
char ToPlayer(int x){
	return x==2?'X':'O';
}
void work(int c){
	bool nofull = false;
	for (int i = 0 ; i < 4; i ++)
		for (int j = 0 ; j < 4 ; j ++)
		{
			int y = getachar();
			if (y=='.') table[i][j] = 0,nofull = true;
			if (y=='X') table[i][j] = 2;
			if (y=='O') table[i][j] = 4;
			if (y=='T') table[i][j] = 6;
		}
		for (int i = 0 ; i < 4 ; i++) 
		{
			int x = table[i][0];
			if (!(x&6)) continue;
			for (int j = 1 ; j < 4 ; j++)
				x&=table[i][j];
			if (x!=0 && x!=6){
				printf("Case #%d: %c won\n",c,ToPlayer(x));
				return ;
			}
		}
		for (int j = 0 ; j < 4 ; j++)
		{
			int x = table[0][j];
			if (!(x&6)) continue;
			for (int i = 1 ; i < 4 ; i++)
				x&=table[i][j];
			if (x!=0 && x!=6){
				printf("Case #%d: %c won\n",c,ToPlayer(x));
				return ;
			}
		}
		int q = table[0][0];
		for (int i = 1 ; i < 4 ; i++){
			q&=table[i][i];
		}
		if (q!=0&&q!=6)
		{
			printf("Case #%d: %c won\n",c,ToPlayer(q));
			return ;
		}
		q = table[0][3];
		for (int i = 1 ; i < 4 ; i++){
			q&=table[i][3-i];
		}
		if (q!=0&&q!=6)
		{
			printf("Case #%d: %c won\n",c,ToPlayer(q));
			return ;
		}
		if (nofull){
			printf("Case #%d: Game has not completed\n",c);
		}
		else
		{
			printf("Case #%d: Draw\n",c);
		}
}
int main(){
	int T;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for (int i = 1 ; i <= T ; i ++) work(i);
}