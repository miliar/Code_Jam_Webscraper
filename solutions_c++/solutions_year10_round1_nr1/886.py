#include <cstdio>
#include <cstdlib>
#include <vector>
#include <list>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;


vector<double> parseStrDoubleV(string str,string del){
	int cut;
	string buf;
	vector<double> result;
	while( (cut = str.find_first_of(del)) != str.npos){
		if(cut > 0){
			buf = str.substr(0,cut);
			if(buf.length() == 0){
				continue;
			}
			result.push_back(atof(buf.c_str()));	
		}
		str = str.substr(cut+1);
	}
	if(str.length() > 0){
		result.push_back(atof(str.c_str()));
	}
	return result;
}	

list<double> parseStrDoubleL(string str,string del){
	int cut;
	string buf;
	list<double> result;
	while( (cut = str.find_first_of(del)) != str.npos){
		if(cut > 0){
			buf = str.substr(0,cut);
			if(buf.length() == 0){
				continue;
			}
			result.push_back(atof(buf.c_str()));	
		}
		str = str.substr(cut+1);
	}
	if(str.length() > 0){
		result.push_back(atof(str.c_str()));
	}
	return result;
}	


list<int> parseStrIntL(string str,string del){
	int cut;
	string buf;
	list<int> result;
	while( (cut = str.find_first_of(del)) != str.npos){
		if(cut > 0){
			buf = str.substr(0,cut);
			if(buf.length() == 0){
				continue;
			}
			result.push_back(atoi(buf.c_str()));	
		}
		str = str.substr(cut+1);
	}
	if(str.length() > 0){
		result.push_back(atoi(str.c_str()));
	}
	return result;
}	

vector<int> parseStrIntV(string str,string del){
	int cut;
	string buf;
	vector<int> result;
	while( (cut = str.find_first_of(del)) != str.npos){
		if(cut > 0){
			buf = str.substr(0,cut);
			if(buf.length() == 0){
				continue;
			}
			result.push_back(atoi(buf.c_str()));	
		}
		str = str.substr(cut+1);
	}
	if(str.length() > 0){
		result.push_back(atoi(str.c_str()));
	}
	return result;
}	

char ** getBoard(vector<string> list,int size){
	char** res;
	res = new char*[size];
	for(int i=0;i<size;i++){
		res[i] = new char[size];
		for(int j=0;j<size;j++){
			res[i][j] = list[i].c_str()[j];
		}
	}
	return res;
}

void free(char** res,int size){
	for(int i=0;i<size;i++){
		delete[] res[i];
	}
	delete[] res;
}

void shift(char* line,int size,int n){
	for(int i=0;i<size-n;i++){
		line[size-i-1] = line[size-i-1-n];
	}
	for(int i=0;i<n;i++){
		line[i] = '.';
	}
	
}

void  boardout(char** line,int size){
	for(int i=0;i<size;i++){
		for(int j=0;j<size;j++){
			printf("%c",line[i][j]);
		}
		printf("\n");
	}
}	

int countWin(char** board,int size,int K){
	int wr = 0;
	int wb = 0;
	int r=0;
	int b=0;
	for(int i=0;i<size;i++){
		r=b=0;
		for(int j=0;j<size;j++){
			if(board[i][j] == 'R'){
				r++;
				b=0;
			}else if(board[i][j] == 'B'){
				b++;
				r=0;
			}else if(board[i][j] == '.'){
				b=r=0;
			}
			if(r == K){
				wr = 1;
			}
			if(b == K){
				wb = 1;
			}
		}

	}
	r=b=0;
	for(int j=0;j<size;j++){
		r=b=0;
		for(int i=0;i<size;i++){
			if(board[i][j] == 'R'){
				r++;
				b=0;
			}else if(board[i][j] == 'B'){
				b++;
				r=0;
			}else if(board[i][j] == '.'){
				b=r=0;
			}
			if(r == K){
				wr = 1;
			}
			if(b == K){
				wb = 1;
			}
		}
	}
	for(int i=0;i<size;i++){
		r=b=0;
		for(int j=0;j<size && i+j<size;j++){
			if(board[i+j][j] == 'R'){
				r++;
				b=0;
			}else if(board[i+j][j] == 'B'){
				b++;
				r=0;
			}else if(board[i][j] == '.'){
				b=r=0;
			}
			if(r == K){
				wr = 1;
			}
			if(b == K){
				wb = 1;
			}
		}
	}
	for(int i=0;i<size;i++){
		r=b=0;
		for(int j=0;j<size && i+j<size;j++){
			if(board[i+j][size-1-j] == 'R'){
				r++;
				b=0;
			}else if(board[i+j][size-1-j] == 'B'){
				b++;
				r=0;
			}else if(board[i][j] == '.'){
				b=r=0;
			}
			if(r == K){
				wr = 1;
			}
			if(b == K){
				wb = 1;
			}
		}
	}
	for(int i=0;i<size;i++){
		r=b=0;
		for(int j=0;j<size && i-j>=0;j++){
			if(board[i-j][j] == 'R'){
				r++;
				b=0;
			}else if(board[i-j][j] == 'B'){
				b++;
				r=0;
			}else if(board[i][j] == '.'){
				b=r=0;
			}
			if(r == K){
				wr = 1;
			}
			if(b == K){
				wb = 1;
			}
		}
	}
	for(int i=0;i<size;i++){
		r=b=0;
		for(int j=0;j<size && i-j>=0;j++){
			if(board[i-j][size-1-j] == 'R'){
				r++;
				b=0;
			}else if(board[i-j][size-1-j] == 'B'){
				b++;
				r=0;
			}else if(board[i][j] == '.'){
				b=r=0;
			}
			if(r == K){
				wr = 1;
			}
			if(b == K){
				wb = 1;
			}
		}
	}
	return wr << 1 | wb;
}

int main(int argc,char** argv){
	fstream fst(argv[1]);
	string buf;
	if(!fst||!getline(fst,buf)) return 1;
	FILE* fp = fopen("res.txt","w");
	//FILE* fp = stdout;

	int T = atoi(buf.c_str());
	int round = 0;
	while(T-->0){
		if(!fst||!getline(fst,buf)) return 1;
		vector<int> in = parseStrIntV(buf," ");
		int size = in[0];
		int K = in[1];

		vector<string> vstr;
		for(int i=0;i<size;i++){
			if(!fst||!getline(fst,buf)) return 1;
			vstr.push_back(buf);
		}
		char** board = getBoard(vstr,size);

		for(int i=0;i<size;i++){
			for(int j=0;j<size && board[i][size-1] == '.';j++){
				shift(board[i],size,1);
			}
		}

		for(int i=0;i<size;i++){
			bool flag = 0;
			int j;
			for(j=0;j<size;j++){
				if(flag == 0 && board[i][j] != '.'){
					flag = 1;
				}
				if(flag == 1 && board[i][j] == '.'){
					shift(board[i],j+1,1);	
					break;
				}
			}
			if(j!=size && flag == 1)
				i--;

		}

		printf("%d\n",K);
		boardout(board,size);
		fprintf(fp,"Case #%d: ",++round);
		switch(countWin(board,size,K)){
		case 0:
			fprintf(fp,"Neither\n");
			break;
		case 1:
			fprintf(fp,"Blue\n");
			break;
		case 2:
			fprintf(fp,"Red\n");
			break;
		case 3:
			fprintf(fp,"Both\n");
			break;
		}

		
	}
	fclose(fp);


}
