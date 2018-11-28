#include <iostream>
#include <algorithm>

using namespace std;

int t, n, w, l;

struct pt{
	int r, idx;
	
	bool operator < (const pt& p) const{
		return r > p.r;
	}
};


pt p[1010];

int x[1010];
int y[1010];

void solvew(){
	int px = 0, s = 0, pp = 0, wid = 0;
	
	while(px <= w && pp < n){
		x[p[pp].idx] = px;
		y[p[pp].idx] = 0;
		
		px += p[pp].r;
		if(px > w){
			pp++;
			break;
		}
		px += p[pp].r;
		
		pp++;
	}
	
	wid = p[0].r;
	
	while(pp < n){
		s = pp;
		px = 0;
		while(px <= w && pp < n){
			x[p[pp].idx] = px;
			y[p[pp].idx] = wid + p[pp].r;
			
			px += p[pp].r;
			if(px > w){
				pp++;
				break;
			}
			px += p[pp].r; 
			
			pp++;
		}
		
		wid += 2*p[pp].r;
	}
}

void solve(){
	if(w > l) solvew();
	else{
		swap(w, l);
		solvew();
		
		for(int i = 0; i < n; i++)
			swap(x[i], y[i]);
	}
}
	
int main(){
	cin >> t;
	
	for(int tc = 1; tc <= t; tc++){
		cin >> n >> w >> l;
		
		for(int i = 0; i < n; i++){
			cin >> p[i].r;			
			p[i].idx = i;
		}		
		sort(p, p+n);
		
		solve();
		
		
		cout << "Case #" << tc << ":";
		
		for(int i = 0; i < n; i++){
			cout << " " << x[i] << " " << y[i];
		}
		cout << "\n";
	}
}
