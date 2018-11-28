#include <cstdio>
#include <algorithm>
using namespace std;

bool win(int a,int b)
{
    if (a>b)
        swap(a,b);
    bool res=true;
    while (a && b<a*2)
    {
        res = !res;
        b=b%a;
        swap(a,b);
    }
    return res;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,A1,A2,B1,B2;
    scanf("%d",&T);
    for (int i=0;i<T;++i)
    {
        scanf("%d%d%d%d",&A1,&A2,&B1,&B2);
        long long res=0;
        for (int a=A1;a<=A2;++a)
            for (int b=B1;b<=B2;++b)
                res+=win(a,b);
        printf("Case #%d: %lld\n",i+1,res);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}

