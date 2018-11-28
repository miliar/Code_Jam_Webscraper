#include<cstdio>
#include<cstdlib>
int T,N,M;
char str[51][51];
int main()
{
    freopen("test.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(int r=1;r<=T;r++)
    {
       scanf("%d%d",&N,&M);
       printf("Case #%d:\n",r);
       for(int i=0;i<N;i++)
          scanf("%s",str[i]);
       for(int i=0;i<N;i++)
         for(int j=0;j<M;j++)
         {
            if((j==M-1||i==N-1)&&str[i][j]=='#')
              {printf("Impossible\n");goto out;}        
            else if(str[i][j]=='#')
            {
              if(str[i+1][j]=='#'&&str[i][j+1]=='#'&&str[i+1][j+1]=='#')
                 {str[i+1][j]='\\';str[i][j+1]='\\';str[i+1][j+1]='/';str[i][j]='/';} 
              else
                 {printf("Impossible\n");goto out;}       
            }     
         }     
         for(int i=0;i<N;i++)
           printf("%s\n",str[i]);
         out:;
    }
    //system("pause");
    return 0;
}
