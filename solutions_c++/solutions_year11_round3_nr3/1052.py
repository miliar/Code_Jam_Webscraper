#include<cstdio>
#include<iostream>
#include<memory.h>

using namespace std;

int a[10001];
int harmony(int);

int main()
{
    int T;
    cin >>T;
    for (int num=1; num<=T; num++)
        harmony(num);
    return 0;
}

int harmony(int num)
{
    memset(a,0,sizeof(a));
    int n,l,h;
    cin >>n >>l >>h;
    int i;
    for (i=0; i<n; i++)
        cin >>a[i];
    int k,ans=0;
    bool found = false;
    for (k=l; k<=h && !found; k++)
    {
        bool flag = true;
        for (i=0; i<n; i++)
            if ((a[i] % k != 0) && (k % a[i] != 0))
            {
                flag = false;
                break;
            }
        if (flag)
        {
            found = true;
            ans = k;
        }
    }
    if (found)
        printf("Case #%d: %d\n",num,ans);
    else
        printf("Case #%d: NO\n",num);

    return 0;
}
