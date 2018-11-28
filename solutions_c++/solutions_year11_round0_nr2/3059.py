#include<iostream>
using namespace std;
int tt, ii;
int u[270]={0};
char a[270][4]={{0}};
char ans[300] = {0};
void clean()
{
	for(int i = 0; i<270; i++)
	{
		u[i] = 0;
		for(int j = 0; j<4; j++)
		a[i][j] = 0;
		ans[i] = 0;
	}
}
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d\n", &tt);
	int i, j, l, c, n, d;
	char s1[10], s2;
	for(ii = 1; ii<=tt; ii++)
	{
		scanf("%d", &c);
		for(i = 1; i<=c; i++)
		{
			scanf("%s", s1);
			a[s1[0]][1] = s1[1];
			a[s1[0]][2] = s1[2];
			a[s1[1]][1] = s1[0];
			a[s1[1]][2] = s1[2];
		}

		scanf("%d", &d);
		for(i = 1; i<=d; i++)
		{
			scanf("%s", s1);
			a[s1[0]][3] = s1[1];
			a[s1[1]][3] = s1[0];
		}
		scanf("%d ", &n);
		l = 0;
		for(i = 1; i<=n; i++)
		{
			scanf("%c", &s2);
			if(!(s2 == 'Q' || s2 == 'W' || s2 == 'E' || s2 == 'R' || s2 == 'A' || s2 == 'S' || s2 == 'D'|| s2 == 'F'))
			{
				l++;
				ans[l] = s2;
			}
			else
			{
				
				if(a[s2][1]!=0 && ans[l] == a[s2][1])
				{
					u[ans[l]]--;
					ans[l] = a[s2][2];
				}
				else if(u[ a[s2][3] ]>0)
				{
					l = 0;
					for(j = 0; j<270; j++)
						u[j] = 0;
				}
				else
				{
					l++;
					ans[l] = s2;
					u[ans[l]]++;
				}
			}
		}
		printf("Case #%d: [", ii);
		for(i = 1; i<l; i++)
			printf("%c, ", ans[i]);
		if(l>=1)
			printf("%c", ans[i]);
		printf("]\n");
		clean();
	}
	return 0;
}