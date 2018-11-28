#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;

long long small;
long long sum;
long long temp;
int t;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
    int cas = 1;
    cin>>t;
    long long a;
    int cnt;
    while(t--)
    {
        sum = 0;
        small = 1000005;
        temp = 0;
        cin>>cnt;
        while(cnt--)
        {
            cin>>a;
            temp^=a;
            sum+=a;
            small = min(small,a);
        }
        if(temp!=0)
        {
            cout<<"Case #"<<cas++<<": NO"<<endl;
        }
        else
        {
            cout<<"Case #"<<cas++<<": "<<sum-small<<endl;
        }
    }
    return 0;
}
