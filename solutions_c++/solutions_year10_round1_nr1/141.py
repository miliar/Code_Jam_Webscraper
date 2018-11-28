#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char field[2][50][51];
int n, K;

bool isExist(char tar);

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int caseN=1;caseN<=t;caseN++)
	{
		scanf("%d %d", &n, &K);
		for(int i=0;i<n;i++) scanf("%s", field[0][i]);
		
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++) field[1][j][n-i-1]=field[0][i][j];
			field[1][i][n]=0;
		}

		for(int i=n-1;i>=0;i--)
		{
			for(int j=0;j<n;j++)
			{
				int next=i+1;
				while(next<n && field[1][next][j]=='.') next++;
				next--;
				swap(field[1][next][j], field[1][i][j]);
			}
		}

		bool isAble[2]={false, false};
		if(isExist('R')) isAble[0]=true;
		if(isExist('B')) isAble[1]=true;

		printf("Case #%d: ", caseN);
		if(isAble[0] && isAble[1]) printf("Both\n");
		else if (isAble[0]) printf("Red\n");
		else if (isAble[1]) printf("Blue\n");
		else printf("Neither\n");
	}

	return 0;
}

bool isExist(char tar)
{
	int mov[4][2]={{0, 1}, {1, 0}, {-1, 1}, {1, 1}};
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			for(int q=0;q<4;q++)
			{
				int ny=i, nx=j;
				bool isAble=true;
				for(int k=0;k<K;k++)
				{					
					if(ny>=n || ny<0 || nx>=n || nx<0) { isAble=false; break; }
					if(field[1][ny][nx]!=tar) { isAble=false; break; }
					ny+=mov[q][0], nx+=mov[q][1];
				}
				if(isAble) 
				{
					return true;
				}
			}
		}
	}

	return false;
}
