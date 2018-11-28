#include <iostream>

using namespace std;

struct button{
	int pos;
	int step;
};


int main(){
	int T, N, i, j, k, total;
	char RC, Flag;
	button O, B;

	cin >> T;
	for (i=1; i<=T; i++){
		cin >> N;
		cin >> RC >> k;
		if (RC == 'O'){ 
			O.pos = k;
			O.step = k;
			Flag = 'O';
			B.pos = 1;
			B.step = 0;
		}
		else{ 
			B.pos=k;
			B.step = k;
			Flag = 'B';
			O.pos = 1;
			O.step = 0;
		}

		for (j=1; j<N; j++){
			cin >> RC >> k;
			if (RC == Flag){
				switch (RC){
					case 'O':  
						O.step += abs(k-O.pos)+1;
						O.pos = k;	break;
					case 'B':
						B.step += abs(k-B.pos)+1;
						B.pos = k;	break;
				}
			}
			else{
				switch (RC) {
				case 'O':
					Flag = 'O';
					if (abs(k-O.pos)>(B.step-O.step)){
						O.step += abs(k-O.pos)+1;
						O.pos = k;
					}
					else {
						O.step = B.step+1;
						O.pos = k;
					}	
					break;
				case 'B':
					Flag = 'B';
					if (abs(k-B.pos)>(O.step-B.step)){
						B.step += abs(k-B.pos)+1;
						B.pos = k;
					}
					else {
						B.step = O.step+1;
						B.pos = k;
					}
					break;
				}
			}
		}
		total = O.step>B.step? O.step : B.step;
		printf("Case #%d: %d\n", i, total);

	}

	return 0;
}