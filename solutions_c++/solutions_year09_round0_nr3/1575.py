#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<sstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;

#define LET(x,a) 	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	IFOR(it,v.begin(),v.end())
#define FOR(i,a,b)  	for(int i=(int)(a) ; i < (int)(b);++i)
#define REP(i,n) 	FOR(i,0,n)
#define PB		push_back
#define MP 		make_pair
#define EPS		1e-9
#define INF 2000000000
#define MOD 10000

typedef vector<int>	VI;
typedef long long	LL;
typedef pair<int,int>	PI;

string s1="welcome to code jam",s2;
int dp[50][1000];

int solve(int index1,int index2){
	if(dp[index1][index2]!=-1)return dp[index1][index2];
	if(index1==(int)s1.length())return 1;
	if(index2==(int)s2.length())return 0;
	int ret=0;
	FOR(i,index2,s2.length()){
		if(s2[i]==s1[index1]){
			ret+=solve(index1+1,i+1);
		}
	}
	return ret%MOD;
}

int main(){
	int t;
	scanf("%d\n",&t);
	FOR(cas,1,t+1){
		memset(dp,-1,sizeof(dp));
		getline(cin,s2);
		cout<<"Case #"<<cas<<": ";
		printf("%04d\n",solve(0,0));
	}
	return 0;
}
