#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<map>
#include<functional>
#define maxn 6010
using namespace std;

const int dx[]={0,1,0,-1};
const int dy[]={1,0,-1,0};
char s[100];
int x[maxn],y[maxn],xn,Yn,l,t,i,j,k,p,ox,oy,od,ans,maxx,maxy,minx,miny;
vector<int>xx[maxn];
vector<int>yy[maxn];

struct node{int x,x2,y,y2; }tmp;
vector<node>r;

int cas,ncas;

void solve()
{
   int i,j,k,s=0,len=r.size();
   for (i=minx;i<=maxx;i++)
     for (j=miny;j<=maxy;j++)
     {
         for (k=0;k<len;k++)
           if (r[k].x<=i && r[k].x2>i &&
               r[k].y<=j && r[k].y2>j) break;
         if (k<len)
         { 
//            printf("(%d,%d) in %d\n",i,j,k);
            s++;
         }
     }
   ans=s;
}

int main()
{
    scanf("%d",&ncas);
    for (cas = 1; cas <= ncas; cas++)
    {   
        scanf("%d",&l);
        xn=1;Yn=1;
        x[0]=ox=3001;y[0]=oy=3001;od=0;
        minx=maxx=ox;miny=maxy=oy;
        for (i=0;i<maxn;i++) xx[i].clear(),yy[i].clear();
        
        for (i=0;i<l;i++)
        {
            scanf("%s",s);scanf("%d",&t);
            for (j=0;j<t;j++)
                for (k=0;s[k];k++)
                    if (s[k]=='F')
                    { 
                      ox = ox + dx[od];
                      oy = oy + dy[od];
                      x[xn]=ox;xn++;
                      y[Yn]=oy;Yn++;
                      if (od == 0) yy[oy-1].push_back(ox);
                      if (od == 2) yy[oy].push_back(ox);
                      if (od == 1) xx[ox-1].push_back(oy);
                      if (od == 3) xx[ox].push_back(oy);
                      
                      if (ox>maxx) maxx=ox;
                      if (ox<minx) minx=ox;
                      if (oy>maxy) maxy=oy;
                      if (oy<miny) miny=oy;
                    }
                    else if (s[k]=='R') od = (od+1)%4;
                    else if (s[k]=='L') od = (od+3)%4;
            
        }
        sort(x,x+xn);
        sort(y,y+Yn);
        r.clear();
        
        for (i=0;i<maxn;i++)
        { 
            sort(xx[i].begin(),xx[i].end());
            sort(yy[i].begin(),yy[i].end());
        }
        
        for (i=0;i<xn-1;i++)
        {
            for (j=1;j+1<xx[x[i]].size();j+=2)
            {
               tmp.x=x[i];
               tmp.x2=x[i]+1;
               tmp.y=xx[x[i]][j];
               tmp.y2=xx[x[i]][j+1];
//               printf("(%d,%d) -- (%d,%d) \n",tmp.x,tmp.y,tmp.x2,tmp.y2);
               r.push_back(tmp);
            }
        }
        
        for (i=0;i<Yn-1;i++)
        {
            for (j=1;j+1<yy[y[i]].size();j+=2)
            {
               tmp.y=y[i];
               tmp.y2=y[i]+1;
               tmp.x=yy[y[i]][j];
               tmp.x2=yy[y[i]][j+1];
//               printf("(%d,%d) -- (%d,%d) \n",tmp.x,tmp.y,tmp.x2,tmp.y2);
               r.push_back(tmp);
            }
        }
       // printf("xn=%d  yn=%d  rn = %d\n",xn,Yn,r.size());
       // printf("dx=%d  dy=%d  tot=%d\n",maxx-minx,maxy-miny,(maxx-minx)*(maxy-miny)*r.size());
        ans=0;
        solve();
        
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
