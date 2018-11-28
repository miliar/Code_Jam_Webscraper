#include <stdio.h>
#include <vector>
#include <iostream>


using namespace std;

#define dbg(...)  \
	fprintf(stdout,__VA_ARGS__); \
	fprintf(stdout,"\n");


class SqTiles {

private:
	FILE * fin;
	FILE * fout;

public:
	SqTiles(char *fileName);
	~SqTiles() {
		fclose(fout);
		fclose (fin);
	}
	void ProcessInputs();
	void GetNewPainting(int cnum,vector<vector<char>> & rvec,int R,int C,int Bc,int Rc);
	void PrintVec(vector<vector<char>> & rvec,int R,int C);
};


SqTiles::SqTiles(char *fileName){
	if (!fileName) {
		cout << "No input file name!"<<endl;
		exit(1);
	}

	fin = fopen(fileName,"r");
	if (!fin) {
		cout << "Cannot open file "<<fileName<<endl;
		exit(1);
	}

	fout = fopen("C:/out.txt","w");
	if (!fout) {
		cout << "Cannot open file "<<"C:/out.txt"<<endl;
		exit(1);
	}

	ProcessInputs();

}


void SqTiles::ProcessInputs () {
	int T = 0;
	fscanf(fin,"%d",&T);
	dbg("Number of tests : %d",T);

	for (int i = 0; i < T; i++) {
		int R;
		int C;
		int Bc=0;
		int Wc=0;

		vector<vector<char>> rvec;
		fscanf(fin,"%d ",&R);
		dbg("Rows: %d",R);
		fscanf(fin,"%ld ",&C);
		dbg("Columns : %d",C);
		rvec.reserve(R);
		for (int j = 0 ; j < R ; j++ ) {
			vector <char> row;
			for (int k = 0; k < C ; k++) {
				char ch = '\0';
				fscanf(fin,"%c ",&ch);
				if (ch == '#')
					Bc++;
				else
					Wc++;
				cout<<ch;
				row.push_back(ch);
			}
			cout << endl;
			rvec.push_back(row);
		}


		GetNewPainting(i,rvec,R,C,Bc,Wc);
	}
}

void SqTiles::GetNewPainting(int cnum,vector<vector<char>> & rvec,int R,int C,int Bc,int Rc) {

	if (Bc != 0 && (Bc % 4 != 0 )) {
		fprintf(fout,"Case #%d:\nImpossible\n",cnum+1);
		dbg("Case #%d:\nImpossible",cnum+1);
		return;
	}

	if (Bc == 0 && Rc ) {
		fprintf(fout,"Case #%d:\n",cnum+1);
		dbg("Case #%d:",cnum+1);
		PrintVec(rvec,R,C);
		return;
	}

	int success = 1;
	for (int i = 0 ; i < R ; i++ ) {
		int impossible = 0;
		for (int j = 0 ; j < C ; j++ ) {
			if (rvec[i][j] == '#') {
				if ( i+1 < R && j+1 < C && rvec[i][j+1] == '#' && rvec[i+1][j] == '#' && rvec[i+1][j+1] == '#' ) {
					rvec[i][j] = '/';
					rvec[i][j+1] = '\\';
					rvec[i+1][j] = '\\';
					rvec[i+1][j+1] = '/';
				} else {
					impossible = 1;
					success = 0;
					break;
				}
			}
		}
		if (impossible)
			break;
	}

	if (success) {
		fprintf(fout,"Case #%d:\n",cnum+1);
		PrintVec(rvec,R,C);
	} else {
		fprintf(fout,"Case #%d:\nImpossible\n",cnum+1);
	}
}

	

void SqTiles::PrintVec(vector<vector<char>> & rvec,int R,int C) {
	for (int i = 0 ; i < R ; i++ ) {
		for (int j = 0 ; j < C ; j++ )  {
			fprintf(fout,"%c",rvec[i][j]);
			cout << rvec[i][j];
		}
		fprintf(fout,"\n");
		cout << endl;
	}
}


int main(int argc,char * argv[]) {
	SqTiles obj("C:/input.txt");
	return 0;
}