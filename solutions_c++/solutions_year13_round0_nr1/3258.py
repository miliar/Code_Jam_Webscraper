#include <iostream>
#include <algorithm>

using namespace std;

bool isOwin();
bool isXwin();
bool isEnd();
char map[4][4];


int main(){
	int n;
	cin >> n;
	for(int i = 0; i < n; i++){
		
		for(int j = 0; j < 4; j++){
			cin >> map[j];
		}
		
		if(isOwin()){
			cout << "Case #" << i+1 << ": " << "O won" << endl;
			continue;
		}
		
		if(isXwin()){
			cout << "Case #" << i+1 << ": " << "X won" << endl;
			continue;
		}
		
		if(isEnd()){
			cout << "Case #" << i+1 << ": " << "Draw" << endl;
			continue;
		}
		
		cout << "Case #" << i+1 << ": " << "Game has not completed" << endl;
	}
	
	return 0;
}


bool isOwin(){
	int count = 0;
	for(int i = 0; i < 4; i++){
		if(map[0][i] == 'O' || map[0][i] == 'T') count++;
	}
	if(count == 4) return true;
	
	count = 0;
	for(int i = 0; i < 4; i++){
		if(map[i][0] == 'O' || map[i][0] == 'T') count++;
	}
	if(count == 4) return true;
	
	count = 0;
	for(int i = 0; i < 4; i++){
		if(map[i][i] == 'O' || map[i][i] == 'T') count++;
	}
	if(count == 4) return true;

	count = 0;
	for(int i = 0; i < 4; i++){
		if(map[i][3 - i] == 'O' || map[i][3 - i] == 'T') count++;
	}
	if(count == 4) return true;
	
	for(int i = 1; i < 4; i++){
		count = 0;
		for(int j = 0; j < 4; j++){
			if(map[i][j] == 'O' || map[i][j] == 'T') count++;
		}
		if(count == 4) return true;
	}

	for(int i = 1; i < 4; i++){
		count = 0;
		for(int j = 0; j < 4; j++){
			if(map[j][i] == 'O' || map[j][i] == 'T') count++;
		}
		if(count == 4) return true;
	}

	return false;
}





bool isXwin(){
	int count = 0;
	for(int i = 0; i < 4; i++){
		if(map[0][i] == 'X' || map[0][i] == 'T') count++;
	}
	if(count == 4) return true;
	
	count = 0;
	for(int i = 0; i < 4; i++){
		if(map[i][0] == 'X' || map[i][0] == 'T') count++;
	}
	if(count == 4) return true;
	
	count = 0;
	for(int i = 0; i < 4; i++){
		if(map[i][i] == 'X' || map[i][i] == 'T') count++;
	}
	if(count == 4) return true;

	count = 0;
	for(int i = 0; i < 4; i++){
		if(map[i][3 - i] == 'X' || map[i][3 - i] == 'T') count++;
	}
	if(count == 4) return true;
	
	for(int i = 1; i < 4; i++){
		count = 0;
		for(int j = 0; j < 4; j++){
			if(map[i][j] == 'X' || map[i][j] == 'T') count++;
		}
		if(count == 4) return true;
	}

	for(int i = 1; i < 4; i++){
		count = 0;
		for(int j = 0; j < 4; j++){
			if(map[j][i] == 'X' || map[j][i] == 'T') count++;
		}
		if(count == 4) return true;
	}

	return false;
}

		

bool isEnd(){
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(map[i][j] == '.') return false;
		}
	}
	return true;
}
