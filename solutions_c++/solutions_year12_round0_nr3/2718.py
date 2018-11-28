#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int a, b, digi;

int dig(int n)
{
    int i;
    for(i=10; n/i; i*=10);
    return i;
}

int solve(int n)
{
    int ans = 0, i, j;
    int aa[20] = {0};
    for(i=10; i<digi; i*=10)
    {
        int tmp = (n%i)*(digi/i)+n/i;
        if( tmp < n && tmp>=a)
        {
            bool ok = 0;
            for(j=0; j<ans; j++)
            {
                if(aa[j]==tmp)
                {
                    ok = 1;
                    break;
                }
            }

            if(ok==0)
            {
                //cout<<n<<' '<<tmp<<endl;
                aa[ans++] = tmp;
            }
        }
    }
    //cout<<"   "<<n<<' '<<ans<<endl;;
    return ans;
}

int main()
{
    freopen("C:\\Users\\Administrator\\Downloads\\C-large.in","r",stdin);
    freopen("test.out","w",stdout);
    int cas, i, ans, j;
    scanf("%d", &cas);
    for(i=1; i<=cas; i++)
    {
        scanf("%d%d", &a, &b);
        digi = dig(a);
        ans = 0;
        for(j=a+1; j<=b; j++)
        {
            ans += solve(j);
        }
        printf("Case #%d: %d\n", i, ans);
    }
	return 0;
}
