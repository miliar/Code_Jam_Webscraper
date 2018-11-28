#include <iostream>
const int ans[31] =
{0,5,27,143,751,935,607,903,991,335,47,943,471,55,447,463,991,95,607,263,151,855,527,743,351,135,407,903,791,135,647};

int main()
{
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    int Test,n;
    scanf("%d",&Test);
    for (int T = 1; T <= Test; ++T)
    {
        scanf("%d",&n);
        printf("Case #%d: %03d\n",T,ans[n]);
    }
    return 0;
}
