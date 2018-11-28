#include "iostream"
using namespace std;

int ds[10002];
int ls[10002];
int md[10002];

int main()
{
    int cas, t;
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    scanf("%d",&cas);
    for(t = 0; t<cas; t++)
    {
       int l,d ;
       int i, n;
       int end; 
       int gd = false;
       scanf("%d",&n);
       for(i=0; i<n; i++)
       {
           scanf("%d %d",&ds[i],&ls[i]);
           md[i] = 0;
       }
       scanf("%d",&end);
       md[0] = min(ds[0], ls[0]);
       int j = 0;
       for(i =0; i<n; i++)
       {
           if( md[i] + ds[i] >= end)
           {
               gd = true;
               break;
           }
           int len = md[i];
           for(j = i + 1; j < n; j++)
           {
               if(ds[j] - ds[i] > len)
                   break;
               int ld = min(ds[j] - ds[i], ls[j]);
               if( ld > md[j])
               {
                   md[j] = ld;
               }
           }
       }
   /*    pos = ds[p];
       while(p != n - 1)
       {
           int maxlen = 0;
           if( pos + len >= end)
           {
               gd = true;
               break;
           }
           for(i=p + 1; i<n; i++)
           {
               if( (ds[i] - pos) <= len)
               {
                   int dis = min(ds[i] - pos, ls[i]);
                   if( dis > maxlen)
                   {
                       maxlen = dis;
                       p = i;
                   }
               }
           }
           if( maxlen == 0)
               break;
           len = min(ds[p] - pos, ls[p]);
           pos = ds[p];
       }
       if( pos + len >= end)
       {
           gd = true;
       }*/
       if(gd)
           printf("Case #%d: YES\n",t + 1);
       else
           printf("Case #%d: NO\n", t + 1);

    }
    return 0;
}