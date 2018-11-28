#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;

typedef long long LL;
#define PB push_back
#define all(v) (v).begin(),(v).end()
#define vi vector<int>
#define vvi vector<vi>
#define vs vector<string>
#define pii pair<int,int>
#define INF 200000000
#define MP make_pair
LL gcd(LL m,LL n){LL tmp;while(n!=0){tmp=m%n;m=n;n=tmp;}return m;}   
LL lcm(LL m,LL n){return (m*n)/gcd(m,n);}
string i2s(LL n){stringstream ss;ss<<n;return ss.str();}
LL s2i(string s){stringstream ss;ss<<s;LL n;ss>>n;return n;}

string W="welcome to code jam";
string A;

int dp[505][20];
int solve(int pos,int k){
	if(k==W.size()) return 1;
	if(pos==A.size()) return 0;
	int& res=dp[pos][k];
	if(res!=-1) return res;
	res=0;
	for(int i=pos;i<A.size();i++)
		if(W[k]==A[i]){ 
			res+=solve(i+1,k+1);
			if(res>=1000000) res%=10000;
		}	
	return res;	
}
int main()
{
	int N;
	cin>>N;
	getline(cin,A);
	for(int t=1;t<=N;t++)
	{
		memset(dp,-1,sizeof(dp));
		getline(cin,A);
		int res=solve(0,0);
		res%=10000;
		string rs=i2s(res);
		for(int i=rs.size();i<4;i++) rs="0"+rs;
		printf("Case #%d: ",t);
		cout<<rs<<endl;
	}
}