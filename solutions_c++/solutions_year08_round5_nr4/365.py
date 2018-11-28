#include<ctime>
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
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define CLR(a,x) memset((a),(x),sizeof((a)))
#define dout if(1) cout
const double TOLL=1e-9;
typedef istringstream iss; typedef ostringstream oss; typedef long long int lli;

int dp[200][200];
bool evil[200][200];
int t,H,W,E;

bool valid(int r,int c)
{
	if(r<=0 || c<=0 || r>H || c>W || evil[r][c]) return false;
	return true;
}

int main()
{

	cin>>t; int cn=0;
	while(t--)
	{
		cin>>H>>W>>E;
		int r,c;
		CLR(dp,0); CLR(evil,false);
		for(int i=0;i<E;i++)
		{
			cin>>r>>c;
			evil[r][c]=true;
		}
		dp[H][W]=1;
		for( r=H;r>0;r--) for(c=W;c>0;c--)
		{
			int nr,nc;
			nr=r-1; nc=c-2;
			if(valid(nr,nc))
			{
				dp[nr][nc]+=dp[r][c];
				dp[nr][nc]%=10007;
			}
			nr=r-2; nc=c-1;
			if(valid(nr,nc))
			{
				dp[nr][nc]+=dp[r][c];
				dp[nr][nc]%=10007;
			}
		}
		cn++;
		cout<<"Case #"<<cn<<": "<<dp[1][1]<<endl;

	}

	return 0;
}
