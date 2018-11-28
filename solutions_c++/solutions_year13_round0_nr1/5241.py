#include <cstdio>
#include <algorithm>

int t;
char arr[4][4];
bool X, O, x, o, dot;

void solve(int cas)	{
	X = O = dot = false;
	for(int i=0;i<4;i++) scanf("%s",arr[i]);
	x = o = true;
	for(int i=0;i<4;i++) {
		x &= (arr[i][i] == 'X' || arr[i][i] == 'T');
		o &= (arr[i][i] == 'O' || arr[i][i] == 'T');
	}
	X |= x; O |= o;
	x = o = true;
	for(int i=0;i<4;i++) {
		x &= (arr[i][3-i] == 'X' || arr[i][3-i] == 'T');
		o &= (arr[i][3-i] == 'O' || arr[i][3-i] == 'T');
	}
	X |= x; O |= o;
	for(int i=0;i<4;i++)	{
		x = o = true;
		for(int j=0;j<4;j++)	{
			dot |= (arr[i][j] == '.');
			x &= (arr[i][j] == 'X' || arr[i][j] == 'T');
			o &= (arr[i][j] == 'O' || arr[i][j] == 'T');
		}
		X |= x; O |= o;
	}
	for(int j=0;j<4;j++)	{
		x = o = true;
		for(int i=0;i<4;i++)	{
			x &= (arr[i][j] == 'X' || arr[i][j] == 'T');
			o &= (arr[i][j] == 'O' || arr[i][j] == 'T');
		}
		X |= x; O |= o;
	}
	printf("Case #%d: ", cas);
	if(X) printf("X won\n");
	if(O) printf("O won\n");
	if(!X && !O) if(dot) printf("Game has not completed\n");
	else printf("Draw\n");
}

int main()	{
	scanf("%d",&t);
	for(int i=1;i<=t;i++)	{
		solve(i);
	}
}
