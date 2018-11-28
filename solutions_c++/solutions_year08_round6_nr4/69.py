#include <vector>
#include <list>
#include <map>
#include <set>
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

#define eps 1e-8
#define PI 3.14159265358979323846
#define push_back(a) pb(a)
typedef long long ll;

bool g[100][100];
bool g2[100][100];
bool v[10];
int n,m;
int a[10];
bool yes;
void getac(int d, int u){
	int i,j;
	if(u==m){
		bool ok=1;

		for(i=0;i<m;i++){
			for(j=0;j<m;j++){
				if(g2[i][j] && g[a[i]][a[j]] || !g2[i][j] && !g[a[i]][a[j]]){
				}else{
					ok=0;
					break;
				}
			}
		}
		if(ok){
			yes=1;
		}
	}else{
		if(d==n) return;
		for(i=0;i<n;i++){
			if(!v[i]){
				v[i]=1;
				a[u]=i;
				getac(d+1,u+1);
				if(yes) return;
				v[i]=0;
			}
		}
	}
}

int main(){
	int T,TT;
	scanf("%d",&T);
	for(TT=1;TT<=T;TT++){
		int i,j,k;
		int a,b;
		memset(g,0,sizeof(g));
		memset(g2,0,sizeof(g2));
		scanf("%d",&n);
		for(i=1;i<n;i++){
			scanf("%d%d",&a,&b);
			a--;b--;
			g[a][b]=1;
			g[b][a]=1;
		}
		scanf("%d",&m);
		for(i=1;i<m;i++){
			scanf("%d%d",&a,&b);
			a--;b--;
			g2[a][b]=1;
			g2[b][a]=1;
		}
		memset(v,0,sizeof(v));
		yes=0;
		getac(0,0);
		printf("Case #%d: ",TT);
		if(yes){
			printf("YES\n");
			
		}else{
			printf("NO\n");
		}
		fflush(stdout);
	}
}
