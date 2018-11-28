#include <stdio.h>
#include <string.h>
#include <string>
#include <map>

using namespace std;

const int maxn = 110;
const int maxq = 1100;


string q[maxq];
int n,m;

map<string,int> id;
int dp[maxq][maxn];
bool was[maxq][maxn];
#define nul(a) memset(a,0,sizeof(a))

void init(){
	id.clear();
	scanf("%d\n",&n);
	nul(was);
	int i;
	char *s = new char[110];

	for (i = 0 ; i<n ; i++){
		gets(s);
		string t = s;
		id[t] = i;
	}
	scanf("%d\n",&m);
	for (i = 0 ; i<m ; i++){
		gets(s);
		q[i] = s;
	}
}

int rec(int pos, int num){
	if (was[pos][num]){
		return dp[pos][num];
	}
	was[pos][num] = true;
	if (pos==m){
		return dp[pos][num] = 0;
	}
	int i;
	bool can = true;
	int numpos = id[q[pos]];
	if (numpos==num){
		can = false;
	}
	int res = 1000000000;
	for (i = 0 ; i<n ; i++){
		if (i==num && can){
			res = min(res,rec(pos+1,num));
		} else{
			if (i!=numpos){
				res = min(res,1+rec(pos+1,i));
			}
		}
	}
	return dp[pos][num] = res;
}

void solve(){
	int res = 1000000;
	int i;
	for (i = 0 ; i<n ; i++){
		res = min(res,rec(0,i));
	}
	printf("%d",res);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int i;
	for (i = 1 ; i<=t ; i++){
		printf("Case #%d: ",i);
		init();
		solve();
		printf("\n");
	}
	return 0;
}