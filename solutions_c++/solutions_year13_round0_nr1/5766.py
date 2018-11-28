#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char** argv){
    ifstream fIn;
    ofstream fOut;
    
    int N;
    
    vector<vector<char> > table(4,vector<char>(4));
    int line;
    int column;
    int diag1;
    int diag2;

    char stat;

    fIn.open("input.dat", ifstream::in);
    fOut.open("output.dat", ofstream::out);

    if(fIn.is_open() && fOut.is_open()){
	fIn >> N;

	for(int i=0; i<N; i++){
	    stat = 'D';
	    diag1 = 0;
	    diag2 = 0;

	    for(int j=0; j<table.size(); j++){
		fIn >> table[j][0] >> table[j][1] >> table[j][2] >> table[j][3];
		if(table[j][0]=='.' || table[j][1]=='.' || table[j][2]=='.' || table[j][3]=='.') stat = 'I';
	    }
	    
	    for(int j=0; j<table.size(); j++){
		line=0;
		column=0;
		line = table[j][0]+table[j][1]+table[j][2]+table[j][3];
		column = table[0][j]+table[1][j]+table[2][j]+table[3][j];
		diag1 += table[j][j];
		diag2 += table[j][table.size()-j-1];

		if(line == 'X'*4 || line == 'X'*3+'T' || column == 'X'*4 || column == 'X'*3+'T'){
		    stat = 'X';
		    break;
		}
		if(line == 'O'*4 || line == 'O'*3+'T' || column == 'O'*4 || column == 'O'*3+'T'){
		    stat = 'O';
		    break;    
		}
	    }
	    if(stat != 'X' && stat != 'O'){	    
		if(diag1 == 'X'*4 || diag1 == 'X'*3+'T' || diag2 == 'X'*4 || diag2 == 'X'*3+'T') stat = 'X';
		if(diag1 == 'O'*4 || diag1 == 'O'*3+'T' || diag2 == 'O'*4 || diag2 == 'O'*3+'T') stat = 'O';
	    }
	    
	    fOut << "Case #" << i+1 << ": ";
	    switch(stat){
		case 'X':
		case 'O':
		    fOut << stat << " won";
		    break;
		case 'I':
		    fOut << "Game has not completed";
		    break;
		case 'D':
		    fOut << "Draw";
		    break;
	    }
	    fOut << "\n";
	}

	fIn.close();
	fOut.close();
    }
}
