#include<cstdio>

int t;

int main(){

    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int n;
        scanf("%d",&n);
        int in;
        double sol=0;
        for(int j=1;j<=n;j++)
        {
            scanf("%d",&in);
            if(in!=j)
                sol+=1;
        }
        printf("Case #%d: %.6lf\n",i+1,sol);
    }
    return 0;
}
