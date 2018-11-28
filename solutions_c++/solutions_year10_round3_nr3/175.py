#include <iostream>

#define GET(X,Y) ( (map[X][(Y>>2)] & (1<<(3-(Y&3)))) != 0 )

int T;
char map[600][200];
int ans=0,a[600];
char bm[600][600];
int b[600][600];
bool used[600][600];
int min(int l1,int l2)
{
if(l1<l2)return l1;
else return l2;    
} 
int down[600][600];

int main()
{   scanf("%d",&T);
    for(int tt=1;tt<=T;tt++)
    {    memset(a,0,sizeof(a));
       ans=0;
        int m,n;char t;
        int i,j;            
        scanf("%d%d",&m,&n);
        for (i=0;i<m;++i)
        {   
                for (j=0;j<(n>>2);++j)
                        scanf("%1X",&map[i][j]);
        }   
        for (i=0;i<m;++i)
                for (j=0;j<n;++j)
                {   
                        bm[i][j]=GET(i,j);
                        used[i+1][j+1]=false;
                        if(bm[i][j]==0)b[i+1][j+1]=0;
                        else b[i+1][j+1]=1;
                          
                } 
          /*for (i=1;i<=m;++i)
               { for (j=1;j<=n;++j) 
                   printf("%d",b[i][j]);
                   
               printf("\n");
               }*/
                   
                   
        for(int l=min(n,m);l>=1;l--)
         {
           for(int i=1;i+l-1<=m;i++)
            for(int j=1;j+l-1<=n;j++)
             {
               for(int x=i;x<=i+l-1;x++)
                 for(int y=j;y<=j+l-1;y++)
                   {
                     if((x-i+y-j)%2==0)
                       {if(b[i][j]!=b[x][y]||used[x][y])
                          goto l1;
                       }
                     else if((x-i+y-j)%2!=0)
                        {if(b[i][j]==b[x][y]||used[x][y])
                          goto l1;
                        }
                     
                   }   
               
               for(int x=i;x<=i+l-1;x++)
                 for(int y=j;y<=j+l-1;y++)
                   used[x][y]=true;
               if(ans<l)ans=l;
               a[l]++;
               l1:;
             }  
         }  
         int ans2=ans;
         for(int i=ans;i>=1;i--)
           if(a[i]==0)ans2--;
         printf("Case #%d: %d\n",tt,ans2);
         for(int i=ans;i>=1;i--)
           if(a[i]>0)printf("%d %d\n",i,a[i]);
}

}

