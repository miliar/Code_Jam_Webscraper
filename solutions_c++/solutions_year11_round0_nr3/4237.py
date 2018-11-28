#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cctype>
#include <sstream>
#include <iomanip>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <list>
#include <climits>
using namespace std;
int main()
{
ios_base::sync_with_stdio(0);
freopen("c-large.in", "r", stdin);
freopen("c-large.out", "w",stdout);
long long i,j,n,t,mn,sum,xsum,txt=0;
cin>>t;
    while(t--){
        cin>>n;
        sum=xsum=mn=0;
        for(i=1;i<=n;i++){
            cin>>j;
            sum+=j;
            if(mn>j||mn==0)mn=j;
            xsum^=j;
        }
        if(xsum)cout<<"Case #"<<++txt<<": NO"<<endl;
        else cout<<"Case #"<<++txt<<": "<<sum-mn<<endl;
    }
return 0;
}
