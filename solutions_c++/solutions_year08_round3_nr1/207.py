#include<iostream>
#include<cstdio>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<set>
#include<algorithm>

using namespace std;
int main()
{
    long long cases;
    cin>>cases;
    for(long long c=1;c<=cases;c++)
    {
        long long p,k,l;
        cin>>p>>k>>l;
        vector<long long> v(l);
        for(long long i=0;i<l;i++)
            cin>>v[i];
        
        
        sort(v.begin(),v.end());
        reverse(v.begin(),v.end());
        long long w=0;
        long long ans=0;
        for(long long i=0;i<v.size();i++)
        {
            if(i%k==0)
                w++;
            ans+=(w*v[i]);
        }
        printf("Case #%Ld: %Ld\n",c,ans);
//        cout<<ans<<endl;
    }
    return 0;
}
