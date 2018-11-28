#include <iostream>
#include <cstdio>
using namespace std;
int n,b,c;
int a[60];
bool check(int p)
{
    int i;
    for (i=1; i<=n; i++)
        if (a[i]%p!=0&&p%a[i]!=0) return false;
    return true;
}
int main()
{
    freopen("C:\\Users\\¼Ó·ÆÃ¨\\Downloads\\C-small-attempt0.in", "r", stdin);
    freopen("D:OUTPUT.txt", "w", stdout);
    int test,pp;
    int im;
    scanf("%d",&test);
    for (pp=1; pp<=test; pp++)
    {
        int i;
        im=0;
        printf("Case #%d: ",pp);
        scanf("%d%d%d",&n,&b,&c);
        for (i=1; i<=n; i++)
            scanf("%d",&a[i]);
        for (i=b; i<=c; i++)
        {
            if (check(i))
            {
                printf("%d\n",i);
                im=1;
                break;
            }
        }
        if (im==0) printf("NO\n");
    }
}
