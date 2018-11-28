#include <vector>
#include <string>
#include <algorithm>
using namespace std;

FILE *Fin = fopen("D-small-attempt0.in","r");
//FILE *Fou = stdout;
FILE *Fou = fopen("d.out","w");

int n,m;
int map1[11][11], map2[11][11];

bool hash[20];
int order[20];

bool search(int u)
{
	if (u==m)
	{
		for (int i=1; i<=m; i++)
			for (int j=1; j<=m; j++) if (map2[i][j]==1 && map1[order[i-1]][order[j-1]]==0)
				return false;
		return true;
	}
	for (int i=1; i<=n; i++)
		if (!hash[i])
		{
			hash[i] = true;
			order[u] = i;
			if (search(u+1)) return true;
			hash[i] = false;
		}
	return false;
}

int main()
{
	int i,j,k,caseN;
	fscanf(Fin,"%d",&caseN);
	for (int t=1; t<=caseN; t++)
	{
		memset(map1,0,sizeof(map1));
		memset(map2,0,sizeof(map2));
		fscanf(Fin,"%d",&n);
		for (int i=0; i<n-1; i++)
		{
			int a,b;
			fscanf(Fin,"%d%d",&a,&b);
			map1[a][b] = map1[b][a] = 1;
		}
		fscanf(Fin,"%d",&m);
		for (int i=0; i<m-1; i++)
		{
			int a,b;
			fscanf(Fin,"%d%d",&a,&b);
			map2[a][b] = map2[b][a] = 1;
		}
		memset(hash,0,sizeof(hash));
		fprintf(Fou,"Case #%d: %s\n",t,search(0) ? "YES" : "NO");
	}
	return 0;
}
