#include <iostream>

using namespace std;

int ax[4]={-1,0,0,1};
int ay[4]={0,-1,1,0};

int n, m;
int mapa[100][100];
bool pase[100][100];
char ans[100][100];
char pos;

char baja(int x,int y)
{
    if(pase[x][y])
    {
	   return ans[x][y];
    }
    pase[x][y]=1;
    int k, w=1000000000;
    int i, j;
    for(k=0; k<4; k++)
    {
	   if( x+ax[k]>-1 && x+ax[k]<n && y+ay[k]>-1 && y+ay[k]<m && mapa[x+ax[k]][y+ay[k]]<w && mapa[x+ax[k]][y+ay[k]]<mapa[x][y])
	   {
		  i=x+ax[k];
		  j=y+ay[k];
		  w=mapa[i][j];
	   }
    }
    if(w!=1000000000)
    {
	   return ans[x][y]=baja(i,j);
    }
    pos++;
    return ans[x][y]=pos;
}

void rainfall(int qwe)
{
    int i, j;
    scanf("%d%d",&n,&m);
    pos='a';
    pos--;
    for(i=0; i<n; i++)
    {
	   for(j=0; j<m; j++)
	   {
		  scanf("%d",&mapa[i][j]);
		  pase[i][j]=0;
	   }
    }
    for(i=0; i<n; i++)
    {
	   for(j=0; j<m; j++)
	   {
		  if( !pase[i][j] )
		  {
			 baja(i,j);
		  }
	   }
    }
    printf("Case #%d:\n",qwe);
    for(i=0; i<n; i++)
    {
	   for(j=0; j<m; j++)
	   {
		  printf("%c ",ans[i][j]);
	   }
	   printf("\n");
    }
    return;
}

int main()
{
    freopen("cosa.in","r",stdin);
    freopen("cosa.txt","w",stdout);
    int n, i;
    scanf("%d",&n);
    for(i=1; i<=n; i++)
    {
	   rainfall(i);
    }
    return 0;
}