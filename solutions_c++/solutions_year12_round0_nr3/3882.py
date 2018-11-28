#include <stdio.h>
#include <set>
#include <utility>
using namespace std;

int pow10[] = {1,10,100,1000,10000,100000,1000000,10000000, 100000000};

int getlen(int x)
{
    for (int i = 8; i >= 0; i--)
    	if(x >= pow10[i])
            return i+1;
    return 0;
}

int change(int x, int p)
{
    int a, b;
    a = x / pow10[p];
    b = x % pow10[p];
    return b*pow10[getlen(x) - p] + a;
}

int main()
{
    int n, cas = 1, a, b;
    scanf("%d", &n);
    while(n--)
    {
        set <pair<int, int> >Q;
        scanf("%d%d", &a, &b);
        int temp;
        int ans = 0;
        for (int i = a; i <= b; i++)
        {
            int l = getlen(i);
            for (int j = 1; j < l; j++)
            {
                temp = change(i, j);
//                if(Q.count(make_pair(i, temp)) != 0)
//                    continue;
                if(temp >= a && temp <= b && temp > i && Q.find(make_pair(temp, i)) == Q.end())
                {
                    ans++;
                    Q.insert(make_pair(temp, i));
                }
            }
        }
        printf("Case #%d: %d\n",cas++, ans);
    }
    return 0;
}
