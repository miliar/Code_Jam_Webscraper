#include<cstdio>

int t;

int main(){

    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int n,sum=0,min=0,in,check=0;
        scanf("%d",&n);
        for(int j=0;j<n;j++)
        {
            scanf("%d",&in);
            if(j==0)
                min=in;
            else if(in<min)
                min=in;
            check^=in;
            sum+=in;
        }
        if(check)
            printf("Case #%d: NO\n",i+1);
        else
            printf("Case #%d: %d\n",i+1,sum-min);
    }
    return 0;
}
