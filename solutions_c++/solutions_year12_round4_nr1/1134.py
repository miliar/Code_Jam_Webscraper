#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

typedef struct Vine {
	int d, l;
	
	int lmin;
} Vine;

int N, D;
vector<Vine> v;

bool is_possible(int m, int l){
	int dmax = v[m].d + l;
	
	if(l <= 0)
		return false;
	
	if(dmax >= D)
		return true;
	
	for(int n=m+1; n<N && dmax >= v[n].d; n++)
		if(is_possible(n, min(v[n].l, v[n].d - v[m].d)))
			return true;
	
	return false;
}

int main(void){
	int T;
	cin >> T;
	
	for(int t=1; t<=T; t++){
		cin >> N;
		
		v.resize(N);
		for(int n=0; n<N; n++){
			cin >> v[n].d >> v[n].l;
		}
		
		cin >> D;
		
		for(int n=0; n<N; n++){
			v[n].lmin = D+100;
		}
		
		for(int n=N-1; n>=0; n--){
			if(v[n].d + v[n].l >= D)
				v[n].lmin = D - v[n].d;
			
			for(int m=n+1; m<N; m++){
				int lmin = D+1;
				
				if(v[m].d - v[n].d >= v[m].lmin)
					lmin = v[m].d - v[n].d;
					
				if(lmin < v[n].lmin && lmin <= v[n].l)
					v[n].lmin = lmin;
			}
		}
		
		if(v[0].lmin <= v[0].d)
			cout << "Case #" << t << ": YES" << endl;
		else
			cout << "Case #" << t << ": NO" << endl;
	}
	
	return 0;
}
