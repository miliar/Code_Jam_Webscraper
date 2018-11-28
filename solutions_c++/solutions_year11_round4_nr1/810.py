#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
#include <cstring>
#include <cmath>

typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned long UL;
typedef unsigned int UI;
typedef unsigned short US;
typedef unsigned char UC;

#define rep(i,a,b) for(int i=a;i<b;i++)

using namespace std;

typedef struct {
	int B, E, W;
} WA;

bool WACmp(const WA& l, const WA& r) {
	return l.W < r.W;
}

int solve(int no)
{
	int X;
	double T;
	int S, R, N;
	cin >> X >> S >> R >> T >> N;
	
	WA W[1010];
	double x = X;
	rep(i, 0, N) {
		cin >> W[i].B >> W[i].E >> W[i].W;
		x -= W[i].E-W[i].B;
	}
	
	sort(W, W+N, WACmp);
	
	double t = 0;
	
	if(T*R>=x) {
		t = x / R;
		T -= t;
	} else {
		t = T + (x-T*R)/S;
		T = 0;
	}
	
	rep(i, 0, N) {
		double len = W[i].E - W[i].B;
		int w = S + W[i].W;
		if(T>0) w = R+W[i].W;
		double dt = (double)len / w;
		if(T>0) {
			if(T>=dt) {
				T -= dt;
			} else {
				len -= T*w;
				dt = T + len / (S+W[i].W);
				T = 0;
			}
		}
		X -= len;
		t += dt;
	}
	
	cout << "Case #" << no << ": ";
	printf("%.7f\n", t);
}

int main()
{
	int T;
	cin >> T;
	rep(no,0,T) {
		solve(no+1);
	}
	return 0;
}
