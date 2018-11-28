#include <fstream>
#include <iostream>

using namespace std;

char getstart(string s){
	for(int i = 0; i < 4; i++){
		if(s[i] != 'T' && s[i] != '.')
			return s[i];
	}
	return 0;
}

//0 - x, 1 - y, 2 - draw, 3 - notodone

int state(string s, char start){
	bool draw = 0;
	for(int i = 0; i < 4; i++){
		if(s[i] != start){
			if(s[i] == '.')	return 3;
			else if(s[i] != 'T')	draw = 1;
		} 
		if(i == 3)	if(draw)	return 2;
		else	return start == 'X' ? 0 : 1;
	}
}

main(){
	ifstream fin ("a.in");
	ofstream fout ("a.txt");
	
	int T;
	string B[4];
	
	fin >> T;

	for(int i = 1; i <= T; i++){
		fout << "Case #" << i;
		for(int j = 0; j < 4; j++){
			fin >> B[j];
		}
		
		bool notdone = 0, x = 0, y = 0, draw = 0;
		
		for(int m = 0; m < 4; m++){
			char start = getstart(B[m]);
			if(start != 0){
				int statenum = state(B[m], start);
				switch(statenum){
					case 0: x = 1; break;
					case 1: y = 1; break;
					case 2: draw = 1; break;
					case 3: notdone = 1; break;
				}
			}
			if(x || y)	break;
		}
	
		if(!(x || y))	
		for(int m = 0; m < 4; m++){
			char start;
			string temp;
			for(int n = 0; n < 4; n++)
				temp += B[n][m];
			start = getstart(temp);
			if(start != 0){
				int statenum = state(temp, start);
				switch(statenum){
					case 0: x = 1; break;
					case 1: y = 1; break;
					case 2: draw = 1; break;
					case 3: notdone = 1; break;
				}
			}
			if(x || y)	break;
		}
		
		if(!(x || y)){
			string temp, temp1;
			for(int m = 0; m < 4; m++){
				temp += B[m][m];
				temp1 += B[m][3-m];
			}
			char start = getstart(temp);
			if(start != 0){
				int statenum = state(temp, start);
				switch(statenum){
					case 0: x = 1; break;
					case 1: y = 1; break;
					case 2: draw = 1; break;
					case 3: notdone = 1; break;
				}
			}
			if(!(x || y)){
				start = getstart(temp1);
				if(start != 0){
					int statenum = state(temp1, start);
					switch(statenum){
						case 0: x = 1; break;
						case 1: y = 1; break;
						case 2: draw = 1; break;
						case 3: notdone = 1; break;
					}
				}
			}
		}					

		if(!x && !y && !draw)	notdone = 1;
		if(x)	fout << ": X won\n";
		else if(y)	fout << ": O won\n";
		else if(draw)	fout << ": Draw\n";
		else if(notdone)	fout << ": Game has not completed\n";
	}

	return 0;
}
