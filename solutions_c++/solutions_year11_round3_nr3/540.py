#include<ctime>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;

int arr[10001];

int main()
{
    int t; cin>>t; int cn=0;
    while(t--)
    {
	int n, l, h; cin>>n>>l>>h;
	for(int i=0;i<n;i++) cin>>arr[i];
	int ans=-1;
	for(int i=l;i<=h && ans==-1;i++)
	{
//	    cerr<<i<<endl;
	    bool ok=true;
	    for(int j=0;j<n;j++)
	    {
		if(arr[j]%i!=0 && i%arr[j]!=0)
		{
		    ok=false; break;
//		    cerr<<"   "<<arr[j]<<endl;
		}
	    }
	    if(ok) ans=i;
	}
	printf("Case #%d: ",++cn);
	if(ans>=0) printf("%d\n",ans);
	else printf("NO\n");
    }

}
