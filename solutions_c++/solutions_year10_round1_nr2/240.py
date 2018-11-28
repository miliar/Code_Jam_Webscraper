/*	SURENDRA KUMAR MEENA	*/
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
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long int LL;
#define ALL(s) (s).begin(),(s).end()
#define R(i,m,n)	for(int i=m;i>=n;i--)
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define VI vector<int>
#define PB push_back
#define CLR(s,v) memset(s,v,sizeof(s))
string to_str(LL x){ ostringstream o;o<<x;return o.str();}
LL to_int(string s){ istringstream st(s); LL i;	st>>i;return i;}
#define FR(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)
typedef pair<int,int> PI;
#define MP(x,y) make_pair(x,y)
#define f first
#define s second
#define VP vector<PI>
#define S(t)	scanf("%d",&t)
const int INF=100000000;
int n;
string b[100],bb[100];
int d,l,m;
int a[100];
int dp[101][301];

int main(){
	int t;
	int cas=0;
	cin>>t;
	while(t--){
		cas++;
		cin>>d>>l>>m>>n;
		F(i,n)	cin>>a[i];
		F(i,101) F(j,301) dp[i][j]=INF;
		F(j,301)	dp[n][j]=0;
		R(i,n-1,0){
			F(j,256){
				int &ret=dp[i][j];
				F(k,256){
					if(abs(k-j)>m)	continue;
					ret=min(ret,dp[i+1][k]+abs(j-a[i]));
					if(j==k && i<n-1)
						ret=min(ret,dp[i+1][k]+d);
				}
				ret=min(ret,dp[i+1][300]+abs(j-a[i]));
//				if(i==n-1 && j==10)
//				cout<<i<<" "<<j<<" = "<<ret<<endl;
			}
			dp[i][300]=dp[i+1][300]+d;
			int cyc=300;
			vector<int> w(1);
			w[0]=-11212;
//			cyc=1;	//change.....................................
			while(cyc--){
			vector<int> v(301);
			F(k,301)	v[k]=dp[i][k];
			if(w==v)	break;
			F(j,256){
				int& ret=dp[i][j];
				int k=max(0,j-m);
				while(k<256){
					if(abs(j-k)>m)	break;
					//insert...
					ret=min(ret,v[k]+l);
//					if(i==2 && j==10 && k==7){
//						cout<<ret<<endl;
//					}
					k++;
				}
			}
			w=v;
			}
		//	F(j,301)	cout<<i<<" "<<j<<" "<<dp[i][j]<<endl;
		}
		int ans=INF;
		F(i,301){
			ans=min(ans,dp[0][i]);
		}
		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
	return 0;
}
