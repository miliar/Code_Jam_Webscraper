#include <iostream>
using namespace std;
#define two(X) (1<<(X))
#define contain(S,X) ((S)&two(X))
int main()
{
freopen("A-small-attempt0 (1).in","r",stdin);
freopen("A-small-attempt0 (1).out","w",stdout);

    int cas;
    scanf("%d",&cas);
    for (int T = 1;T <= cas;T++)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        bool flag = 1;
        for (int i = 0;i < n;i++)
            if (!contain(k,i))
            {
                flag = 0;
                break;
            }
        printf("Case #%d: ",T);
        if (flag)
            printf("ON\n");
        else
            printf("OFF\n");
    }
}
