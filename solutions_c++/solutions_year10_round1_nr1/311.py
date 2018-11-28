#include <cmath>
#include <algorithm>
#include <sstream>
#include <queue>
#include<iostream>
#define FALSE 0
#define TRUE 1
using namespace std;
typedef long long ll;
typedef pair<int,int> ipair;
#define SIZEARRAY(x) (sizeof(x)/sizeof(x[0]))

const int maxnum = 105;
char mm[maxnum][maxnum];

int T,K;
void rotate()
{
	char nmm[maxnum][maxnum];
	memcpy(nmm,mm,sizeof(mm));
	for (int i = 1;i<=T;i++)
	{
		for (int j = 1;j<=T;j++)
		{
			nmm[j][T-i+1] = mm[i][j];
		}
	}
	memcpy(mm,nmm,sizeof(nmm));
}

void fix()
{
	int nowNum[maxnum];
	for (int i = 1;i<=T;i++)
	{
		nowNum[i] = T;
	}
	for (int i = 1;i<=T;i++)
	{
		for (int j = T;j>=1;j--)
		{
			if (mm[j][i] != '.')
			{
				if ((nowNum[i] != j))
				{
					mm[nowNum[i]][i] = mm[j][i];
					mm[j][i] = '.';
				}
				nowNum[i]--;
			}
		}
	}
}


int memo[maxnum][maxnum][4];
int main()
{

	freopen("F:\\code\\topcoder\\A-large (1).in","r",stdin);
	freopen("F:\\code\\topcoder\\compete\\compete\\test2.out","w",stdout);
	int caseNum;
	cin>>caseNum;
	int caseIndex = 1;
	while (caseIndex<=caseNum)
	{
		cin>>T>>K;
		for (int i = 0;i<=T+1;i++)
		{
			for (int j = 0;j<=T+1;j++)
			{
				mm[i][j] = '.';
			}
		}
		char tempC;
		tempC = getchar();
		for (int i = 1;i<=T;i++)
		{
			for (int j = 1;j<=T;j++)
			{
				tempC = getchar();
				mm[i][j] = tempC;
			}
			getchar();
		}
		rotate();
		fix();
		int x1,y1,x2,y2,x3,y3,x4,y4;
		memset(memo,0,sizeof(memo));
		for (int i = 1;i<=T;i++)
		{
			for (int j = 1;j<=T;j++)
			{
				x1 = i-1;
				y1 = j;
				x2 = i;
				y2 = j-1;
				x3 = i-1;
				y3 = j-1;
				x4 = i-1;
				y4 = j+1;
				if (mm[i][j] != '.')
				{
					if (mm[x1][y1] == mm[i][j])
					{
						memo[i][j][0] = memo[x1][y1][0]+1;
					}
					else
					{
						memo[i][j][0] = 1;
					}
					if (mm[x2][y2] == mm[i][j])
					{
						memo[i][j][1] = memo[x2][y2][1]+1;
					}
					else
					{
						memo[i][j][1] = 1;
					}
					if (mm[x4][y4] == mm[i][j])
					{
						memo[i][j][3] = memo[x4][y4][3]+1;
					}
					else
					{
						memo[i][j][3] = 1;
					}
					if (mm[x3][y3] == mm[i][j])
					{
						memo[i][j][2] = memo[x3][y3][2]+1;
					}
					else
					{
						memo[i][j][2] = 1;
					}
				}
			}
		}
		int res = 0;
		for (int i = 1;i<=T;i++)
		{
			for (int j = 1;j<=T;j++)
			{
				for (int s = 0;s<4;s++)
				{
					if (memo[i][j][s] >= K)
					{
						if (mm[i][j] == 'R')
						{
							res |= 1;
						}
						else
						{
							res |=2;
						}
					}
				}
			}
		}
		cout << "Case #"<<caseIndex<<": ";
		if (res == 0)
		{
			cout << "Neither"<<endl;
		}
		else if (res == 1)
		{
			cout << "Red"<<endl;
		}
		else if (res == 2)
		{
			cout << "Blue"<<endl;
		}
		else if (res == 3)
		{
			cout << "Both"<<endl;
		}
		caseIndex++;
	}
}