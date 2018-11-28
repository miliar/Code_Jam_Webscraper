#include <stdio.h>
#include <algorithm>

using namespace std;

const int maxn = 110;
const int move[4][2]={{-1,0},{0,-1},{0,1},{1,0}};

int map[maxn][maxn];
int letter[maxn*maxn];

struct node
{
	int n, i;
	bool operator < (const node &big) const
	{
		return n<big.n;
	}
} a[maxn*maxn];

int s[maxn*maxn];

int find(int x)
{
	int temp, anc = x;
	while (s[anc]!=-1) anc = s[anc];
	while (s[x]!=-1)
	{
		temp=s[x];
		s[x]=anc;
		x=temp;
	}
	return anc;
}

int main()
{
	int T, ti, i, j, k, n, m, x, y, kk, nx, ny, d, ln;
	freopen("bl.in", "r", stdin);
	freopen("bl.txt", "w", stdout);	
	scanf("%d", &T);	
for (ti=1; ti<=T; ti++)
{
	scanf("%d%d", &n, &m);
	for (i=0; i<n; i++)
	 for (j=0; j<m; j++)
	 {
	   scanf("%d", &map[i][j]);
	   a[i*m+j].i=i*m+j;
	   a[i*m+j].n=map[i][j];
	 }
	 sort(a, a+n*m);
	 memset(s, 0xff, sizeof(s));
	 for (i=0; i<n*m; i++)
	 {
	 	x=a[i].i/m;
	 	y=a[i].i%m;
	 	d=map[x][y];
	 	kk=-1;
	 	for (k=0; k<4; k++)
	 	{
	 		nx=x+move[k][0];
	 		ny=y+move[k][1];
	 		if (nx>=0 && nx<n && ny>=0 && ny<m)
	 		{
	 			if (map[nx][ny]<d)
				   {
				   		d=map[nx][ny];
				   		kk=k;
				   }
	 		}
	 	}
	 	if (kk>=0)
	 	{
	 		x+=move[kk][0];
	 		y+=move[kk][1];
	 		s[a[i].i]=find(x*m+y);
	 	}
	 }
	printf("Case #%d:\n", ti);
	
	ln=-1; 
	memset(letter, 0xff, sizeof(letter));
	for (i=0; i<n; i++)
	 for (j=0; j<m; j++)
	 {
	 	k=find(i*m+j);
	 	if (letter[k]==-1) letter[k]=++ln;
	 	printf("%c", 'a'+letter[k]);
	 	if (j==m-1) printf("\n");
	 	else printf(" ");
	 }
}
	return 0;
}

