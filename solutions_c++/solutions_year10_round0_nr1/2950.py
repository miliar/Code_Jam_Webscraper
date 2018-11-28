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


int main()
{
    int t;
    long long n,k;
    cin>>t;
    int cn=0;
    while(t--)
    {
	cn++;
	printf("Case #%d: ",cn);
	cin>>n>>k;
	if((k+1)%(1ll<<n)==0)
	{
	    printf("ON\n");
	}
	else
	{
	    printf("OFF\n");
	}
    }


}
