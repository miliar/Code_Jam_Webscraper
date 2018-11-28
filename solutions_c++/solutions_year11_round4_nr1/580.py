#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct walk{
	int beg, end, speed;
	
	void set (int a, int b, int c){
		beg = a; end = b; speed = c;
	}
};

bool operator < (const walk & w1, const walk & w2){
	return w1.speed < w2.speed;
}

typedef long double lDouble;

int main(){
	int nCases, iCases;
	cin >> nCases;

	for (iCases=1; iCases<=nCases; iCases++){
	
		int totD, S, R, runT, n;
		scanf("%d %d %d %d %d", &totD, &S, &R, &runT, &n);
	
		int i, d = 0, vS, vR;
		vector<walk> walks;
		walk w, w2;
		w.end = 0;
		lDouble total = 0, t, leftT;
		
		for (i=0; i<n; i++){
			scanf("%d %d %d", &w.beg, &w.end, &w.speed);
			
			if (w.beg != d){ // Adicionar uma walkway de velocidade 0
				w2.set(d, w.beg, 0);
				total += lDouble(w.beg-d) / lDouble(S);
				walks.push_back(w2);
			}

			d = w.end;
			total += lDouble(w.end-w.beg) / lDouble(w.speed+S);
			walks.push_back(w);
		}
		
		if (w.end != totD){ // Adicionar uma walkway de velocidade 0
			w2.set(w.end, totD, 0);
			total += lDouble(totD-w.end) / lDouble(S);
			walks.push_back(w2);
		}
		
		sort (walks.begin(), walks.end());
		
		//printf("%.12lf\n", double(total));
	
		i = 0;
		leftT = runT;
		n = int(walks.size());
		while (leftT>0 and i<n){
			d = walks[i].end - walks[i].beg;
			vR = walks[i].speed + R;
			t = lDouble(d)/vR;
			
			//printf("%d %lf %lf\n", walks[i].beg, double(t), double(leftT));
			
			if (t > leftT){
				t = leftT;
				leftT = 0;
			}
			else {
				leftT -= t;
			}
			
			vS = walks[i].speed + S;
			
			total -= lDouble(vR)*t*(R-S)/(vS*vR);
			i++;
		}

		printf("Case #%d: ", iCases);
		printf("%.12lf\n", double(total));
	}
	
	return 0;
}
