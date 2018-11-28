#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>

using namespace std;

long long n,k;
long long f[31];

int main()
{
//    freopen("test.in","r",stdin);
//    freopen("test.out","w",stdout);
    f[1] = 1;
    for (int i = 2; i <= 30 ; i++) 
        f[i] = f[i - 1] * 2 + 1;
    int T;
    scanf("%d", & T);
    for (int p = 1; p <= T ; p++)
    {
        cin>>n>>k;
        printf("Case #%d: ", p);
        if (k && k % (f[n] + 1) == f[n]) printf("ON\n");
          else printf("OFF\n");
    }
    return 0;
}
    
