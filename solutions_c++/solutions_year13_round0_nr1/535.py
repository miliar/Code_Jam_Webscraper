#include<cstdio>

int N;
char in[5][5];

int valid[10][4] = 
{
	{0, 1, 2, 3},
	{4, 5, 6, 7},
	{8, 9, 10, 11},
	{12, 13, 14, 15},
	{0, 4, 8, 12},
	{1, 5, 9, 13},
	{2, 6, 10, 14},
	{3, 7, 11, 15},
	{0, 5, 10, 15},
	{3, 6, 9, 12}
};

int main()
{
	scanf("%d", &N);
	for(int t=0;t++<N;){
		for(int i=0;i<4;i++) scanf("%s", in[i]);

		int ret = -1;
		for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(in[i][j]=='.') ret = -2;

		for(int i=0;i<10;i++){
			bool fo=true, fx=true;
			for(int j=0;j<4;j++){
				char v = in[valid[i][j]/4][valid[i][j]%4];
				if(v=='.') fo = fx = false;
				if(v=='X') fo = false;
				if(v=='O') fx = false;
			}
			if(fo) ret = 1;
			if(fx) ret = 2;
		}
		printf("Case #%d: ", t);
		switch(ret){
		case -1: puts("Draw"); break;
		case -2: puts("Game has not completed"); break;
		case 1: puts("O won"); break;
		case 2: puts("X won"); break;
		}
	}
	return 0;
}
