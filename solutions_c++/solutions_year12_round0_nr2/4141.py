#include <iostream>
#include <vector>
using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t=1;t<=T;t++){
		int N, S, P;
		cin >> N >> S >> P;

		vector <int> score(N, 0);
		for(int i=0;i<N;i++)cin >> score[i];

		int cnt = 0;
		int scnt = 0;
		for(int i=0;i<N;i++){
			int sup, nor;
			int base = score[i]/3;

			if(score[i]==0){
				sup = 0;
				nor = 0;
			}
			else if(score[i]%3==2){
				sup = base+2;
				nor = base+1;
			}
			else if(score[i]%3==1){
				sup = base+1;
				nor = base+1;
			}
			else{
				sup = base+1;
				nor = base;
			}

			if(nor >= P)	cnt++;
			else{
				if(sup >= P)	scnt++;
			}
		}
		if(S <= scnt)	scnt = S;
		cnt += scnt;
		cout << "Case #" << t << ": " << cnt << endl;
	}
}