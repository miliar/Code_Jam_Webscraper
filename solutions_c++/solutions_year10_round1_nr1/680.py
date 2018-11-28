#include<iostream>
#define Max 55
using namespace std;

char map[Max][Max];
int dis[4][2] = {{1, 0}, {0, 1}, {1, 1}, {-1, 1}};
int n, k;

bool check(int x, int y)
{
	int tx, ty, t, i;
	char tc;
	
	tc = map[x][y];
	for(i=0;i<4;i++)
	{
		tx = x, ty = y;
		for(t=0;tx>=0 && tx<n && ty>=0 && y<n && map[tx][ty]==tc;t++)
			tx+=dis[i][0], ty+=dis[i][1];
		if(t >= k)
		    return 1;
	}
	return 0;
}

int main()
{
	int N, i, j, ta, tb, z;
	char t;
	bool r, b;
	
	
	scanf("%d", &N);
	z = 1;
	while(N--)
	{
		scanf("%d %d", &n, &k);
		getchar();
		for(i=0;i<n;i++)
		{
		    for(j=0;j<n;j++)
			{
		        t=getchar();
		        map[j][n-i-1] = t;
			}
		    getchar();
		}
		for(i=n-2;i>=0;i--)
		    for(j=0;j<n;j++)
		    {
				ta = i, tb = j;
				while(map[ta][tb]!='.' && ta+1<n && map[ta+1][tb]=='.')
				{
					swap(map[ta][tb], map[ta+1][tb]);
					ta++;
				}
			}
		r = b = 0;
		for(i=0;i<n;i++)
		    for(j=0;j<n;j++)
		    {
		        if(map[i][j]=='R')
					r |= check(i, j);
				else if(map[i][j]=='B')
				    b |= check(i, j);
			}

		printf("Case #%d: ", z++);
		if(!r && !b)
		    printf("Neither\n");
		else if(!b)
		    printf("Red\n");
		else if(!r)
		    printf("Blue\n");
		else
		    printf("Both\n");
	}

}
