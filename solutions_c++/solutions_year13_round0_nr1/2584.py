#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<functional>
#include<algorithm>

using namespace std;

//#define _INFILE		"A.in"
//#define _OUTFILE	"A.out"

//#define _INFILE		"A-small-attempt0.in"
//#define _OUTFILE	"A-small.out"

#define _INFILE		"A-large.in"
#define _OUTFILE	"A-large.out"
typedef long long lint;

bool judge(char in[10][10], char c)
{
	int i;
	for(i=0; i<4; i++)
	{
		if (in[i][i] != c && in[i][i] != 'T')
		{
			break;
		}
	}
	if (i == 4) return true;

	for(i=0; i<4; i++)
	{
		if (in[i][3-i] != c && in[i][3-i] != 'T')
		{
			break;
		}
	}
	if (i == 4) return true;

	for(i=0; i<4; i++)
	{
		int j;
		for(j=0; j<4; j++)
		{
			if (in[i][j] != c && in[i][j] != 'T')
			{
				break;
			}
		}
		if (j == 4) return true;
		for(j=0; j<4; j++)
		{
			if (in[j][i] != c && in[j][i] != 'T')
			{
				break;
			}
		}
		if (j == 4) return true;


	}

	return false;
}

void solve()
{
	char in[10][10];
	bool isCompleted = true;
	for(int i=0; i<4; i++)
	{
		scanf("%s", in[i]);
		for(int j=0; j<4; j++)
			if (in[i][j] == '.')
				isCompleted = false;
	}

	if (judge(in, 'X'))
		printf("X won\n");
	else if (judge(in, 'O'))
		printf("O won\n");
	else if (isCompleted)
		printf("Draw\n");
	else printf("Game has not completed\n");
}

int main(void)
{
	int T;
	freopen(_INFILE, "r", stdin);
	freopen(_OUTFILE, "w", stdout);

	scanf("%d",&T);

	for(int i=0; i<T; i++)
	{
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}

