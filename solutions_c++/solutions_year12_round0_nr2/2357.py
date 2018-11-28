#include <iostream>
#include <algorithm>
using namespace std;

typedef struct {
	int normal;
	int surprising;
} Scores;

bool comparar(const Scores& x, const Scores& y){
	return (x.normal > y.normal);
}

int main(){
	int T, N, S, p, ti, i, j, score, rest, total;
	Scores googlers[102];
	cin >> T;
	for(i = 1; i <= T; i++){
		cin >> N >> S >> p;
		total = 0;
		for(j = 0; j < N; j++){
			cin >> ti;
			score = ti/3;
			rest = ti%3;
			if(rest == 0){
				googlers[j].normal = score;
				if(score != 0)
					googlers[j].surprising= score+1;
				else
					googlers[j].surprising = 0;
			}else if(rest == 1){
				googlers[j].normal = score+1;
				googlers[j].surprising = score+1;
			}else{
				googlers[j].normal = score+1;
				googlers[j].surprising = score+2;
			}
		}
		sort(googlers, &googlers[N], comparar);
		for(j = 0; j < N; j++){
			//cout << googlers[j].normal << endl;
			if(googlers[j].normal >= p){
				total += 1;
				//cout << "	+1" << endl;
			}else{
				//cout << "	" << googlers[j].surprising << endl;
				if((googlers[j].surprising >= p) && (S > 0)){
					//cout << "		+1" << endl;
					total += 1;
					S -= 1;
				}
			}
		}

		cout << "Case #" << i << ": " << total << endl;
	}
	return 0;
}
