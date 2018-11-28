#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<deque>
using namespace std;
#define pb push_back
typedef long long lint;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
int dp[11000];
vector <lint> pl,cl;
int inf=10000000;
string moji(lint a){
	string ret="";string r="";int amari;
	if(a==0) return "0";if(a<0) return "-"+moji(-a);
	while(a>0){
		amari=a%10;r+=(amari+'0');a/=10;
	}
	for(int i=0;i<r.size();i++) ret+=r[r.size()-(i+1)];
	return ret;
}
int main()
{
	lint i,j,k,a,l;int t,n;
	cin>>t;vector <string> out;
	for(i=0;i<t;i++){
		cin>>l>>n;pl=cl;
		for(j=0;j<n;j++){cin>>a;pl.pb(a);}sort(pl.begin(),pl.end());
		for(j=0;j<11000;j++) dp[j]=inf;dp[0]=0;
		for(j=1;j<11000;j++) for(k=0;k<n && j>=pl[k];k++) dp[j]<?=dp[j-pl[k]]+1;
		for(j=10999;j>=0;j--){
			if((l-j)%pl[n-1]==0){
				if(dp[j]>=inf) out.pb("IMPOSSIBLE");else out.pb(moji(dp[j]+(l-j)/pl[n-1]));break;
			}
		}
	}
	for(i=0;i<t;i++) cout<<"Case #"<<i+1<<": "<<out[i]<<endl;
	return 0;
}
