#include <iostream>
#include <vector>
#include <math.h>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int t, c;
    cin>>t;
    for(c=1;c<=t;c++)
    {
        int low, high, mul;
        cin>>low>>high>>mul;
        long long ans=1;
        while(low*mul < high)
        {
            if(high%mul) high=high/mul+1;
            else high=high/mul;
            //cout<<ans<<"=> "<<high<<endl;
            ans++;
        }
        cout<<"Case #"<<c<<": "<<(long long)ceil((log(ans)/log(2)))<<endl;
    }
    return 0;
}
