#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <map>

using namespace std;
int main(int argc, char ** argv){
	ifstream fin(argv[1]);
	int T;
	fin >> T;
	
	for (int t=0; t!= T; t++){
		int N;
		fin >> N;
		
		int y=0;
		char lastrobot = 'X';
		int lastmoves = 0;
		
		int bpos = 1;
		int opos = 1;
		
		for (int n=0; n!= N; n++){
			char R;
			int P;
			fin >> R >> P;
			
			//how far to move
			int dist = 0;
			if (R == 'B'){
				dist = abs(P-bpos); 
			} else {
				dist = abs(P-opos); 
			}

			if (lastrobot == R) {
				lastmoves += dist + 1;
				y += dist + 1;				
			} else {
				lastrobot = R;
				if (lastmoves > dist) {
					y += 1;
					lastmoves = 1;
				} else {
					y += dist - lastmoves + 1;
					lastmoves = dist - lastmoves + 1;
				}

			}
			//Set the robots position
			if (R == 'B'){
				bpos = P; 
			} else {
				opos = P; 
			}	
			//cout << opos << " " << bpos << " " << lastrobot << " " << lastmoves << " " << y << endl;
		}
		cout << "Case #" << t+1 << ": " << y << endl;

	}
	return 0;
}