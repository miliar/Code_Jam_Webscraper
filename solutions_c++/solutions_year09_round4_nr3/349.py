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
#include <cstring>
#include <fstream>
using namespace std;
bool mp[41][41];
int N;
#define fir(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
int price[101][26];
int n,k;
bool intersect(int r1,int r2)
{
	fir(i,0,k) if (price[r1][i]>=price[r2][i]) return true;
	return false;
}
void swapRow(int r1,int r2)
{
	fir(i,0,k) swap(price[r1][i],price[r2][i]);
}
int dp[1<<16][16];
int solve(int cs,int ind)
{
	if (__builtin_popcount(cs)==n) return 0;
	int ret=100000;
	if (ind>=n) return ret;
	if (dp[cs][ind]!=-1) return dp[cs][ind];
	fir(i,ind+1,n) {
		if ((cs&(1<<i))!=0) continue;
		//cout<<ind<<" "<<i<<endl;
		//cout<<intersect(i,ind)<<endl;
		if (!intersect(ind,i))
		{
			//cout<<ind<<" "<<i<<endl;
			ret=min(ret,solve(cs|(1<<i),i));
		}
	}
	fir(i,0,n) {
		if ((cs&(1<<i))!=0) continue;
		ret=min(ret,1+solve(cs|(1<<i),i));
		break;
	}
	return dp[cs][ind]=ret;
}
int main()
{
	int tc;
	cin>>tc;int cs=0;
	while(tc--) {
		++cs;
		cin>>n>>k;
		fir(i,0,n) {
			fir(j,0,k)
			cin>>price[i][j];
		}
		//cout<<endl;
		fir(i,0,n) fir(j,i+1,n) {
			if (price[i][0]>price[j][0]) swapRow(i,j);
		}
		//fir(i,0,n) {fir(j,0,k) cout<<price[i][j]<<" ";cout<<endl;}
		int ans=100000;
		memset(dp,-1,sizeof(dp));
		//cout<<intersect(0,1)<<endl;
		ans=1+solve(1<<0,0);
		cout<<"Case #"<<cs<<": "<<ans<<endl;
	}
	return 0;
}