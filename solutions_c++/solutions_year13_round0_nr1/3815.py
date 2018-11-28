#include <iostream>
#include <fstream>

using namespace std;

char tabelca[4][4] = {'*'};
// najprej vrstica, nato stolpec

int main(){
	ifstream input("in.in");
	ofstream out("out");
	ofstream tabel("tabelca");
	
	int ponovi;
	input >> ponovi;
	
	for(int a(0);a<ponovi;a++){
		bool X(false), O(false), empty(false);
		
		tabel << a+1 << endl;
		//get table
		for(int b(0);b<4;b++){
			tabel << "vrstica # " << b << ": ";
			for(int c(0);c<4;c++){
				char temp;
				while(true){
					input.get(temp);
					if(temp=='.' or temp=='T' or temp=='X' or temp=='O')break;
				}		
				tabelca[b][c]=temp;
				if(tabelca[b][c]=='.')empty=true;
				tabel << temp;
				
			}
			tabel << endl;
		}
			
		//vrstice preišèemo
		for(int b(0);b<4;b++){
			int x(0),o(0);
			for(int c(0);c<4;c++){
				if(tabelca[b][c]=='T' or tabelca[b][c]=='X'){
					x++;
				}
				if(tabelca[b][c]=='T' or tabelca[b][c]=='O'){
					o++;
				}
			}
			//check if there someone win
			if(x==4)X=true;
			if(o==4)O=true;
		}
		//stolpce preišèemo
		for(int b(0);b<4;b++){
			int x(0),o(0);
			for(int c(0);c<4;c++){
				if(tabelca[c][b]=='T' or tabelca[c][b]=='X'){
					x++;
				}
				if(tabelca[c][b]=='T' or tabelca[c][b]=='O'){
					o++;
				}
			}
			//check if there someone win
			if(x==4)X=true;
			if(o==4)O=true;
		}
		//diagonalno 1.
			int x(0),o(0);
			for(int b(0);b<4;b++){
				if(tabelca[b][b]=='T' or tabelca[b][b]=='X'){
					x++;
				}
				if(tabelca[b][b]=='T' or tabelca[b][b]=='O'){
					o++;
				}
			}
			//check if there someone win
			if(x==4)X=true;
			if(o==4)O=true;
			
		//diagonalno 2.
			x=0;
			o=0;
			for(int b(0), c(3);b<4 ;b++, c--){
				if(tabelca[c][b]=='T' or tabelca[c][b]=='X'){
					x++;
				}
				if(tabelca[c][b]=='T' or tabelca[c][b]=='O'){
					o++;
				}
			}
			//check if there someone win
			if(x==4)X=true;
			if(o==4)O=true;
		
		//PRINT THE CLUE
			out << "Case #" << a+1 << ": ";
			if(X==1 and O==1)out << "Draw";
			else if(X==1)out << "X won";
			else if(O==1)out << "O won";
			else if(empty==1)out << "Game has not completed";
			else out << "Draw";
			out << endl;
			
		char temp=input.get();
	}
	return 0;
}
