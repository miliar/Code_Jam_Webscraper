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
#define pdi pair<double,int>
#define MP make_pair
#define GI ({int t ; scanf("%d",&t);t;})
#define INF 200000000
int n,q;
string A[100],Q[1000];
int dp[105][1005];
int solve(int s,int pos)
{
	if(pos==q) return 0;
	int& res=dp[s][pos];
	if(res!=-1) return res;
	res=INF;
	if(A[s]==Q[pos]){
		for(int i=0;i<n;i++)
			if(i!=s) res=min(res,1+solve(i,pos+1));
	}		
	else		
		res=solve(s,pos+1);
	return res;		
}
int main()
{
	int t=GI;
	string str;
	for(int kase=1;kase<=t;kase++)
	{
		n=GI;
		getline(cin,str);
		for(int i=0;i<n;i++)
			getline(cin,A[i]);
		q=GI;
		getline(cin,str);
		for(int i=0;i<q;i++)
			getline(cin,Q[i]);
		memset(dp,-1,sizeof(dp));
		int res=INF;
		for(int i=0;i<n;i++)
			if(A[i]!=Q[0])
				res=min(res,solve(i,0));
		cout<<"Case #"<<kase<<": "<<res<<endl;	
	}
}