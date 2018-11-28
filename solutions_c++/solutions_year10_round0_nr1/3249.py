#include <iostream>
#include <cmath>
#include <vector>
#include <functional>
#include <algorithm>
#include <numeric>
using namespace std;

int main()
{
freopen("A-large.in","r",stdin);
freopen("a-large.out","w",stdout);
long t,n,k;
cin>>t;
int c=0;
while(t--)
    {
    c++;
    cin>>n>>k;
    if((((1<<n)-1)&k)==((1<<n)-1))
        printf("Case #%d: ON\n",c);
    else
        printf("Case #%d: OFF\n",c);
    }
return 0;
}
