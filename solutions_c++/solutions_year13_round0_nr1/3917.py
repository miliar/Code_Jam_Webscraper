#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int T;
	fin>>T; string aux; getline(fin,aux);
	for(int I=0;I<T;I++) {
		char x[5][5];
		int np=0;
		int sumw[4]={0,0,0,0},sumh[4]={0,0,0,0},sumd[2]={0,0};
		for(int i=0;i<4;i++) { fin.getline(x[i],5); } fin.getline(x[5],5);
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				switch (x[i][j]) {
				case '.': np++; break;
				case 'O': sumh[j]+=1; sumw[i]+=1; break;
				case 'X': sumh[j]+=10; sumw[i]+=10; break;
				case 'T': sumh[j]+=100; sumw[i]+=100; break;
				}
			}
			
			switch (x[i][i]) {
				case 'O': sumd[0]+=1; break;
				case 'X': sumd[0]+=10; break;
				case 'T': sumd[0]+=100; break;
			}
			switch (x[i][3-i]) {
				case 'O': sumd[1]+=1; break;
				case 'X': sumd[1]+=10; break;
				case 'T': sumd[1]+=100; break;
			}
		}
		bool xwon=false,owon=false;
		for(int j=0;j<4;j++) { 
			switch (sumw[j]) {
			case 4:case 103: owon=true; break;
			case 40:case 130: xwon=true; break;
			}
			switch (sumh[j]) {
			case 4:case 103: owon=true; break;
			case 40:case 130: xwon=true; break;
			}
		}
		for(int j=0;j<2;j++) { 
			switch (sumd[j]) {
			case 4:case 103: owon=true; break;
			case 40:case 130: xwon=true; break;
			}
		}
		if (xwon) fout<<"Case #"<<I+1<<": X won"<<endl;
		else if (owon) fout<<"Case #"<<I+1<<": O won"<<endl;
		else if (np) fout<<"Case #"<<I+1<<": Game has not completed"<<endl;
		else fout<<"Case #"<<I+1<<": Draw"<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}

