#include<iostream>

using namespace std;

char M[50][55];

int f(int R,int C)
{
    R--;
    for(int i=0;i<R;i++)
        for(int j=0;j<C;j++)
        {
            if(M[i][j]=='.' || M[i][j]=='/' || M[i][j]=='\\')
                continue;
            else if(M[i][j]=='#' && M[i+1][j]=='#' && M[i][j+1]=='#' && M[i+1][j+1]=='#')
            {
                M[i][j]     ='/';   M[i][j+1]      ='\\';
                M[i+1][j]   ='\\';   M[i+1][j+1]    ='/';
            }
            else
                return 0;
        }
    for(int i=0;i<C;i++)
        if(M[R][i]=='#')
            return 0;
    return 1;
}


int main()
{
    int T,R,C,P;
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        scanf("%d%d",&R,&C);        
        for(int j=0;j<R;j++)
        {
            scanf("%s",M[j]);
        }
                
        P   =   f(R,C);
                
        if(!P)
        {
            printf("Case #%d:\nImpossible\n",i+1);   
        }
        else
        {
            printf("Case #%d:\n",i+1);
            for(int j=0;j<R;j++)
                printf("%s\n",M[j]);
        }
    }

    return 0;
}
