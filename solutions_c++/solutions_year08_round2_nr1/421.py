#include<iostream>
#include<vector>
#include<string>
#include<queue>
#include<sstream>
#include<map>
#include<stack>
#include<set>
#include<cmath>
using namespace std;
#define PB push_back
#define vi vector<int>
#define vvi vector<vi>
#define LL long long
#define all(v) v.begin(),v.end()
#define pii pair<int,int>
#define MP make_pair
#define INF 200000000
inline int gcd(int m,int n){int tmp;while(n!=0){tmp=m%n;m=n;n=tmp;}return m;}  
LL s2i(string s){LL n;stringstream ss;ss<<s;ss>>n;return n;}
string i2s(LL n){stringstream ss;ss<<n;return ss.str();}
int x[100000],y[100000];
int dp[100000][4][4][4];
int n;
int solve(int pos,int sumx,int sumy,int k)
{
	if(k==3){
		if(sumx==0 && sumy==0) return 1;
		return 0;
	}	
	if(pos==n) return 0;
	int& res=dp[pos][sumx][sumy][k];
	if(res!=-1) return 0;
}
LL solve2()
{
	LL res=0;
	for(int i=0;i<n;i++)
		for(int j=i+1;j<n;j++)
			for(int k=j+1;k<n;k++)
				if((x[i]+x[j]+x[k])%3==0 && (y[i]+y[j]+y[k])%3==0) res++;
	return res;			
}
int main()
{
	int t;
	cin>>t;
	for(int kase=1;kase<=t;kase++)
	{
		cin>>n;
		memset(dp,-1,sizeof(dp));
		LL A,B,C,D,x0,y0,M;
		cin>>A>>B>>C>>D>>x0>>y0>>M;
		x[0]=x0; y[0]=y0;
		for(int i = 1;i<n;i++){
			x[i] = (A * x[i-1] + B)%M;
			y[i] = (C * y[i-1] + D)%M;
		}	
		LL res=solve2();
		//for(int i=0;i<n;i++)
			//res+=solve(i,x[i]%3,y[i]%3);
		cout<<"Case #"<<kase<<": "<<res<<endl;	
	}
}
