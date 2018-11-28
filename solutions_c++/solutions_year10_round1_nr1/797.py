#include <cstdio>
#include <memory.h>
char M[55][55];
char N[55][55];
int row;
void rotate(int r,int c)
{
	for(int i = 0; i < r; ++ i)
		for(int j = 0;j < c; ++ j)
		{
			N[j][row - i - 1] = M[i][j];
		}
		memcpy(M,N,sizeof M);
}
int dir[][2] = {{1,0},{1,1},{1,-1},{0,1},{0,-1}};
int K;
bool check2(int beg,int end,char c)
{
	for(int i = 0; i < 5; ++ i)
	{
		bool tag = true;
		for(int z = 0; z < K; ++ z)
		{
			if(beg + z * dir[i][0] >= row || beg + z * dir[i][0] < 0) {tag = false;break;}
			if(end + z * dir[i][1] >= row || end + z * dir[i][1] < 0) {tag = false;break;}
			if(M[beg + z * dir[i][0]][end + z * dir[i][1]] != c) tag = false;
		}
		if(tag) return true;
	}
	return false;
}
int ZZ = 0,PP = 0;
void check(int row,int col)
{
	int i,j;
	for(i = 0; i < row;++ i)
		for(j = 0; j < row ; ++ j)
		{
			if(ZZ == 0 && check2(i,j,'R')) ZZ = 1;
			if(PP == 0 && check2(i,j,'B')) PP = 1;

		}
}
void Grav(int row,int col)
{
	for(int i = 0; i < col; ++ i)
	{
		int ret = row - 1;
		int j;
		for(j = row - 1; j >= 0; -- j)
		{
			if(M[j][i] != '.') {
				M[ret][i]=M[j][i];
			    ret --;
			}
		}
		for(j = 0; j <= ret; ++ j) M[j][i] = '.';
	}
}
int main()
{
	int T;
	int j;
	freopen("A-large.in","r",stdin);
	freopen("output1.txt","w",stdout);
	scanf("%d",&T);
	for(int i = 1;i <= T; ++ i)
	{
		scanf("%d%d",&row,&K);
		for(j = 0; j < row; ++ j)
		{
			scanf("%s",M[j]);
			//printf("%s\n",M[j]);
		}
		rotate(row,row);
	
		Grav(row,row);
	
		ZZ = PP = 0;
		check(row,row);
		printf("Case #%d: ",i);
		if(ZZ == 0 && PP == 0) puts("Neither");
		else if(ZZ == 1 && PP == 1) puts("Both");
		else if(ZZ == 1 && PP == 0) puts("Red");
		else if (ZZ == 0 && PP == 1) puts("Blue");
	}
	return 0;
}