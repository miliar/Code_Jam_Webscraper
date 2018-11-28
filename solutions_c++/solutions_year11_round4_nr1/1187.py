#include <stdio.h>
#include <algorithm>

using namespace std;

typedef struct walkway{
	double b,e,s,l;
} walkway;

bool compare( const walkway &a, const walkway &b){
	return a.s < b.s;
}

double eps = 1e-9;
int comp(double a, double b){
	if(a+eps<b)return -1;
	if(b+eps<a)return 1;
	return 0;
}


int T;
int q;
double resp;
double X,S,R,t;
int N;
walkway w[1010];


int main(){
	scanf(" %d", &T);
	for(int q=1; q<=T; q++){
		scanf(" %lf %lf %lf %lf %d", &X, &S, &R, &t, &N);
		for(int i=0; i<N; i++){
			scanf(" %lf %lf %lf", &w[i].b, &w[i].e, &w[i].s);
			w[i].l = w[i].e - w[i].b;
			X -= (w[i].l);
			
		}
		
		//printf("X: %lf %lf\n", X, resp);
		resp = 0;
		double at;
		at = X/(R);
		if(comp(at,t)!= 1){
			t-=at;
			X=0;
			resp+=at;
		}
		else{
			X -= t*R;
			resp+=t;
			t = 0;
		}
		
		//printf("X: %lf %lf\n", X, resp);
		
		if(comp(X,0)==1){
			resp += X/S;
		}
		
		//printf("X: %lf %lf\n", X, resp);
		sort(w,w+N,compare);
		
		for(int i=0; i<N; i++){
			at = w[i].l/(R+w[i].s);
			if(comp(at,t)!= 1){
				t-=at;
				w[i].l=0;
				resp+=at;
			}
			else{
				w[i].l -= t*(w[i].s+R);
				resp+=t;
				t = 0;
			}
		
			if(comp(w[i].l,0)==1){
				resp += w[i].l/(S+w[i].s);
			}
		}
	
		printf("Case #%d: %.9lf\n", q, resp);
	}
	
}
