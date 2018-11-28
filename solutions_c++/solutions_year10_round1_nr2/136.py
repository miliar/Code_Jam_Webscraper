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
int dp[110][260];
int inf=1000000000;
int kei(int a,int b){
	if(a==0) return 0;
	return (a-1)/b;
}
int main()
{
//	cout<<(-1/5)<<endl;
//	cout<<kei(6,3)<<endl;
	int i,j,k,l,m,n,a,d,z,t;vector <int> out;cin>>t;
	for(i=0;i<t;i++){
		cin>>d>>a>>m>>n;
		vector <int> re;
		for(j=0;j<n;j++){cin>>z;re.pb(z);}
		if(n<2){out.pb(0);continue;}
//		cout<<i<<' '<<n<<endl;
		for(j=0;j<110;j++) for(k=0;k<260;k++) dp[j][k]=inf;
		for(j=0;j<n;j++) dp[j][re[j]]=d*j;
		for(j=0;j<256;j++) dp[0][j]<?=abs(j-re[0]);
		for(j=0;j<n-1;j++) for(k=0;k<256;k++){
//			if(m>0) dp[j+1][re[j+1]]<?=dp[j][k]+(abs(k-re[j+1])/m*a);
			if(m>0) dp[j+1][re[j+1]]<?=dp[j][k]+(kei(abs(k-re[j+1]),m)*a);
			dp[j+1][k]<?=dp[j][k]+d;
			for(l=max(0,k-m);l<=k+m && l<256;l++){
				if(l>=0 && l<260) dp[j+1][l]<?=dp[j][k]+abs(l-re[j+1]);
			}
		}
		int ret=inf;for(j=0;j<256;j++) ret<?=dp[n-1][j];out.pb(ret);
	}
	for(i=0;i<t;i++) cout<<"Case #"<<i+1<<": "<<out[i]<<endl;
	return 0;
}
