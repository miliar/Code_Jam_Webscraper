#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>

using namespace std;

#define TAM 16

char tab[TAM][TAM];

bool is_completo(){

	for(int i = 0 ; i < 4 ;i++)
		for(int j = 0 ; j < 4 ; j++)
			if(tab[i][j] == '.') return false;

	return true;
}

bool ganha(char c){

	for(int i = 0 ; i < 4 ;i++){
		int countc = 0;
		int countt = 0;
		for(int j = 0 ; j < 4 ; j++){
			if(tab[i][j] == c) countc++;
			if(tab[i][j] == 'T') countt++;
		}
		if(countc == 4 || (countc == 3 && countt == 1)) return true;
	}

	for(int i = 0 ; i < 4 ;i++){
		int countc = 0;
		int countt = 0;
		for(int j = 0 ; j < 4 ; j++){
			if(tab[j][i] == c) countc++;
			if(tab[j][i] == 'T') countt++;
		}
		if(countc == 4 || (countc == 3 && countt == 1)) return true;
	}
	int countc = 0;
	int countt = 0;
	for(int i = 0 ; i < 4 ;i++){
		if(tab[i][i] == c) countc++;
		if(tab[i][i] == 'T') countt++;
	}
	if(countc == 4 || (countc == 3 && countt == 1)) return true;

	countc = 0;
	countt = 0;
	for(int i = 0 ; i < 4 ;i++){
		if(tab[i][3-i] == c) countc++;
		if(tab[i][3-i] == 'T') countt++;
	}
	if(countc == 4 || (countc == 3 && countt == 1)) return true;

	return false;
}

int main(){
	int nt;
	FILE *in = fopen("A.in","r");
	FILE *out = fopen("A.out","w");

	fscanf(in," %d",&nt);
	for(int t = 1 ; t <= nt ; t++){
		for(int i = 0 ; i < 4 ; i++) fscanf(in," %s",tab[i]);

		bool completo = is_completo();
		bool Xganha = ganha('X');
		bool Yganha = ganha('O');
		fprintf(out,"Case #%d: ",t);
		if(Xganha) fprintf(out,"X won\n");
		else if(Yganha) fprintf(out,"O won\n");
		else if(completo) fprintf(out,"Draw\n");
		else fprintf(out,"Game has not completed\n");

	}

	return 0;


}
