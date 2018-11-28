#include <iostream>

using namespace std;

int main(){
	//FILE *stream ;
	//if((stream = freopen("botTrust.txt", "w", stdout)) == NULL)
    //  exit(-1);

	int cases;
	int steps;
	
	char botColor;
	int botMove;

	int posO;
	int posB;
	int timeLapse;
	int total;
	char lastBot;

	cin >> cases;

	for(int i=0; i<cases; i++){
	
		cin >> steps;
		lastBot='c';
		posO=posB=1;
		timeLapse=total=0;
		int move;

		for(int j=0; j<steps; j++){

			cin >> botColor;
			cin >> botMove;

			if(lastBot=='c'){
				lastBot=botColor;
				timeLapse=0;
			}

			if(botColor=='O'){
				move = abs(botMove-posO)+1;
				if(lastBot=='O'){
					total += move;

					posO=botMove;
					timeLapse+=move;
				}else if(lastBot=='B'){
					if(timeLapse<move){
						total += move-timeLapse;
						timeLapse=move-timeLapse;
					}else{
						total += 1;
						timeLapse=1;
					}

					lastBot='O';
					posO=botMove;
				}
			}else if(botColor=='B'){
				move = abs(botMove-posB)+1;
				if(lastBot=='B'){
					total += move;

					posB=botMove;
					timeLapse+=move;
				}else if(lastBot=='O'){
					if(timeLapse<move){
						total += move-timeLapse;
						timeLapse=move-timeLapse;
					}else{
						total += 1;
						timeLapse=1;
					}

					lastBot='B';
					posB=botMove;
				}
			}
			//cout << "total: "<< total << ", timeLapse: "<< timeLapse << endl;

		}

		cout << "Case #" << i+1 << ": " << total << endl;
	}

	return 0;
}