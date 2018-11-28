/*
  Problem No : 
  Author     : Debashis Maitra
  Complexity :
  Date       :
*/

#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <ctype.h>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <sstream>

using namespace std;

#define CLR(x) memset((x),0,sizeof(x))
#define pb push_back
#define sz size()
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORALL(i,x) for(int i=0;i<x.size();i++)
#define i64 long long
#define MAX 1000
#define INF 1<<30

typedef vector<int> vi;
typedef vector<string> vs;
char s1[60]="welcome to code jam";
char s2[600];
int memo[600][600];
int l1,l2;
int caseno;

int input(){
	return 1; 
}
int dp(int i,int j){
	if(i>=l1) return 1;
	if(j>=l2)return 0;	
	if(memo[i][j]>=0)return memo[i][j];	
	int &ret=memo[i][j];
	ret=0;
	if(s1[i]==s2[j])ret=dp(i+1,j+1);	
	ret=(ret+dp(i,j+1))%10000;
	return 	ret;
}
void process(){
	 memset(memo,-1,sizeof(memo));
     l1=strlen(s1);
	 l2=strlen(s2);
	 int ret=dp(0,0);
	 printf("Case #%d: %04d\n",++caseno,ret);
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("outputL.txt","w",stdout);
	int cases;
	scanf("%d\n",&cases);
	while(cases--){
		gets(s2);
		process();
	}
}
