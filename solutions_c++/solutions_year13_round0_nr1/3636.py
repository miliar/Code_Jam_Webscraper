#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main(void){

	int N;
	long long*a;
	long long*b;
	int i;
	
	ifstream fin;
	fin.open("A-large.in",ios_base::in);
	ofstream fout;
	fout.open("output.txt",ios_base::out);

	fin>>N;
	for(int test=0;test<N;test++){

		char data[4][4];
		int xRows[4] = {0};
		int yRows[4] = {0};
		int xColumns[4] = {0};
		int yColumns[4] = {0};
		int xDiag1 = 0; int xDiag2 = 0;
		int yDiag1 =0; int yDiag2 = 0;
		bool pExists = false;
		
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				fin>>data[j][k];
				if(data[j][k] == 'X' || data[j][k] == 'T'){
					xRows[j]++;
					xColumns[k]++;
					if(j==k) xDiag1++;
				}
				if(data[j][k] == 'O' || data[j][k] == 'T') {
					yRows[j]++;
					yColumns[k]++;
					if(j==k) yDiag1++;
				}
				if(data[j][k] == '.') pExists = true;
			}
		}
		
		for(int i=0;i<4;i++){
			if(data[i][4-i-1] == 'X' || data[i][4-i-1] == 'T'){
				xDiag2++;
			}
			if(data[i][4-i-1] == 'O' || data[i][4-i-1] == 'T'){
				yDiag2++;
			}
		}

		bool xWins = false;
		bool oWins = false;
		
		int s = *max_element(xRows, xRows+4);
		if(*max_element(xRows, xRows+4) == 4 || *max_element(xColumns, xColumns+4) == 4 || xDiag1 == 4 || xDiag2 == 4) xWins = true;
	    if(*max_element(yRows, yRows+4) == 4 || *max_element(yColumns,yColumns+4) == 4 || yDiag1 == 4 || yDiag2 == 4) oWins = true;

		if(xWins) fout<<"Case #"<<test+1<<": "<<"X won"<<endl;
		else if(oWins)  fout<<"Case #"<<test+1<<": "<<"O won"<<endl;
		else if(!xWins && !oWins && pExists) fout<<"Case #"<<test+1<<": "<<"Game has not completed"<<endl;
		else if(!xWins && !oWins && !pExists) fout<<"Case #"<<test+1<<": "<<"Draw"<<endl;

	}

	fin.close();
	fout.close();



}