#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
using namespace std;
#define tr(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++) 
#define all(a) (a).begin(),(a).end()
#define FR(i,x,y) for(int i=x;i<y;++i)
#define FRZ(i,y) FR(i,0,y)
typedef long long int ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<string,string> ds;
typedef pair<int,ds> ii;
#define PB push_back
#define SZ(a) (int)(a).size()
#define GI ({int t ;scanf("%d",&t);t;})
int MOD = 10000;
int main()
{
    int nC = GI;
    getchar();
    string ip = "welcome to code jam";
    int sz1 = SZ(ip);
    FR(nc,1,nC+1)
    {
	printf("Case #%d: ",nc);
	string str;
	getline(cin,str);
	int dp[20];
	memset(dp,0,sizeof dp);
	int sz = SZ(str);
	dp[0] = 1;
	FRZ(i,sz)
	{
	    FRZ(j,sz1)
		if(str[i] == ip[j])
		    dp[j+1] = (dp[j+1] + dp[j]) % MOD;
	}
	ostringstream ss;
	ss << dp[sz1];
	string op = ss.str();
	while(SZ(op) != 4)
	    op = '0' + op;
	cout << op << endl;
    }
}
