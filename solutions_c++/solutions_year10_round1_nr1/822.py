#include <stdio.h>
#include <algorithm>

using namespace std;

int move[4][2]={{0,1},{1,1},{1,0},{1,-1}};

char a[110][110], b[110][110];

int len, n;

bool can(int x, int y, int k)
{
	char player=b[x][y];
	int s=0;
	while (b[x][y]==player) 
	{
		s++;
		x+=move[k][0];
		y+=move[k][1];
		if (x<0 || x>=n || y<0 || y>=n) break;	
	}
	return s>=len;
}

int main()
{
	int T, i, j, k,cas=0;
	bool red, blue;
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);	
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d%d", &n, &len);
		for (i=0; i<n; i++)
		  scanf("%s", a[i]);
		for (i=0; i<n; i++)
		 for (j=0; j<n; j++)
		   b[j][n-1-i]=a[i][j]; 
		   
		for (j=0; j<n; j++)
		{
			k=n-1;
		 for (i=n-1; i>=0; i--)
		   if (b[i][j]!='.')
		   {
		   		swap(b[i][j], b[k][j]);
		   		k--;
		   }
		}
		red=blue=false;
		for (i=0; i<n; i++)   
		 for (j=0; j<n; j++)
		   if (b[i][j]!='.')
		   {
		   	 for (k=0; k<4; k++)
		   	   if (can(i, j, k))
		   	     if (b[i][j]=='R') red=true;
		   	     else blue=true;
		   }
   		printf("Case #%d: ", ++cas);
   		if (red && blue) printf("Both\n");
   		else if (red) printf("Red\n");
   				else if (blue) printf("Blue\n");
   						else printf("Neither\n");
	}
	return 0;
}
