#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

/* int abs(int x){
	return (x>0)? x: -x; 
} */



int main(){
	int T;
	int N;
	int R, P;
	char c;
	int pos[2];
	int time[2];

	cin >> T;
	for (int cnt=1; cnt<=T; cnt++){
		cin >> N;
		pos[0] = 1;
		pos[1] = 1;
		time[0] = 0;
		time[1] = 0;
		int current_time = 0;
		for (int i=0; i<N; ++i){
			cin >> c >> P;
			if (c=='O'){
				R = 0;
			} else {
				R = 1;
			}
			current_time += max(abs(pos[R]-P)-(current_time-time[R]),0)+1;
//			cout << current_time << " " << i << endl;
			pos[R] = P;
			time[R] = current_time;
		}
		cout << "Case #" << cnt << ": ";
		cout << current_time;
		cout << endl;
	}
	


	return 0;
}
