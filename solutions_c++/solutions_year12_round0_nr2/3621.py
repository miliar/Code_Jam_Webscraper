#include <iostream>

using namespace std;

int main(void){
	int T;
	cin >> T;

	for(int t=1; t<=T; t++){
		int N, S, p;
		cin >> N >> S >> p;
		
		int y = 0;
		for(int n=0; n<N; n++){
			int score;
			cin >> score;
			
			int max_normal = (score+2)/3;

			if(max_normal >= p){
				y++;
			}else if(score >= 2 && S > 0 && score%3 != 1 && max_normal >= p-1 ){
				y++;
				S--;
			}
		}
		
		cout << "Case #" << t << ": " << y << endl;
	}

	return 0;
}
