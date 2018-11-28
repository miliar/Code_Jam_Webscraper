#include <vector>
#include <algorithm>
using namespace std;
#include <stdio.h>
#include <string.h>

FILE *Fin = fopen("C-large.in","r");
FILE *Fou = fopen("c.out","w");
//FILE *Fin = stdin;
//FILE *Fou = stdout;

const int d[4][2] = {{0,-1},{0,1},{-1,-1},{-1,1}};

int n,m;
char map[100][100];
int id1[100][100];
int tot[2];
vector<int> net[3300];
bool hash[3300];
int done[3300];

bool path(int u)
{
	if (hash[u]) return false;
	hash[u] = true;
	for (int i=0; i<net[u].size(); i++)
	{
		int v = net[u][i];
		if (done[v]==-1 || path(done[v]))
		{
			done[v] = u;
			return true;
		}
	}
	return false;
}

int main()
{
	int i,j,k,caseN;
	fscanf(Fin,"%d",&caseN);
	for (int t=1; t<=caseN; t++)
	{
		fscanf(Fin,"%d%d",&n,&m);
		for (i=0; i<n; i++)
			fscanf(Fin,"%s",map[i]);

		tot[0] = tot[1] = 0;
		for (i=0; i<n; i++)
			for (j=0; j<m; j++)
				if (map[i][j]=='.')
					if (j%2==0) id1[i][j] = tot[0]++;
					else id1[i][j] = tot[1]++;
		
		for (i=0; i<3300; i++) net[i].clear();

		//if (tot[0]<tot[1])
			for (i=0; i<n; i++)
				for (j=0; j<m; j++)
					if (map[i][j]=='.')
					{
						for (k=0; k<4; k++)
						{
							int x = i+d[k][0], y = j+d[k][1];
							if (x>=0&&x<n&&y>=0&&y<m && map[x][y]=='.')
							{
								int a,b;
								a = id1[i][j];
								b = id1[x][y];
								if (j%2!=0) swap(a,b);
								net[a].push_back(b);
							}
						}
					}
		//else
			/*for (i=0; i<n; i++)
				for (j=0; j<m; j++)
					if (map[i][j]=='.' && j%2!=0)
					{
						for (k=0; k<4; k++)
						{
							int x = i+d[k][0], y = j+d[k][1];
							if (x>=0&&y>=0&&y<m && map[x][y]=='.')
							{
								int a,b;
								a = id2[i][j];
								b = id1[x][y];
								fprintf(stderr,"%d %d %d %d\n",i,j,x,y);
								net[b].push_back(a);
							}
						}
					}*/
		
		//int mm = tot[0] < tot[1] ? tot[0] : tot[1];
		int ans = tot[0] + tot[1];
		memset(done,0xFF,sizeof(done));
		for (i=0; i<tot[0]; i++)
		{
			memset(hash,0,sizeof(hash));
			if (path(i)) ans--;
		}

		fprintf(Fou,"Case #%d: %d\n",t, ans);
	}
	return 0;
}

