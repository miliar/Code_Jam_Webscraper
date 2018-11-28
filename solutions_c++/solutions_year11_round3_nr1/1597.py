#include<cstring>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;

#define N 201

int num,R,C;
char s[N][N];

void init()
{
	num = 0;
	scanf("%d%d",&R ,&C);
	for (int i = 0; i < R; i++)
	{
		scanf("%s",s[i]);
		for (int j = 0; j < C; j++)
		 if (s[i][j] == '#') num++;
	}
}

bool ll(int i,int j)
{
	if (i >= R || j >= C || s[i][j] != '#') return false;
	return true;
}

bool solve()
{
	if (num % 4 != 0) return false;
	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++)
			if (s[i][j] == '#')
			{
				if (!ll(i,j+1) || !ll(i+1,j) || !ll(i+1,j+1)) return false;
				s[i][j] = '/'; s[i][j+1] = '\\';
				s[i+1][j] = '\\'; s[i+1][j+1] ='/';
			}
	return true;
}

int main() 
{
//	freopen("A.in","r",stdin);
//	freopen("A.ans","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i = 1; i <= T; i++)
	{
		init();
		printf("Case #%d:\n",i);
		if (!solve()) {
			printf("Impossible\n");
		} else 
		{
			for (int j = 0; j < R; j++)
			{
				for (int k = 0; k < C; k++)
					printf("%c",s[j][k]);
				printf("\n");
			}
		}
	}
}
