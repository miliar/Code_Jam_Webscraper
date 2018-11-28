#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <ctime>

#define ln printf("\n")
#define rep(a,b) for(int a = 0; a < b; a++)

using namespace std;
#define ll long long

ll r[1111];
ll cy[1111];
ll cx[1111];
int n;
int size;

bool colide(int pos, ll y, ll x){
	rep(i,size){
		if( (y-cy[i])*(y-cy[i]) + (x-cx[i])*(x-cx[i]) < r[pos]*r[pos] + 2*r[i]*r[pos] + r[i]*r[i] ) return true;
	}
	return false;
}
int w, l;

bool read(){
	scanf("%d%d%d", &n, &w, &l);
	rep(i,n) scanf("%d", &r[i]);
	/*
	n = 1000;
	
	double area = 0;
	
	rep(i,n){
		unsigned int lol = (rand()<<16)+rand();
		lol %= 100000;
		r[i] = lol;
		area += acos(-1)*lol*lol;
	//	printf("%d %lf\n", lol, area);
	}
	
	ll tot = 5*area+1;
	w = (int) sqrt(tot+1);
	l = (int) sqrt(tot+1);
	
	//printf("%lld %d %d\n", tot, w, l);
	//*/
	return true;	
}

int cn = 1;

void process(){
	printf("Case #%d:", cn++);
	size = 0;
	int tries = 0;
	int maxtries = 1000;
	
	while(size < n){
		tries++;
		if(tries > maxtries){
			tries = 0;
			size = 0;
		}
		unsigned int y = (rand()<<16)+rand();
		unsigned int x = (rand()<<16)+rand();
		y %= w;
		x %= l;
				
		//printf("Trying %d %d\n", y, x);		
						
		if(colide(size, y, x) == false){
			cy[size] = y;
			cx[size] = x;
			size++;
			tries = 0;
		}
	}
	
	rep(i,n){
		if(cx[i] > l || cy[i] > w) printf("dim\n");
		rep(j,n){
			if(j != i){
				if( (cy[i]-cy[j])*(cy[i]-cy[j]) + (cx[i]-cx[j])*(cx[i]-cx[j]) < r[i]*r[i] + 2*r[i]*r[j] + r[j]*r[j] ) printf("Fail\n");
			}
		}
	}
	
	rep(i,n){
		printf(" %lld %lld", cy[i], cx[i]);
	}
	ln;
}

int main(){
	srand(time(NULL));
	freopen("a.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t = -1;
	scanf("%d", &t);
	while(t-- && read()) process();
	
	//while(1);
	return 0;
}
