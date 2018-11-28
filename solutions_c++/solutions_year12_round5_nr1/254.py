#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <map>

#define ln printf("\n")
#define rep(a,b) for(int a = 0; a < b; a++)

using namespace std;

int n;
int l[1111];
int p[1111];

struct frac{
	int a, b, ind;
	
	bool operator < (const frac & x) const{
		if(b == x.b) return ind < x.ind;
		return b < x.b;
		//if(a*x.b == x.a*b) return ind < x.ind;
		//return a*x.b > x.a*b;
	}
} r[1111];

bool read(){
	scanf("%d", &n);
	
	rep(i,n){
		scanf("%d", &l[i]);
	}
	
	rep(i,n){
		scanf("%d", &p[i]);
		p[i] = 100-p[i];
	}
	
	
	rep(i,n){
		r[i].a = l[i];
		r[i].b = p[i];
		r[i].ind = i;
	}
	return true;
}

int cn = 1;

void process(){
	printf("Case #%d:", cn++);
	
	sort(r, r+n);
	
	rep(i,n){
		printf(" %d", r[i].ind);
	}
	printf("\n");
	
	rep(i,n){
		//printf("%d/%d ", r[i].a, r[i].b);
	}
//	printf("\n");
}

int main(){
	freopen("a.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t = -1;
	scanf("%d", &t);
	while(t-- && read()) process();
	
	//while(1);
	return 0;
}
