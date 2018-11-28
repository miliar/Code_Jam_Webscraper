#include <iostream>
#include <string.h>

using namespace std;
const int go[4][2]={ { -1,0 }, { 0, -1 }, { 0, 1 }, { 1, 0 } };
int h,w;
int M[110][110];
int d[110][110];
int tot;

void Init(int x,int y)
{
     int i;
     if(d[x][y]>0) return;
     int min=M[x][y],minp=-1,tx,ty;
     for(i=0;i<4;i++) {
        tx=x+go[i][0];
        ty=y+go[i][1];
        if(tx>=1&&tx<=h&&ty>=1&&ty<=w) {
           if(M[tx][ty]<min) {  min=M[tx][ty]; minp=i;  }
        }
     }
     if(minp==-1) 
        d[x][y]=++tot;
}

int Dfs(int x,int y)
{
     int i;
     if(x<1||x>h||y<1||y>w) return 0;
     if(d[x][y]>0) return d[x][y];
     int min=M[x][y],minp=-1,tx,ty;
     for(i=0;i<4;i++) {
        tx=x+go[i][0];
        ty=y+go[i][1];
        if(tx>=1&&tx<=h&&ty>=1&&ty<=w) {
           if(M[tx][ty]<min) {  min=M[tx][ty]; minp=i;  }
        }
     }
     if(minp!=-1) d[x][y]=Dfs(x+go[minp][0],y+go[minp][1]);
     else d[x][y]=++tot;      
     return d[x][y]; 
}
int Dfs2(int x,int y,int tt)
{
     int i;
     if(x<1||x>h||y<1||y>w) return 0;
     //if(d[x][y]>0) return d[x][y];
     d[x][y]=tt;
     int min=M[x][y],minp=-1,tx,ty;
     for(i=0;i<4;i++) {
        tx=x+go[i][0];
        ty=y+go[i][1];
        if(tx>=1&&tx<=h&&ty>=1&&ty<=w) {
           if(M[tx][ty]<min) {  min=M[tx][ty]; minp=i;  }
        }
     }
     if(minp!=-1) {    Dfs2(x+go[minp][0],y+go[minp][1],tt);  }        
}        
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("p2.out","w",stdout);
    int T,i,j,k;
    scanf("%d",&T);
    for(i=1;i<=T;i++) {
       tot=0;
       scanf("%d%d",&h,&w);
       for(j=1;j<=h;j++)
          for(k=1;k<=w;k++)
             scanf("%d",&M[j][k]);
       memset(d,0,sizeof(d));
       tot=0;
       //d[1][1]=1;
       for(j=1;j<=h;j++)
          for(k=1;k<=w;k++)
             if(d[j][k]==0) {
                //tot;
                Dfs(j,k);
             }
       /*
       for(j=1;j<=h;j++)
          for(k=1;k<=w;k++)
             Init(j,k);
       //for(j=1;j<=h;j++,cout<<endl)
          //for(k=1;k<=w;k++)
             //cout<<d[j][k]<<" ";
       for(j=1;j<=h;j++)
          for(k=1;k<=w;k++)
             if(d[j][k]==0) {
                //tot;
                Dfs(j,k);
             }
       */
       printf("Case #%d:\n",i);
       for(j=1;j<=h;j++)
          for(k=1;k<=w;k++)
            if(k<w) printf("%c ",d[j][k]+96);
            else printf("%c\n",d[j][k]+96);         
    }
    
    return 0;
}
