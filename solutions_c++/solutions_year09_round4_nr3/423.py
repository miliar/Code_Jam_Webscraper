 #include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>


using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)

int n,m;
vector<int> a[110];


bool compareab(const vector<int> &a, const vector<int> &b){
	int i;
	rep(i,m) if (a[i]!=b[i]) {
		if (a[i]<b[i]) return true;
		else return false;
	}
	return false;
}

bool have[110];

bool check(const vector<int> &a, const vector<int> &b) {
	int i;
	rep(i,m) if (a[i]>=b[i]) return false;
	return true;
}

int tot;
int num[110];
int ans;

bool g[110][110];
void dfs(int deep) {
	if (tot>=ans) return;
	if (deep>n) {
		if (tot<ans) ans=tot;
		return;
	}
	int i,j,k;
	foru(i,1,tot) if (g[num[i]][deep]){
		j=num[i];
		num[i]=deep;
		dfs(deep+1);
		num[i]=j;
	}
	tot++;
	num[tot]=deep;
	dfs(deep+1);
	tot--;
}

int main(){
    freopen("c2.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,test,cases;
	scanf("%d",&test);
	cases=0;
    while (test){
		test--;
		cases++;
		scanf("%d%d",&n,&m);
		printf("Case #%d: ",cases);
		foru(i,1,n) {
			a[i].clear();
		  foru(j,1,m) {
				scanf("%d",&k);
				a[i].push_back(k);
			}
		}
		sort(a+1,a+n+1,compareab);
		memset(g,0,sizeof(g));
		
		foru(i,1,n)
		  foru(j,1,n) if (check(a[i],a[j])) g[i][j]=true;
		  else g[i][j]=false;
		  
		memset(have,0,sizeof(have));
		tot=0;
		ans=n;
		dfs(1);
		printf("%d\n",ans);
		
		
	}
     return 0;
}
    
