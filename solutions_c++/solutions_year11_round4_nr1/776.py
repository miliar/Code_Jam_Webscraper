#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define MAX 1005

using namespace std;

typedef double dou;

struct pista{
	double b, e, w;
	pista(){}
	pista(double bb, double ee, double ww){
		b = bb;
		e = ee;
		w = ww;
	}
};

bool operator < (const pista &a, const pista &b){
	if (a.w == b.w)
		return (a.e - a.b) > (b.e - b.b);
	return a.w < b.w;
}

dou X, S, R, t;
int N;
pista p[MAX];

int main(){
	int T;
	scanf ("%d", &T);
	for (int cas = 1; cas <= T; cas++){
		scanf ("%lf %lf %lf %lf %d", &X, &S, &R, &t, &N);
		dou walk = X;
		for (int i = 0; i < N; i++){
			scanf ("%lf %lf %lf", &p[i].b, &p[i].e, &p[i].w);
			walk -= (p[i].e - p[i].b);
		}
		sort(p, p + N);
		dou ds = t*R;
		printf ("Case #%d: ", cas);
		dou resp = 0.0;
		if (ds <= walk){
			resp += t;
			t = 0.0;
			walk -= ds;
			resp += walk / S;
		}
		else{
			resp += walk/R;
			t -= walk/R;
		}
		for (int i = 0; i < N; i++){
			ds = t*(R + p[i].w);
			dou dist = p[i].e - p[i].b;
			if (ds <= dist){
				resp += t;
				t = 0.0;
				dist -= ds;
				resp += dist/(S+p[i].w);
			}
			else{
				resp += dist/(R+p[i].w);
				t -= dist/(R+p[i].w);
			}
		}
		printf ("%.7f\n", resp);
	}
	return 0;
}
