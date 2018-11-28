#include <iostream>
#include <iomanip>

using namespace std;

typedef long double ld;

const int MaxN= 100000 + 10, MaxX= 1000000 + 100;
const ld eps= 1e-7;
struct walkway{
	ld b, e, w;
	
	inline bool operator < (const walkway & second)const{
		return w < second.w;
	}
	
	inline ld tool(){
		return e-b;
	}
		
} w[MaxN];
ld x, s, r, t, n;

int main(){
	cout << fixed << setprecision(10);
	ld test;
	cin >> test;
	for (int tc=1 ; tc<=test ; tc++){
		cout << "Case #" << tc << ": ";
		cin >> x >> s >> r >> t >> n;
		int cnt= 0;
		ld back= 0;
		for (int i=0  ; i<n ; i++){
			cin >> w[cnt].b >> w[cnt].e >> w[cnt].w;
			ld now= w[cnt].e;
			cnt++;
			if (w[cnt-1].b > back){
				w[cnt].b= back;
				w[cnt].e= w[cnt-1].b;
				w[cnt].w= 0;
				cnt++;
			}
			back= now;
		}
		if (back<x){
			w[cnt].b= back;
			w[cnt].e= x;
			w[cnt].w= 0;
			cnt++;
		}
		sort(w, w+cnt);
		ld res= 0;
		ld tt= t;
		for (int i=0 ; i<cnt ; i++){
			if (tt>eps){
				ld len= w[i].tool();
				if (tt*(w[i].w+r)>len+eps){
					ld now= len/(w[i].w+r);
					tt-= now;
					res+= now;
				}else{
					ld now= tt;
					len-= tt*(w[i].w+r);
					tt-= now;
					res+= now;
					now= len/(w[i].w+s);
					res+= now;
				}
			}else{
				ld len= w[i].tool();
				res+= len/(w[i].w+s);
			}
		}
		cout << res << endl;
	}
	return 0;
}