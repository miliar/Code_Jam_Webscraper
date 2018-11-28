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

int gcd(int a,int b) {return b?gcd(b,a%b):a;}

int main()
{
    int t; int cn=0;
    cin>>t;
    while(t--)
    {
	int n,pd,pg; cin>>n>>pd>>pg;
	bool ok=true;
	int wd=pd/gcd(pd,100); int d=100/gcd(pd,100);
	int wg=pg/gcd(pg,100); int g=100/gcd(pg,100);
	cerr<<d<<' '<<wd<<' '<<g<<' '<<wg<<endl;
	if(d-wd!=0 && g-wg==0) ok=false;
	if(wd && wg==0) ok=false;

	if(d==0 || d>n) ok=false;
	
	printf("Case #%d: ",++cn);
	if(ok) printf("Possible\n");
	else printf("Broken\n");
    }

}
