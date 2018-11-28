#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

const int maxn = 10000;
const int INF = 1000000000;
const double eps = 1e-10;

#define nul(a) memset(a,0,sizeof(a))
#define fill(a,b) memset(a,b,sizeof(a))
#define sqr(a) ((a)*(a))

struct tp{
	int x,y;
	tp(int _x = 0, int _y = 0){
		x = _x;
		y = _y;
	}
	tp operator +(tp a){
		return tp(x+a.x,y+a.y);
	}
	tp operator -(tp a){
		return tp(x-a.x,y-a.y);
	}
	tp operator *(int k){
		return tp(x*k,y*k);
	}
	tp operator /(int k){
		return tp(x/k,y/k);
	}
	int operator *(tp a){
		return x*a.y-y*a.x;
	}
	void print(){
		printf("%d %d ",x,y);
	}
	void get(){
		scanf("%d%d",&x,&y);
	}
};


int n,m,a;

void init(){
	scanf("%d%d%d",&n,&m,&a);
}

void solve(){
	int i,j,k,t;
	for (i = 0 ; i<=n ; i++){
		for (j = 0 ; j<=m ; j++){
			tp p1(i,j);
			for (k = 0 ; k<=n ; k++){
				for(t = 0 ; t<=m ; t++){
					tp p2(k,t);
					int val = p1*p2;
					if (val==a){
						printf("0 0 ");
						p1.print();
						p2.print();
						return;
					}
				}
			}
		}
	}
	printf("IMPOSSIBLE");
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i;
	scanf("%d",&t);
	for (i = 0 ; i<t ; i++){
		printf("Case #%d: ",i+1);
		init();
		solve();
		printf("\n");
	}
	return 0;
}