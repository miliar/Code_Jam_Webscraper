/*
Program:
Author: ldl
Method:
DataStructure:
Date: 2010-2-
Status:
Remark:
*/
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>

using namespace std;

int r,n;
int f[1001];
long long k;
unsigned long long g[1001],h[1001];
unsigned long long ans;

int main()
{
//    freopen("test.in","r",stdin);
//    freopen("test.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int p = 1; p <= T ; p++)
    {
        cin>>r>>k>>n;
        for (int i = 0; i < n ; i++) cin>>g[i];
        for (int i = 0; i < n ; i++)
        {
            h[i] = 0;
            int j = i;
            while (h[i] + g[j] <= k)
            {
                h[i] += g[j];
                j = (j + 1) % n;
                if (j == i) break;
            }
            f[i] = j;
        }
        ans = 0;
        int j = 0;
        for (int i = 0; i < r ; i++)
        {
            ans += h[j];
            j = f[j];
        }
        cout<<"Case #"<<p<<": "<<ans<<endl;
    }
    return 0;
}
    
