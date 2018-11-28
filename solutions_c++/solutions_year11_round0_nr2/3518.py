#include <stdio.h>
#include <vector>
#include <iostream>
#include <stdlib.h>

using namespace std;

#define dbg(...)  \
	fprintf(stdout,__VA_ARGS__); \
	fprintf(stdout,"\n");

struct combine {

	char ch1;
	char ch2;
	char repch;
	int  flag;

	typedef enum { COMBINE = 1, OPPOSITE } TYPE;
	TYPE type;

	combine (TYPE type, char ch1,char ch2,char repch) {
		this->ch1 = ch1;
		this->ch2 = ch2;
		this->repch = repch;
		this->type = type;
		dbg("TYPE : %d , ch1 = %c , ch2 = %c , repch = %c",
			type,ch1,ch2,repch);
		this->flag = 0;
	}
};


class MagicKa {

	FILE * fin;
	FILE * fout;
	vector <char> str;
	vector <combine*> comb;
	vector <combine*> opp;

public:
	MagicKa(char * fileName) {
		ProcessInputs(fileName);
	}
	void ProcessInputs(char * fileName);

	void FreeVec(vector <combine*> & vec) {
		int i;
		for (i= 0 ; i< vec.size() ; i++) {
			free(vec[i]);
		}
		vec.clear();
	}

	char CheckForCombining(char ch1,char ch2) {
		if (!comb.size())
			return '\0';
		for (int i = 0; i < comb.size(); i++ ) {
			int num1 = comb[i]->ch1 + 2*comb[i]->ch2;
			int num2 = comb[i]->ch2 + 2*comb[i]->ch1;
			int num3 = ch1 + 2*ch2;
			int num4 = ch2 + 2*ch1;
			if ( (num1 == num3 && num2 == num4) || (num1 == num4 && num2 == num3)) 
				return comb[i]->repch;

		}
		return '\0';
	}

	bool DoesOppositeExist(char ch1,char ch2) {
		if (!opp.size())
			return false;
		for (int i = 0; i < opp.size(); i++ ) {
			int num1 = opp[i]->ch1 + 2*opp[i]->ch2;
			int num2 = opp[i]->ch2 + 2*opp[i]->ch1;
			int num3 = ch1 + 2*ch2;
			int num4 = ch2 + 2*ch1;
			if ( (num1 == num3 && num2 == num4) || (num1 == num4 && num2 == num3)) 
				return true;
		}
		return false;
	}

};

void MagicKa::ProcessInputs (char *fileName) {
	int T = 0;
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
	fscanf(fin,"%d",&T);
	dbg("Number of tests : %d",T);
	for (int i = 0; i < T; i++) {
		int C = 0;
		fscanf(fin,"%d ",&C);
		dbg("Number of combine strings : %d",C);
		for (int j = 0;j < C;j++) {
			char tuple[4] = {'\0'};
			fscanf(fin,"%s ",tuple);
			combine *obj = new combine(combine::COMBINE,tuple[0],tuple[1],tuple[2]);
			comb.push_back(obj);
		}
		int D = 0;
		fscanf(fin,"%d ",&D);
		dbg("Number of opposit strings : %d",D);
		for (int k = 0;k < D;k++) {
			char tuple[3] = {'\0'};
			fscanf(fin,"%s ",tuple);
			combine * obj = new combine(combine::OPPOSITE,tuple[0],tuple[1],tuple[2]);
			opp.push_back(obj);
		}

		int N = 0;
		fscanf(fin,"%d ",&N);
		dbg("Number of characters in string : %d",N);
		char *string = (char*)malloc(N+1);
		string[0] = '\0';
		fscanf(fin,"%s ",string);
		dbg ("String : %s",string);

		for(int l = 0; l < N; l++ ) {
			char topChar = '\0';
			if (str.size())
				topChar = str[str.size()-1];

			char combine = '\0';
			if ((combine = CheckForCombining(topChar,string[l]))) {
				str.pop_back();
				str.push_back(combine);
				continue;
			}

			int cleared = 0;
			for(int m = 0;m < str.size() ; m++) {
				if (DoesOppositeExist(str[m],string[l])) {
					str.clear();
					cleared =1;
					break;
				}
			}	
			if(cleared)
				continue;

			str.push_back(string[l]);
		}

		cout << "Case #" <<i+1<<": " <<"[";
		fprintf(fout,"Case #%d: [",i+1);
		int first = 1;
		for(int n=0; n < str.size(); n++)  {
			if (first) {
				cout <<str[n];
				fprintf(fout,"%c",str[n]);
				first = 0;
				continue;
			}
			cout <<", "<<str[n];
			fprintf(fout,", %c",str[n]);
		}
		cout <<"]\n";
		fprintf(fout,"]\n");

		free(string);
		str.clear();
		FreeVec(opp);
		FreeVec(comb);
	}
	fclose(fout);
	fclose(fin);
}


int main(int argc,char * argv[]) {
	MagicKa obj("C:/input1.txt");
	return 0;
}