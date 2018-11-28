#include <iostream>
#include <algorithm>
#include <map>
#include <sstream>
#include <vector>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
#define sz(x) (int)(x).size()
#define pb push_back
#define clr(x) (x).clear()
#define all(x) (x).begin(), (x).end()

int tn, cc;
int N, M, A;
bool ok;
int x[4], y[4];
void input() {
	cin >> N >> M >> A;
}

void solve() {
	ok = false;
	int i;
	x[0] = 0;
	y[0] = 0;
	for(x[1]=0;x[1]<=N;++x[1])
	for(y[1]=0;y[1]<=M;++y[1])
	for(x[2]=0;x[2]<=N;++x[2])
	for(y[2]=0;y[2]<=M;++y[2]) {
		x[3] = x[0];
		y[3] = y[0];
		int a = 0;
		for(i=0;i<=2;++i) a += x[i] * y[i+1];
		for(i=3;i>=1;--i) a -= x[i] * y[i-1];
		a = abs(a);
		if(a==A) {
			ok = true;
			return;
		}
		if(a>A) break;
	}
}

void output() {
	printf("Case #%d: ", cc);
	if(!ok) {
		printf("IMPOSSIBLE");
	}
	else {
		int i;
		for(i=0;i<3;++i) {
			cout << x[i] << " " << y[i] << " ";
		}
	}
	printf("\n");
}

int main() {
	cin >> tn;
	for(cc=1;cc<=tn;++cc) {
		input();
		solve();
		output();
	}
}

