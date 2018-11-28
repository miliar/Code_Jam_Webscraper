
#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<cstdlib>
#include<cstring>
#include<sstream>
#include<cassert>
#include<climits>
using namespace std;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vb> vvb;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef pair<int,int> ii;
typedef pair<int,ii> pii;
typedef long long LL;
#define sz(c) (int)c.size()
#define pb push_back
#define all(v) v.begin(),v.end()
#define inc(i,n) for(int i=0;i<n;i++)
#define dec(i,n) for(int i=n-1;i>=0;i--)
#define FOR(i,a,n) for(int i=a;i<n;i++)
#define INF 1000000000
#define F first
#define S second
int dp[100][101][101];
int minMoves(int pos1,int pos2,int index,const vvi &arr){
	if(pos1>100 || pos2>100 || pos1<=0 || pos2<=0)
		return INF;
	if(index==sz(arr))	
		return 0;
	int &ans = dp[index][pos1][pos2];
	if(ans!=-1) return ans;
	ans = INF;

	if(arr[index][0]==1) //orange
	{
		int dist = abs(arr[index][1]-pos1)+1;
		for(int i=0;i<=dist;i++){
			ans = min(ans,dist+minMoves(arr[index][1], pos2+i,index+1,arr));
			ans = min(ans,dist+minMoves(arr[index][1], pos2-i,index+1,arr));
		}
	}
	else{
		int dist = abs(arr[index][1]-pos2)+1;
		inc(i,dist+1){
			 ans = min(ans,dist+minMoves(pos1+i,arr[index][1],index+1,arr));
			 ans = min(ans,dist+minMoves(pos1-i,arr[index][1],index+1,arr));
		}
	}
	return ans;
}
int main(){

	int T;
	cin>>T;
	for(int g=1;g<=T;g++){
		int N;
		cin>>N;
		vvi arr(N,vi(2));
		inc(i,N){
			char b;
			cin>>b;
			arr[i][0]=(b=='O')?1:0;
			cin>>arr[i][1];
		}
		memset(dp,-1,sizeof dp);
		printf("Case #%d: %d\n",g,minMoves(1,1,0,arr));
	}
return EXIT_SUCCESS;

}
