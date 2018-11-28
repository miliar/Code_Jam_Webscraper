#include<stdlib.h>
#include<stdio.h>

int main()
{
    int T,N;
    freopen("A-large.in","r",stdin);
    freopen("large-attempt.out","w",stdout);
    scanf("%d",&T);
    //printf("%d",T);
    for(int i=0;i<T;i++)
    {
            int R,C;
            char a[100][100];
            scanf("%d%d",&R,&C);
            for(int j=0;j<R;j++)
            {
                    scanf("%s",a[j]);
            };
            int flag=1;
            for(int j=0;j<R;j++)
            {
                    for(int k=0;k<C;k++)
                    {
                            if(a[j][k]=='#')
                                            if(a[j][k+1]=='#'&&a[j+1][k]=='#'&&a[j+1][k+1]=='#')
                                            { 
                                               a[j][k]='/';a[j][k+1]='\\';a[j+1][k]='\\';a[j+1][k+1]='/';
                                            }
                                            else
                                                flag*=0;
                    }
            }
            printf("Case #%d:\n",i+1);
            if(flag==0)
                       printf("Impossible\n");
            else
            for(int j=0;j<R;j++)
            {
                    printf("%s\n",a[j]);
            }
            
                            
    }
    //system("pause");
}
