#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define FOR1(i,n) for(i=1;i<=n;i++)
#define FORab(i,a,b) for(i=a;i<=b;i++)
int main()
{
    int t,cn=1,n,i,arr[1010];
    freopen("input.txt","r",stdin);
    freopen("outputC2.txt","w",stdout);

	cin>>t;
	while(t--)
	{
        cin >>n;
        int sum=0,exor=0,nsum=0;
        FOR(i,n)
        {
            cin>>arr[i];
            sum+=arr[i];
            nsum+=arr[i];
        }
        sort(arr,arr+n);
        int ans=0;
        for(i=n-1;i>=1;i--)
        {
            exor^=arr[i];
            nsum-=arr[i];
            if(exor==nsum)
            {
                ans=sum-nsum;
            }
        }

        cout<<"Case #"<<cn++<<": ";

        if(ans==0)cout<<"NO"<<endl;
        else cout<<ans<<endl;
	}

	return 0;
}
