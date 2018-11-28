#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <array>

using namespace std;

#define INIT -1
#define X_WIN 0
#define O_WIN 1
#define HAS_EMPTY 2
#define DRAW 3

//possible newIn: X,O,T
static int modStatus(char newIn, int oldStatus){
	if(oldStatus==DRAW) return DRAW;
	if(oldStatus==INIT){
		if(newIn=='X')
			return X_WIN;
		else if(newIn=='O')
			return O_WIN;
		else return INIT;
	}else if(oldStatus==X_WIN){
		if(newIn=='X' || newIn=='T')
			return X_WIN;
		else return DRAW;
	}else if(oldStatus==O_WIN){
		if(newIn=='O' || newIn=='T')
			return O_WIN;
		else return DRAW;
	}
}

static int checkCol(array<array<char,4>,4>* const &gridarray, int col){

	int status = INIT;

	for(int i=0;i<4;i++){
		char test = (*gridarray)[i][col];
		if(test == '.')
			return HAS_EMPTY;
		else status = modStatus(test, status);
	}

	return status;
}

int checkRow(array<array<char,4>,4>* const &gridarray, int row){

	int status = INIT;

	for(int i=0;i<4;i++){
		char test = (*gridarray)[row][i];
		if(test == '.')
			return HAS_EMPTY;
		else status = modStatus(test, status);
	}

	return status;
}


int checkDiag(array<array<char,4>,4>* const &gridarray, int cor){
	int status = INIT;
	int startAt;
	int mult;

	if(cor == 0){
		startAt=0;
		mult=1;
	}else if(cor==1){
		startAt=3;
		mult=-1;
	}else return DRAW;

	for(int i=0;i<4;i++){
		int j=startAt+mult*i;
		char test = (*gridarray)[i][j];
		if(test == '.')
			return HAS_EMPTY;
		else status = modStatus(test, status);
	}
	return status;
}

void printOut(int caseNum, int status, ostream& c){
	c << "Case #" << caseNum+1 << ": ";
	switch(status){
	case X_WIN:
		c << "X won";
		break;
	case O_WIN:
		c << "O won";
		break;
	case HAS_EMPTY:
		c << "Game has not completed";
		break;
	case DRAW:
		c << "Draw";
		break;
	}
	c << endl;
	return;
}

int main(){
	istream * stream;
	ifstream myfile;
	myfile.open("A-large.in");

	ofstream outfile;
	outfile.open("output.txt");
	
	if(myfile.is_open()){
		stream = &myfile;
	}else{
		stream = &cin;
	}

	int num;

	string in;
	getline(*stream,in);
	num = atoi(in.c_str());

	vector<array<array<char,4>,4>> gridarray;
	
	
	for(int i=0;i<num;i++){
		array<array<char,4>,4> te = {{0}};
		for(int j=0;j<4;j++){
			getline(*stream,in);
			for(int k=0;k<4;k++){
				te[j][k] = in[k];
			}
		}

		gridarray.push_back(te);
		getline(*stream,in);
	}


	for(int i=0;i<num;i++){
		/*for(int j=0;j<4;j++){
			cout << checkCol(&gridarray[i], j) << endl;
		}
		for(int j=0;j<4;j++){
			cout << checkRow(&gridarray[i], j) << endl;
		}
		cout << endl;*/

		int cmp;
		bool hasEmpty = false;
		bool hasPrinted = false;

		for(int j=0;j<4;j++){
			
			cmp = checkCol(&gridarray[i], j);
			if(cmp == X_WIN || cmp == O_WIN){
				printOut(i,cmp,outfile);
				hasPrinted = true;
				break;
			}
			else if(cmp == HAS_EMPTY) hasEmpty = true;


			cmp = checkRow(&gridarray[i], j);
			if(cmp == X_WIN || cmp == O_WIN){
				printOut(i,cmp,outfile);
				hasPrinted = true;
				break;
			}
			else if(cmp == HAS_EMPTY) hasEmpty = true;

			cmp = checkDiag(&gridarray[i], j);
			if(cmp == X_WIN || cmp == O_WIN){
				printOut(i,cmp,outfile);
				hasPrinted = true;
				break;
			}
			else if(cmp == HAS_EMPTY) hasEmpty = true;
		}

		if(!hasPrinted){
			if(hasEmpty){
			printOut(i,HAS_EMPTY,outfile);
			}else printOut(i,DRAW,outfile);
		}
	}

}
