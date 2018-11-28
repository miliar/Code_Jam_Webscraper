#include<iostream>
#include<stdio.h>
#include<string>
#include<string.h>
#include<algorithm>
#include<vector>
#include<map>
#include<sstream>
#include<cmath>
#include<set>
using namespace std;
set<long long>hash;

int main()
{
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        int a,b;
        cin>>a>>b;
        int ans=0;
        for(int p=a;p<=b;p++)
        {
            if(p<10)continue;
            for(int q=10;q<=a;q*=10)
            {
                int newn=(p/q)+(p%q)*(pow(10,(int)(log10(p)+0.00001))/q)*10;
                if(newn>p&&newn<=b&&hash.count((long long)p*100000000+newn)==0)
                {
                    //cout<<p<<" "<<newn<<endl;
                    hash.insert(p*100000000+newn);
                    ans++;
                }

            }
        }
        printf("Case #%d: %d\n",tt,ans);
    }

    return 0;
}
