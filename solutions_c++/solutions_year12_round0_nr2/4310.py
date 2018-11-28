#include<cstdio>
#include<iostream>

using namespace std;
int arr[200];
int best[30][2];

void init()
{
    for(int i=0;i<=30;i++)
    for(int j=0;j<2;j++)
     best[i][j]=-1;
}

void solve()
{
    int s,small,large;
    
    for(int i=0;i<=10;i++)
    {
       for(int j=0;j<=10;j++)
       {
          for(int k=0;k<=10;k++)
          {
              s = i+j+k;
              
              small = min(i,j);
              small = min(small,k);
              
              large = max(i,j);
              large = max(large,k);
              
              if((large-small) < 2)
              {
                   best[s][0] = max(large,best[s][0]);
              }
              else if((large-small)==2)
              {
                   best[s][1] = max(large,best[s][1]);
              }
          }
       }
    }    
}
void print(){
for(int i=0;i<30;i++){printf("%d: ",i);
for(int j=0;j<=1;j++)
printf("%d\t",best[i][j]);
printf("\n");
}
}

int main()
{
    int test,n,surprising,sur,p,ret;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    init();
    solve();
    scanf("%d",&test);

    for(int i=0;i<test;i++)
    {
            printf("Case #%d: ",i+1);
            ret = 0;
            scanf("%d%d%d",&n,&surprising,&p);
            for(int j=0;j<n;j++)
            scanf("%d",&arr[j]);
            sur = surprising;
            
            for(int j=0;j<n;j++)
            {
               if(best[arr[j]][0]>=p)
               ret++;
               else if(best[arr[j]][1]>=p && sur)
               {
                    ret++;sur--;
               }
            }
            
            printf("%d\n",ret);
    }
    
    return 0;
}
