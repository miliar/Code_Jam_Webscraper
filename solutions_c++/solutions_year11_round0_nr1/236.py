#include<stdio.h>
#include<algorithm>

using namespace std;

int ntest;
int n, x, pos;
char who[5];
int p[2];
int t[2];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d",&ntest);
	for(int test=1;test<=ntest;test++)
	{
		scanf("%d",&n);
		t[0] = t[1] = 0;
		p[0] = p[1] = 1;
		for(int i=0;i<n;i++)
		{
			scanf("%s%d",&who,&pos);
			if(*who == 'O') x = 0;
			else x = 1;

			int delta = abs(pos - p[x]);
			t[x] += delta + 1; p[x] = pos;
			if(t[x] <= t[x^1]) t[x] = t[x^1] + 1;
		}

		printf("Case #%d: %d\n", test, max(t[0], t[1]));
	}

	return 0;
}
