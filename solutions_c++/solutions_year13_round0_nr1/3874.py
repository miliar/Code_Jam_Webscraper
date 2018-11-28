#include<iostream>
#include<fstream>
#include<sstream>
#include<string>

using namespace std;

string convertInt(int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

int main(){
	int num=0;
	char board[4][4];
	string temp;
	char letter;
	bool full, found;
	ifstream inFile;
	ofstream outFile;
	inFile.open("input.in");
    outFile.open("output.out");
    if(!inFile){
        cerr << "Unable to DIE";
    }
    inFile >> num;
	
	for(int i=0; i<num; i++){
		inFile >> temp;
		board[0][0] = temp[0];
		board[0][1] = temp[1];
		board[0][2] = temp[2];
		board[0][3] = temp[3];
		inFile >> temp;
		board[1][0] = temp[0];
		board[1][1] = temp[1];
		board[1][2] = temp[2];
		board[1][3] = temp[3];
		inFile >> temp;
		board[2][0] = temp[0];
		board[2][1] = temp[1];
		board[2][2] = temp[2];
		board[2][3] = temp[3];
		inFile >> temp;
		board[3][0] = temp[0];
		board[3][1] = temp[1];
		board[3][2] = temp[2];
		board[3][3] = temp[3];
		
		outFile << std::string("Case #") + convertInt(i+1) + std::string(": ");
		found = false;
		
		//X rows
		for(int j=0; j<4; j++){
			if((board[j][0] == 'X' || board[j][0] == 'T') && (board[j][1] == 'X' || board[j][1] == 'T') && (board[j][2] == 'X' || board[j][2] == 'T') && (board[j][3] == 'X' || board[j][3] == 'T') && !found){
				outFile << "X won\n";
				found = true;
			}
		}
		//X cols
		for(int j=0; j<4; j++){
			if((board[0][j] == 'X' || board[0][j] == 'T') && (board[1][j] == 'X' || board[1][j] == 'T') && (board[2][j] == 'X' || board[2][j] == 'T') && (board[3][j] == 'X' || board[3][j] == 'T') && !found){
				outFile << "X won\n";
				found = true;
			}
		}
		//X diags
		if((board[0][0] == 'X' || board[0][0] == 'T') && (board[1][1] == 'X' || board[1][1] == 'T') && (board[2][2] == 'X' || board[2][2] == 'T') && (board[3][3] == 'X' || board[3][3] == 'T') && !found){
			outFile << "X won\n";
			found = true;
			continue;
		}
		if((board[3][0] == 'X' || board[3][0] == 'T') && (board[2][1] == 'X' || board[2][1] == 'T') && (board[1][2] == 'X' || board[1][2] == 'T') && (board[0][3] == 'X' || board[0][3] == 'T') && !found){
			outFile << "X won\n";
			found = true;
			continue;
		}
		//O rows
		for(int j=0; j<4; j++){
			if((board[j][0] == 'O' || board[j][0] == 'T') && (board[j][1] == 'O' || board[j][1] == 'T') && (board[j][2] == 'O' || board[j][2] == 'T') && (board[j][3] == 'O' || board[j][3] == 'T') && !found){
				outFile << "O won\n";
				found = true;
			}
		}
		//O cols
		for(int j=0; j<4; j++){
			if((board[0][j] == 'O' || board[0][j] == 'T') && (board[1][j] == 'O' || board[1][j] == 'T') && (board[2][j] == 'O' || board[2][j] == 'T') && (board[3][j] == 'O' || board[3][j] == 'T') && !found){
				outFile << "O won\n";
				found = true;
			}
		}
		//O diags
		if((board[0][0] == 'O' || board[0][0] == 'T') && (board[1][1] == 'O' || board[1][1] == 'T') && (board[2][2] == 'O' || board[2][2] == 'T') && (board[3][3] == 'O' || board[3][3] == 'T') && !found){
			outFile << "O won\n";
			found = true;
			continue;
		}
		if((board[3][0] == 'O' || board[3][0] == 'T') && (board[2][1] == 'O' || board[2][1] == 'T') && (board[1][2] == 'O' || board[1][2] == 'T') && (board[0][3] == 'O' || board[0][3] == 'T') && !found){
			outFile << "O won\n";
			found = true;
			continue;
		}
		full = true;
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				if(board[j][k] == '.'){
					full = false;
				}
			}
		}
		if(full && !found){
			outFile << "Draw\n";
		}
		else if(!full && !found){
			outFile << "Game has not completed\n";
		}
	}
	
	inFile.close();
	outFile.close();
	return 1;
}