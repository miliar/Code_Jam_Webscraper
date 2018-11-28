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

int arr[1001]; int n;
int backward[1001];
int backsum[1001];

int main()
{
    int t; cin>>t; int cn=0;
    while(t--)
    {
	cin>>n;
	for(int i=0;i<n;i++) cin>>arr[i];
	sort(arr,arr+n);
	backward[n-1]=arr[n-1]; backsum[n-1]=arr[n-1];

	for(int i=n-2;i>=0;i--) backward[i]=(backward[i+1]^arr[i]), backsum[i]=arr[i]+backsum[i+1];
	int rv=-1;
	int fsum=0, fxor=0;
	for(int i=0;i<n-1;i++)
	{
	    fsum+=arr[i]; fxor=(fxor^arr[i]);
	    if(fxor==backward[i+1])
	    {
		if(fsum>rv) rv=fsum;
		if(backsum[i+1]>rv) rv=backsum[i+1];
	    }
	}
	
	if(rv==-1) printf("Case #%d: NO\n",++cn);
	else printf("Case #%d: %d\n",++cn,rv);
	
    }

}
