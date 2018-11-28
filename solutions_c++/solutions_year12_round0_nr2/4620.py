#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;

int tt[105];
int score[105][3];

int main(){
	int T, total;
	cin>>T;
	for(int i = 0; i<T; i++){
		int N, S, p, cnt = 0;

		cin>>N>>S>>p;		
		
		for(int j = 0; j<N; j++)
			cin>>tt[j];
		
		sort(tt, tt+N, greater<int>());

		for(int j = 0; j<N; j++){
			int dv = tt[j] / 3;
			int rm = tt[j] % 3;
			int add[3];

			if(dv == 0 && rm == 0) {
				score[j][0] = score[j][1] = score[j][2] = dv;
			}else if(dv == 10 && rm == 0){
				score[j][0] = score[j][1] = score[j][2] = dv;
			}else if(dv == 9 && rm == 2){
				score[j][0] = dv - 1;
				score[j][1] = dv + 1;
				score[j][2] = dv + 1;
			}else if(rm == 0){
				score[j][0] = dv;
				score[j][1] = dv;
				score[j][2] = dv;
				if(S!=0 && score[j][2] < p){
					score[j][0] = dv-1;
					score[j][1] = dv;
					score[j][2] = dv+1;
					S--;
				}
			}else if(rm == 1){
				score[j][0] = dv;
				score[j][1] = dv;
				score[j][2] = dv + 1;
				if(S!=0 && score[j][2] < p){
					score[j][0] = dv-1;
					score[j][1] = dv + 1;
					score[j][2] = dv+1;
					S--;
				}
			}else if(rm == 2){
				score[j][0] = dv;
				score[j][1] = dv+1;
				score[j][2] = dv+1;
				if(S!=0 && score[j][2] < p){
					score[j][0] = dv;
					score[j][1] = dv;
					score[j][2] = dv+2;
					S--;
				}
			}
		
			for(int k = 0; k<3; k++){
			//	cout<<score[j][k]<<" ";
			}
			//cout<<endl;

			if(score[j][2] >= p) cnt++;
					
		}

		cout<<"Case #"<<i+1<<": "<<cnt<<endl;

	}
	return 0;
}