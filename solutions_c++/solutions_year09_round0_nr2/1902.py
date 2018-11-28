#include<cstdio>
#include<map>
#include<algorithm>
#define MAX 105
#define inf 1000000001
using namespace std;

int X[4]={-1,0,0,1},Y[4]={0,-1,1,0};
int tab[MAX][MAX],rep[MAX*MAX],n,w,h,i,j,k,ile,et;
bool odw[MAX][MAX];
map<int,int> mapa;

int Find(int a)
{
if(rep[a]==a) return a;
int ra=Find(rep[a]);
rep[a]=ra;
return ra;
}

void Union(int a, int b)
{
int ra=Find(a);
int rb=Find(b);
rep[ra]=rb;
}

void DFS(int x, int y)
{
int i,wsk,best=inf;

odw[x][y]=true;
for(i=0; i<4; ++i)
     if(x+X[i]>=0 && y+Y[i]>=0 && x+X[i]<h && y+Y[i]<w)
          if(tab[x+X[i]][y+Y[i]]<tab[x][y] && tab[x+X[i]][y+Y[i]]<best)
               {
               best=tab[x+X[i]][y+Y[i]];
               wsk=i;
               }
       
if(best!=inf)
     {
     Union(x*w+y,(x+X[wsk])*w+(y+Y[wsk]));
     if(!odw[x+X[wsk]][y+Y[wsk]]) DFS(x+X[wsk],y+Y[wsk]);
     }     
}
     
int main()
{
scanf("%d",&n);

for(i=1; i<=n; ++i)
     {
     scanf("%d %d",&h,&w);
     if(i==1) printf("%d %d\n",h,w);
     ile=et=0;
     mapa.clear();
     
     for(j=0; j<h; ++j)
          for(k=0; k<w; ++k)
               {
               scanf("%d",&tab[j][k]);
               odw[j][k]=false;
               rep[ile]=ile;
               ++ile;
               }
 
     for(j=0; j<h; ++j)
          for(k=0; k<w; ++k)
               if(!odw[j][k]) DFS(j,k);
               
     printf("Case #%d:\n",i);
     for(j=0; j<h; ++j)
         {
         for(k=0; k<w; ++k)
              if(mapa[Find(j*w+k)]!=0) printf("%c ",(char)(mapa[Find(j*w+k)]+'a'-1)); else
                   {
                   ++et;
                   mapa[Find(j*w+k)]=et;
                   printf("%c ",(char)(mapa[Find(j*w+k)]+'a'-1));
                   }                   
         printf("\n");
         }
     }
     
return 0;
}
