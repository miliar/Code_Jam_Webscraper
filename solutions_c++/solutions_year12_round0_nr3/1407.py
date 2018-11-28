#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
#define maxn 2000000
int flag[maxn];
int T;
int A,B;
int solve(int d)
{
    int tmp2;
    int ans = 0;
    int tmp = d;
    int k = 1;
    while(tmp >= 10)
    {
        tmp/=10;
        k = k * 10;
    }
    if(k == 1)
        return 0;
    tmp = tmp2 = d;

    do
    {
        if(tmp2 >= A && tmp2 <= B)
        {
        //    cout << d <<' '<<tmp2<<endl;
            flag[tmp2] = 1;
            ans++;
        }
        tmp = tmp2;
        tmp2 = ( tmp % k ) * 10 + tmp / k;


    }while(tmp2 != d);
    return  ans * (ans - 1) / 2;
}
int main()
{
    int sum,cc,i;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    while(cin >> T)
    {
        cc = 1;
        while(T--)
        {
            sum = 0;

            memset(flag,0,sizeof(flag));
            cin >> A >> B;
            for(i = A; i<= B; i++)
            {
                if(flag[i] == 0)
                    sum += solve(i);
            }
            printf("Case #%d: %d\n",cc++,sum);
        }
    }
    return 0;
}
