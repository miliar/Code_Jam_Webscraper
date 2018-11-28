#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int p[110][110];
int n, k;

struct node
{
	int i;
	bool operator < (const node &big) const
	{
		return p[i][0]<p[big.i][0];
	}
} o[110];

bool mat[110][110];
bool b[110];
int match[110];
int ans, cas;

bool over(int x, int y)
{
	int i;
	for (i=0; i<k; i++)
	  if (p[x][i]>=p[y][i]) return false;
	return true;  
}

bool can(int x)
{
	int i;
	b[x]=false;
	for (i=0; i<n; i++)
	  if (mat[x][i])
	    if (match[i]==-1 || b[match[i]] && can(match[i]))
	    {
	    	match[i]=x;
	    	return true;
	    }
	return false;   
}

int main()
{
	int T, i, j;
	freopen("cl.txt", "r", stdin);
	freopen("c.out", "w", stdout);
	
	scanf("%d", &T);
while (T--)
{
	scanf("%d%d", &n, &k);
	for (i=0; i<n; i++)
	{
		o[i].i=i;
		for (j=0; j<k;j++)
		  scanf("%d", &p[i][j]);
	}
	sort(o, o+n);	
	memset(mat, false, sizeof(mat));
	for (i=0; i<n; i++)
	  for (j=i+1; j<n; j++)
	    if (over(o[i].i, o[j].i))
			 mat[i][j]=true;
	ans=0;   
	memset(match, 0xff, sizeof(match)); 
	for (i=0; i<n; i++)
	{
		memset(b, true, sizeof(b));
		if (can(i)) ans++;
	}
	printf("Case #%d: %d\n", ++cas, n-ans);
}
	return 0;
}
