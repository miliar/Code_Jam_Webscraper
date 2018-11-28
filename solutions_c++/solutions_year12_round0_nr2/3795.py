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

int r[1111];
int n, s, p;

bool read(){
	scanf("%d%d%d", &n, &s, &p);
	
	rep(i,n) scanf("%d", &r[i]);
	
	return true;
}

int cn = 1;

int calc(int x){
	int trip = 0;
	int regular = 0;
	
	rep(i,11){
		rep(j,11){
			int k = x-j-i;
			if(k >= 0 && k <= 10){
				int lo = min(i,j);
				lo = min(lo,k);
				int hi = max(i,j);
				hi = max(hi,k);
				int ab = hi-lo;
				if(hi >= p){
					if(ab == 2) trip = 1;
					else if(ab == 0 || ab == 1) regular = 2; 
				}
			}
		}
	}
	
	return trip + regular;
}

void process(){
	printf("Case #%d: ", cn++);
	
	int trip = 0;
	int both = 0;
	int regular = 0;
	
	rep(i,n){
		int temp = calc(r[i]);
		if(temp == 3) both++;
		else if(temp == 2) regular++;
		else if(temp == 1) trip++;
	}
	
//	printf("%d %d %d\n", trip, both, regular);
	
	int res = 0;
	int take = min(trip, s);
	res += take;
	s -= take;
	take = min(s, both);
	both -= take;
	res += take;
	res += regular + both;
	printf("%d\n", res);
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
