#include<cstdio>
#include<iostream>
#include<string.h>
#include<algorithm>

using namespace std;

const int MAXN = 2000000;

long long sum[ MAXN ],val[ MAXN ];
int cnt[ MAXN ];
int next[ MAXN ];

int R,K,n;
int g[ MAXN ];
long long tot;
int len;
int main()
{
    int i,J,k,o;
    int ncase,casenum = 1;
    int add;
    freopen("C-large.in.txt","r",stdin);
    freopen("b.txt","w",stdout);
    cin>>ncase;
    while(ncase--)
    {
          memset(sum,0,sizeof(sum));
          memset(cnt,0,sizeof(cnt));
          scanf("%d%d%d",&R,&K,&n);
          
          for(i = 0;i < n;i++) scanf("%d",&g[i]);
          
          for(i = 0;i < n;i++)
          {
           for(add = 0,J = i,k = 0;k < n;J = (J + 1) % n,k++)
           {
               add = add + g[J];
               if(add > K) 
               {
                      next[i] = J;
                      break;
               }
               val[i] = add;
           }
           if(add <= K)
           next[i] = J;
          }
         
         long long c = 0;
         for(i = 0,J = 1;i < n;i = next[i],J++)
         {
             c += val[i];  
             if(cnt[i] > 0)
             {
                len = (J - cnt[i]);
                tot = (c - sum[i]);
                break;
             }
             sum[i] = c;
             cnt[i] = J;
         }
        
         printf("Case #%d: ",casenum++);
         if(R < J)
         {
           long long c = 0;
           for(i = 0,k = 1;k <= R;i = next[i],k++)
              c += val[i]; 
           cout<<c<<endl;
         }
         else
         {
        
            long long res = c - val[i];
            res += (long long)( R - (J - 1) ) / len * tot;
            o = ( R - (J - 1) ) % len;
            for(J = 1;J <= o;i = next[i],J++)
             res += val[i];
            cout<<res<<endl; 
              
         }  
    }
    //system("pause");
    return 0;
}
