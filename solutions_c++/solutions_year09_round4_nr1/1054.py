#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <cstring>
#define FOR(i,a,n) for(int i=a;i<=n;i++)
#define REP(i,n) for(int i=0;i<n;i++)
#define FORD(i,n,a) for(int i=n;i>=a;i--)
#define PB push_back
#define MP make_pair
#define xx first
#define yy second
#define vi vector<int>
#define pi pair<int,int>
using namespace std;
const int R=50;
int last[R];
bool bylo[R];
int fun(int a,int n){
	//printf("%d %d ",a,n);
	int cnt=0;
	FOR(i,1,n){
		if(bylo[i])
			cnt++;
		if(!bylo[i] && last[i]<=a){
			bylo[i]=1;
			int poz=i-1+a-cnt;
			//printf("%d: %d\n",i,max(poz,a)-min(poz,a));
			return (max(poz,a)-min(poz,a));
		}
	}
	return 0;
}
			
	

int solve(void){
	int n;
	char c='0';
	memset(bylo,0,sizeof(bylo));
	memset(last,0,sizeof(last));
	scanf("%d ",&n);
	FOR(i,1,n){
		FOR(j,1,n){
			scanf("%c",&c);
			if(c=='1')
				last[i]=max(last[i],j);
		}
		scanf("%c",&c);
	}
	int sum=0;
	FOR(i,1,n)
		sum+=fun(i,n);
	return sum;
}
int main(){
	int t;
	scanf("%d ",&t);
	REP(i,t)
		printf("Case #%d: %d\n",i+1,solve());
	return 0;
}
