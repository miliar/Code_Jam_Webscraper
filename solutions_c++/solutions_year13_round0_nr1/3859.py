#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

enum{
	X_WON,
	O_WON,
	DRAW,
	UNFINISHED
};

int status(string lines[4]){
	bool boardFull = true, xWon = false, oWon = false, draw = false;
	// test rows
	for(unsigned i = 0; i<4; i++){
		if(lines[i] == "XXXX" || lines[i] == "XXXT" || lines[i] == "XXTX" || lines[i] == "XTXX"|| lines[i] == "TXXX"){
			return X_WON;
			
		}
		
		if(lines[i] == "OOOO" || lines[i] == "OOOT" || lines[i] == "OOTO" || lines[i] == "OTOO"|| lines[i] == "TOOO"){
			return O_WON;
		}
	}
	
	// test columns 
	string columns[4];
	for(unsigned i = 0; i<4; i++){
		for(unsigned j = 0; j<4; j++){
			char &t = lines[j][i];
			if ( t == '.' ) boardFull = false;
			columns[i] += t;
		}
	}
	
	for(unsigned i = 0; i<4; i++){
		if(columns[i] == "XXXX" || columns[i] == "XXXT" || columns[i] == "XXTX" || columns[i] == "XTXX"|| columns[i] == "TXXX"){
			return X_WON;
			
		}
		
		if(columns[i] == "OOOO" || columns[i] == "OOOT" || columns[i] == "OOTO" || columns[i] == "OTOO"|| columns[i] == "TOOO"){
			return O_WON;
		}
	}
	
	// test diags
	string diags[2];
	diags[0] = "";
	diags[1] = "";

	for(int ii = 0; ii<4; ii++){
		diags[0]+=lines[ii][ii];
		diags[1]+=lines[ii][3-ii];
	}

//	cout<<"diags: "<<diags[0]<<" "<<diags[1]<<endl;
	
	if(diags[0] == "XXXX" || diags[0] == "XXXT" || diags[0] == "XXTX" || diags[0] == "XTXX"|| diags[0] == "TXXX"){
		return X_WON;
	}
	
	if(diags[1] == "XXXX" || diags[1] == "XXXT" || diags[1] == "XXTX" || diags[1] == "XTXX"|| diags[1] == "TXXX"){
		return X_WON;
	}
	
	if(diags[0] == "OOOO" || diags[0] == "OOOT" || diags[0] == "OOTO" || diags[0] == "OTOO"|| diags[0] == "TOOO"){
		return O_WON;
	}
	
	if(diags[1] == "OOOO" || diags[1] == "OOOT" || diags[1] == "OOTO" || diags[1] == "OTOO"|| diags[1] == "TOOO"){
		return O_WON;
	}
	
	
	return boardFull?DRAW:UNFINISHED;
}

int main(int argc, char *argv[]) {
	ifstream input("/home/pabratte/Downloads/A-large.in");
	if(!input.is_open()){
		cerr<<"ERROR: No se pudo abrir archivo"<<endl;
	}
#ifndef M_DEBUG
	ofstream output("1_large.out");
#else
	ostream &output = cout;
#endif
	unsigned nTestCases;
	input>>nTestCases;
	input.ignore();
	string lines[4];
	for(unsigned i = 0; i < nTestCases; i++){
		for(unsigned c = 0; c < 4; c++){
			getline(input, lines[c]);
			cout<<lines[c]<<endl;
		}
		input.ignore();
		
		int result = status(lines);
		string out;
		switch(result){
		case X_WON: out = "X won"; break;
		case O_WON: out = "O won"; break;
		case DRAW: out = "Draw"; break;
		case UNFINISHED: out = "Game has not completed"; break;
		}
		output<<"Case #"<<i+1<<": "<<out<<endl;
	}
	
	input.close();
#ifndef M_DEBUG
	output.close();
#endif
	return 0;
}

