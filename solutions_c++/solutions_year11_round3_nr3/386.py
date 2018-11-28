#include<iostream>
using namespace std;
int num[10101];
int main()
{
    int cases;
    scanf("%d",&cases);
    for(int ca=1;ca<=cases;ca++)
    {
        int n,l,h;
        scanf("%d%d%d",&n,&l,&h);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&num[i]);
        }
        int res=-1;
        for(int i=l;i<=h;i++)
        {
            bool judge=true;
            for(int j=0;j<n;j++)
            {
                if(num[j]%i&&i%num[j])
                {
                    judge=false;
                    break;
                }
            }
            if(judge)
            {
                res=i;
                break;
            }
        }
        printf("Case #%d: ",ca);
        if(res==-1) puts("NO");
        else
        printf("%d\n",res);
    }
}
