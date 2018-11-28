#include <iostream>
#include <vector>
using namespace std;

int res[30][2];

void init()
{
	int i, j;
	res[0][0] = res[0][1] = 0;
	res[1][0] = res[1][1] = 1;
	res[2][0] = 1;  res[2][1] = 2;
	
	for (i=3; i<=30; i++)
	{
		if(i%3==0)
		{
			res[i][0] = i/3;
			res[i][1] = i/3+1;
		}
		else if(i%3==1)
		{
			res[i][0] = i/3+1;
			res[i][1] = i/3+1;
		}
		else
		{
			res[i][0] = i/3+1;
			res[i][1] = i/3+2;
		}
	}
}

int main()
{
//  freopen("B-small-attempt0.in", "r", stdin);
// 	freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int i, j, cnt, icase, nCase;

	scanf("%d", &nCase);
	int N, S, P;
	int num[105];
	init();
	for (icase=1; icase<=nCase; icase++)
	{
		scanf("%d%d%d", &N, &S, &P);
		cnt = j =0;
		for (i=0; i<N; i++)
		{
			scanf("%d", &num[i]);
			if(res[num[i]][0]>=P)
			{
				j++;
			}
			else if(res[num[i]][1]>=P)
			{
				cnt++;
			}
		}
		if(cnt>S) cnt = S;
		printf("Case #%d: %d\n", icase, j+cnt);
	}

	return 0;
}
