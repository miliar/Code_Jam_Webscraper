#include "stdio.h"
#include <iostream>
#include <fstream>

using namespace std;

class FileReadData{
	ifstream _read;

public :
	FileReadData(){}
	~FileReadData(){ _read.close();	}
	void open(char *afilename){ _read.open(afilename);}
	bool good(){return _read.good();}
	bool read(char *stream){
		if(_read.good()){
			_read >> stream;
			return true;
		}
		else{ return false; }
	}
	int readNum(){ int value;
		if(_read.good()){
			_read >> value;
			return value;
		}
		else{ return -1;}
	}
};


class Magicka{
	int		C;
	char	Cchar[100][4];
	int		Csize;
	int		D;
	char	Dchar[100][4];
	int		Dsize;
	int		N;
	char	Nchar[200];
	int		Noffset;
	char	base[9];

public:
	Magicka(){
		C		= 0;
		Csize	= 0;
		D		= 0;
		Dsize	= 0;
		N		= 0;
		Noffset	= 0;
		strcpy(base, "ASDFQWER");
	}

	void	read(FileReadData &read){
		int iter = 0;
		C = read.readNum();
		for(iter = 0; iter < C; iter++){
			read.read(Cchar[iter]);
			if(NULL == strchr(base, (int)Cchar[iter][0])){
				printf("Error in C\n");
			}
			if(NULL == strchr(base, (int)Cchar[iter][1])){
				printf("Error in C\n");
			}
			if(NULL != strchr(base, (int)Cchar[iter][2])){
				printf("Error in C\n");
			}
		}
		D = read.readNum();
		for(iter = 0; iter < D; iter++){
			read.read(Dchar[iter]);
			if(NULL == strchr(base, (int)Dchar[iter][0])){
				printf("Error in D\n");
			}
			if(NULL == strchr(base, (int)Dchar[iter][1])){
				printf("Error in D\n");
			}
		}
		N = read.readNum();
		read.read(Nchar);
	}

	void copy(char *from, char *to, int size){
		int iter = 0;
		for(;iter<size;iter++){
			*(to+iter) = *(from+iter);
		}
	}

	void chkC(int position){
		int iter = 0;
		for(;iter < C; iter++){
			bool match = false;
			if(Nchar[position+Noffset] == Cchar[iter][0]){
				if(Nchar[position-1+Noffset] == Cchar[iter][1]){
					match = true;
				}
			}
			else if(Nchar[position+Noffset] == Cchar[iter][1]){
				if(Nchar[position-1+Noffset] == Cchar[iter][0]){
					match = true;
				}
			}
			if(match == true){
				Nchar[position-1+Noffset] = Cchar[iter][2];
				/** CHeck for newline copy **/
				copy(&Nchar[position+Noffset+1],&Nchar[position+Noffset],N-position);
				N--;
				iter = -1;
			}
		}
	}

	int chkDmatchPos(int Dnum, int index, int position){
		int cnt = 0;
		for(;cnt < position;cnt++){
			if(Dchar[Dnum][index] == Nchar[Noffset+cnt]){
				return cnt;
			}
		}
		return -1;
	}

	void remove(int end){
		/** Check this operation */
		Noffset+=(end+1);
		N -= (end+1);
	}

	bool chkD(int position){
		int iter = 0;
		for(;iter < D;iter++){
			if(Dchar[iter][0] == Nchar[position+Noffset]){
				int start = chkDmatchPos(iter,1, position);
				if(-1 != start){
					remove(position);
					return true;
				}
			}
			else if(Dchar[iter][1] == Nchar[position+Noffset]){
				int start = chkDmatchPos(iter,0, position);
				if(-1 != start){
					remove(position);
					return true;
				}
			}
		}
		return false;
	}

	void genFinal(char *string){
		string[0] = '[';
		int iter = 0;
		for(iter = 1;iter < N; iter++){
			chkC(iter);
			if(true == chkD(iter)) {
				iter = 0;
			}
		}
		for(iter = 0;iter < N; iter++){
			string[3*iter+1] = Nchar[iter+Noffset];
			string[3*iter+2] = ',';
			string[3*iter+3] = ' ';
		}
		if(iter != 0){
			string[3*iter-1] = ']';
			string[3*iter] = 0;
		}
		else{
			string[3*iter+1] = ']';
			string[3*iter+2] = 0;
		}
		return;
	}
};

void main (int argc, char *argv[])
{
	FileReadData read;
	
	//read.open("E:\\users\\parikshit\\msvc\\folder1\\data\\test5.in");
	//read.open("E:\\users\\parikshit\\msvc\\folder1\\data\\B-small-attempt0.in");
	read.open("E:\\users\\parikshit\\msvc\\folder1\\data\\B-large.in");
	ofstream out("E:\\users\\parikshit\\msvc\\folder1\\data\\output6.out");

	if(out.good() && read.good())
		cout << "All okay" << endl;
	else
		cout << "File wrong" << endl;

	int numCases = read.readNum();
	cout << numCases << endl;

	int countCases = 0;

	for(;countCases < numCases;countCases++){
		Magicka	magic;
		char	output[300];
		magic.read(read);
		magic.genFinal(output);
		cout << "Case #" << countCases + 1 << ": " << output << endl;
		out << "Case #" << countCases + 1 << ": " << output << endl;
	}

	//cin.get();
	return;
}