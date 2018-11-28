#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <stdlib.h>
using namespace std;

string check(vector<string> &board){
    for(int k=0; k<2; k++){
	bool useT = false;
	bool isSuccess = true;
	for(int i=0; i<4; i++){

	    // row	    
	    for(int j=0; j<4; j++){
		if(board[i][j]=='T' && !useT)
		    useT = true;
		else if(k==0 && board[i][j] == 'X')
		    continue;
		else if(k==1 && board[i][j] == 'O')
		    continue;
		else{
		    isSuccess = false;
		    break;
		}
	    }
	    
	    if(isSuccess)
		return (k==0) ? "X won" : "O won";

	    // col
	    useT = false;
	    isSuccess = true;
	    for(int j=0; j<4; j++){
		if(board[j][i]=='T' && !useT)
		    useT = true;
		else if(k==0 && board[j][i] == 'X')
		    continue;
		else if(k==1 && board[j][i] == 'O')
		    continue;
		else{
		    isSuccess = false;
		    break;
		}
	    }
	    if(isSuccess)
		return (k==0) ? "X won" : "O won";
	}

	// '\'
	useT = false;
	isSuccess = true;
	for(int i=0; i<4; i++){
	    if(board[i][i]=='T' && !useT)
		useT = true;
	    else if(k==0 && board[i][i] == 'X')
		continue;
	    else if(k==1 && board[i][i] == 'O')
		continue;
	    else{
		isSuccess = false;
		break;
	    }
	}
	if(isSuccess)
	    return (k==0) ? "X won" : "O won";

	// '/'
	useT = false;
	isSuccess = true;
	for(int i=0; i<4; i++){
	    if(board[i][3-i]=='T' && !useT)
		useT = true;
	    else if(k==0 && board[i][3-i] == 'X')
		continue;
	    else if(k==1 && board[i][3-i] == 'O')
		continue;
	    else{
		isSuccess = false;
		break;
	    }
	}
	if(isSuccess)
	    return (k==0) ? "X won" : "O won";
    }

    for(int i=0; i<4; i++){
	for(int j=0; j<4; j++){
	    if(board[i][j] == '.')
		return "Game has not completed";
	}
    }
    return "Draw";
}

int main(){
    ifstream input_file("A-small-attempt0.in");
    ofstream output_file("output.out");
    string buff;
    vector<string> text;

    while(getline(input_file, buff))
	text.push_back(buff);	    

    int total = atoi(text[0].c_str());
    int caseCount = 0;
    for(int i=1; i<text.size(); i+=5){
	caseCount++;

	vector<string> board;
	for(int j=i; j<i+4; j++)
	    board.push_back(text[j]);

	string result = check(board);
	output_file << "Case #" << caseCount << ": " << result << endl;
    }

    

    input_file.close();
    output_file.close();
    return 0;    
}
