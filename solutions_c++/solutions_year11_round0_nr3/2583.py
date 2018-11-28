#include <iostream>
#include <math.h>
#include <list>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <memory.h>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <stdio.h>
#include <assert.h>

using namespace std;
#define SET(a,n) memset(a,n,sizeof(a));
#define FOR(a,b,c) for(int a=b;a<c;++a)
#define GN(a) scanf("%d",&a)

typedef long long int LL;
typedef vector<int> VI;

using namespace std;

int main()
{
    freopen("i.txt","r",stdin);
    freopen("C-large.txt","w",stdout);
    int t;
    cin>>t;
    FOR(test,1,t+1)
    {
        int n;
        cin>>n;
        int arr[1002];
        FOR(i,0,n)cin>>arr[i];
        int x = 0;
        FOR(i,0,n)
        {
            x = x^arr[i];
        }
        int ans = -1;
        if(x==0)
        {
            sort(arr,arr+n);
            int sum = 0;
            FOR(i,0,n)sum+=arr[i];
            ans = sum - arr[0];
        }
        cout<<"Case #"<<test<<": ";
        if(ans==-1)cout<<"NO";
        else cout<<ans;

        puts("");
    }
    return 0;
}

