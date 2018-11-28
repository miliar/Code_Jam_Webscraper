#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <iostream>

#define ln printf("\n")
#define mp make_pair
#define pii pair<int,int>
#define a first
#define b second

using namespace std;

const int inf = 0x7f7f7f7f;
const double pi=acos(-1.0);
const double eps = 1e-8;

int x, s, run, n;
double t;

struct walk{
	int a, b, s;
	walk(int a, int b, int s): a(a), b(b), s(s){}
	walk(){}
	bool operator < (const walk & b) const{
		return s < b.s;
	}
	
	void print(){
		printf("%d %d %d\n", a, b, s);
	}
};

pii f[1010];
int s1[1010];
walk r[3030];

bool read(){
	scanf("%d%d%d%lf%d", &x, &s, &run, &t, &n);
//	printf("Lendo\n");
	for(int i = 0; i < n; i++){
		scanf("%d%d%d", &f[i].a, &f[i].b, &s1[i]);
	}
	
	return true;
}

int cn = 1;

double cost(walk v){
	double res = 0;
	
	double dist = v.b-v.a;
	double speed = v.s+run;
	double time = dist/(speed);
	double cantake;
	if(time < t){
		cantake = time;
		t-=time;
	}else{
		cantake = t;
		t = 0;
	}
	
	time = cantake;
	dist -= cantake*(v.s+run);
	time += dist/(v.s+s);
	
	//printf("Walk(%d,%d,%d) = %lf\n",v.a, v.b, v.s, time);
	return time;
}

void process(){
	printf("Case #%d: ", cn++);

	sort(f, f+n);
	
	int m = 0;
	r[m++] = walk(0,f[0].a, 0);
	//r[m-1].print();
	for(int i = 0; i < n; i++){
		r[m++] = walk(f[i].a, f[i].b, s1[i]);
		//r[m-1].print();
		
		if(i < n-1){
			r[m++] = walk(f[i].b, f[i+1].a, 0);
		//	r[m-1].print();
		}
	}	
	
	r[m++] = walk(f[n-1].b, x, 0);
	//r[m-1].print();	
	
	sort(r, r+m);
	
	double res = 0;
	
	for(int i = 0; i < m; i++){
		res += cost(r[i]);
	}
	
	printf("%.12lf\n", res);
}

int main(){
	freopen("a.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cases; scanf("%d", &cases);
		
	
	while(cases-- && /**/ read()){		
		process();
	}
	
	//while(1);
	
	return 0;
}
