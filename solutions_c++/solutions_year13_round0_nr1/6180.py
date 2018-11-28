#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

char table[4][4];

char result(){
	
	int score;
	
	for(int j = 0; j < 4; j++){
		score = 0;
		for(int i = 0; i < 4; i++){
			score += (int)table[i][j];
		}
		if(score == 316 || score == 321)
			return 'O';
		else if(score == 352 || score == 348)
			return 'X';
	}
	
	for(int i = 0; i < 4; i++){
		score = 0;
		for(int j = 0; j < 4; j++){
			score += (int)table[i][j];
		}
		if(score == 316 || score == 321)
			return 'O';
		else if(score == 352 || score == 348)
			return 'X';
	}
	
	score = 0;
	for(int i = 0; i < 4; i++){
		score += (int)table[i][i];
	}
	if(score == 316 || score == 321)
		return 'O';
	else if(score == 352 || score == 348)
		return 'X';
		
	score = table[3][0] + table[2][1] + table[0][3] + table[1][2];
	if(score == 316 || score == 321)
		return 'O';
	else if(score == 352 || score == 348)
		return 'X';
	
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++)
			if(table[i][j] == '.')
				return 'N';
	}
	
	return 'D';
}

int main(){
	
	string line;
  	ifstream myfile("large.in");
  	if(myfile.is_open()){
  		getline(myfile,line);
  		int test_cases = atoi(line.c_str());
    	for(int i = 1; i <= test_cases; i++){
      		
      		for(int j = 0; j < 4; j++){
      			getline(myfile,line);
      			for(int k = 0; k < 4; k++)
      				table[k][j] = line[k];
      		}
      		getline(myfile,line); // reading empty line
      		
      		char res = result();
      		if(res == 'X' || res == 'O')
      			cout << "Case #" << i << ": " << res << " won" << endl;
      		else if(res == 'D')
      			cout << "Case #" << i << ": " << "Draw" << endl;
      		else if(res == 'N')
      			cout << "Case #" << i << ": " << "Game has not completed" << endl;
    	}
    	myfile.close();
  	}
  	else cout << "Unable to open file";
	
	return 0;
}
