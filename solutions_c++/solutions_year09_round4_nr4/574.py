#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define dbg(x) cout << #x << " == " << x << endl
#define print(x) cout << x << endl

int r[100];
int x[100];
int y[100];
int n;

int read() {
	scanf("%d",&n);
	for(int i = 0; i < n; i++) {
		scanf("%d %d %d",&x[i],&y[i],&r[i]);
	}
	return 0;
}

int casos = 1;

void process() {
	double raio = 0.0;
	if(n == 1) {
		raio = r[0];
	}
	else if(n == 2) {
		raio = max(r[0],r[1]);
	}
	else {
		raio = 1e10;
		
		double d;
		
		d = pow(x[0]-x[1],2.0) + pow(y[0]-y[1],2.0);
		d = sqrt(d);
		d += r[0] + r[1];
		d /= 2;
		d = max(d,r[2]*1.0);
		raio = min(raio,d);
		

		d = pow(x[1]-x[2],2.0) + pow(y[1]-y[2],2.0);
		d = sqrt(d);
		d += r[1] + r[2];
		d /= 2;
		d = max(d,r[0]*1.0);
		raio = min(raio,d);
		

		d = pow(x[0]-x[2],2.0) + pow(y[0]-y[2],2.0);
		d = sqrt(d);
		d += r[0] + r[2];
		d /= 2;
		d = max(d,r[1]*1.0);
		raio = min(raio,d);
	}
	
	printf("Case #%d: %lf\n",casos++,raio);
}

int main() {

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
		
	int t;
	scanf("%d",&t);
	while(t--) {
		read();
		process();
	}
	
	return 0;
}
