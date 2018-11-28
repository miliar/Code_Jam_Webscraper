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
lint inf=1000000000;
lint dp[12][12][550];
lint pl[12][550];
vector <int> te,cl;
lint calc(int n,int a,int b,int c){
	if(a==n-1){
		if(te[c*2]>b+1 || te[c*2+1]>b+1) return inf;
		if(te[c*2]<=b && te[c*2+1]<=b) return 0;return pl[a][c];
	}
	if(dp[a][b][c]>-1) return dp[a][b][c];
	return dp[a][b][c]=min(pl[a][c]+calc(n,a+1,b+1,c*2+1)+calc(n,a+1,b+1,c*2),calc(n,a+1,b,c*2+1)+calc(n,a+1,b,c*2));
}
int main()
{
	int i,j,k,n,t,a,l;vector <lint> out;
	cin>>t;
	for(i=0;i<t;i++){
		cin>>n;te=cl;
		for(j=0;j<(1<<n);j++){scanf("%d",&a);te.pb(n-a);}
		for(j=n-1;j>=0;j--) for(k=0;k<(1<<j);k++) scanf("%d",&pl[j][k]);
		for(j=0;j<12;j++) for(k=0;k<12;k++) for(l=0;l<550;l++) dp[j][k][l]=-1;
//		for(j=0;j<(1<<n);j++) cout<<te[j]<<endl;
/*		for(j=0;j<(1<<n);j++){
			int b=j;
			for(k=0;k<n;k++){
				b/=2;
				if(k>=te[j]){
					if(!sumi[k][b]){sumi[k][b]=true;ret++;}
				}
			}
		}
		out.pb(ret);
*/		
//		cout<<calc(n,1,1,1)<<' '<<calc(n,1,0,1)<<endl;
		out.pb(calc(n,0,0,0));
//		for(j=n-1;j>=0;j--) for(k=0;k<(1<<j);k++) cout<<j<<' '<<k<<' '<<pl[j][k]<<endl;
//		for(j=0;j<n;j++) for(k=0;k<=j;k++) for(l=0;l<(1<<j);l++) cout<<j<<' '<<k<<' '<<l<<' '<<dp[j][k][l]<<endl;
	}
	for(i=0;i<t;i++) cout<<"Case #"<<i+1<<": "<<out[i]<<endl;
	return 0;
}
