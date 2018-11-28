#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iostream>
using namespace std;
struct Node
{
  int w;
  int len;
  bool operator<(const Node &ret)const
  {
     return w<ret.w;

  }

}node[10000];


int main()
{
    int T,X,S,R,N;
    double t;
    int Bi,Ei,w;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    int cas=0;
    while(T--)
    {
       scanf("%d%d%d%lf%d",&X,&S,&R,&t,&N);
       int ans=0;
       for(int i=0;i<N;i++)
         {
            scanf("%d%d%d",&Bi,&Ei,&w);
            node[i].len=Ei-Bi;
            node[i].w=w;
            ans+=node[i].len;

         }
       sort(node,node+N);
       int LX=X-ans;
       double re=0.0;
       if(t*R>=LX)
       {
           re+=1.0*LX/R;
           t-=1.0*LX/R;
       }
       else
       {
          re+=t;
          re+=1.0*(LX-t*R)/S;
          t=0.0;
       }

       int mi=N;
       for(int i=0;i<N;i++)
       {
          int v=node[i].w+R;
          if(t*v>=node[i].len)
          {
             re+=1.0*node[i].len/v;
             t-=1.0*node[i].len/v;
          }
          else
          {
             re+=t;
             re+=1.0*(node[i].len-t*v)/(node[i].w+S);
             t=0.0;
             mi=i+1;
             break;
          }

       }
       for(int i=mi;i<N;i++)
       {
          re+=1.0*node[i].len/(node[i].w+S);
       }
       printf("Case #%d: ",++cas);
       printf("%.8f\n",re);
    }
    return 0;

}
