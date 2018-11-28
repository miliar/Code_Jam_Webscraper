#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <fstream>
#include <list>

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

vector<string> parseStrStrV(string str,string del){
	int cut;
	string buf;
	vector<string> result;
	while( (cut = str.find_first_of(del)) != str.npos){
		if(cut > 0){
			buf = str.substr(0,cut);
			if(buf.length() == 0){
				continue;
			}
			result.push_back(buf.c_str());	
		}
		str = str.substr(cut+1);
	}
	if(str.length() > 0){
		result.push_back((str.c_str()));
	}
	return result;
}


int case_number;
#define gout case_number++, printf("Case #%d: ",case_number), cout

unsigned char C2H(char X){
	if(X>='0' && X<='9'){
		return X-'0';
	}else if(X>='A' && X<='F'){
		return X-'A'+10;
	}
	return 0;
}

unsigned char** getBoard(vector<string> buf,int N,int M){
	unsigned char** board = new unsigned char*[M];
	for(int i=0;i<M;i++){
		board[i] = new unsigned char[N];
	}

	for(int i=0;i<M;i++){
		for(int j=0;j<N/4;j++){
			unsigned char in = C2H(buf[i][j]);
			board[i][j*4+0] = (in>>3)&1;
			board[i][j*4+1] = (in>>2)&1;
			board[i][j*4+2] = (in>>1)&1;
			board[i][j*4+3] = (in>>0)&1;
		}
	}
	return board;
}

int check(int X,int Y,int size,int N,int M,unsigned char** board){
	int c = 0;
	if(X+size > N || Y+size > M) return 0;
	if(board[Y][X] == 3) return 0;
	for(int i=X;i<X+size;i++){
		int bef = board[Y][i];
		for(int j=Y+1;j<Y+size;j++){
			
			if(bef == board[j][i] || board[j][i] == 3){
				return 0;
			}
			bef = board[j][i];
		}
	}
	for(int j=Y;j<Y+size;j++){
		int bef = board[j][X];
		for(int i=X+1;i<X+size;i++){
			if(bef == board[j][i] || board[j][i] == 3){
				return 0;
			}
			bef = board[j][i];
		}
	}

	return 1;
}

void freeboard(unsigned char** mem,int N,int M){
	for(int i=0;i<M;i++){
		delete[] mem[i];
	}
	delete[] mem;
}

typedef struct _tagBoard{
	int X,Y,size;
} CHESS;

int main(int argc,char* argv[]){
	fstream fstr(argv[1]);
	string buf;

	if(!fstr||!getline(fstr,buf)) return 1;
	int T = atoi(buf.c_str());

	while(T-->0){
		
		if(!fstr||!getline(fstr,buf)) return 1;
		vector<int> in = parseStrIntV(buf," ");
		int M = in[0];
		int N = in[1];

		vector<string> msg;
		for(int i=0;i<M;i++){
			if(!fstr||!getline(fstr,buf)) return 1;
			msg.push_back(buf);
		}
		unsigned char** board = getBoard(msg,N,M);
		/*
		printf("\n\n\n");
		for(int Y=0;Y<M;Y++){
			for(int X=0;X<N;X++){
				printf("%d",board[Y][X]);
			}
			printf("\n");
		}
		printf("\n\n\n");
		*/
		map<int,vector<CHESS>> chess;
		for(int size = 1;size<=M;size++){
			for(int Y=0;Y<M;Y++){
				for(int X=0;X<N;X++){
					if(check(X,Y,size,N,M,board)){
						CHESS tmp;
						tmp.X = X;tmp.Y = Y;tmp.size = size;
						chess[size].push_back(tmp);
					}
				}
			}
		}

		map<int,int> result;
		int c = 0;
		for(int i=M;i>=1;i--){
			if(chess[i].size() == 0) continue;
			result[i] = 0;
			for(vector<CHESS>::iterator ite = chess[i].begin(); ite != chess[i].end(); ite++){
				if(check(ite->X,ite->Y,ite->size,N,M,board)){
					for(int X=ite->X;X<ite->X+ite->size;X++){
						for(int Y=ite->Y;Y<ite->Y+ite->size;Y++){
							board[Y][X] = 3;
						}
					}
					/*
					if(ite->size >= 4){
						printf("%d : %d %d\n",ite->size,ite->X,ite->Y);
					}
					*/
					result[i]++;
				}
			}
				 
		}
		/*

		for(int X=0;X<N;X++){
			for(int Y=0;Y<M;Y++){
				if(board[Y][X] != 3){
					printf("CHECK!!!!!!!!!!!!\n");
					getchar();
				}
			}
		}
		*/
		for(int i=M;i>=1;i--){
			if(result[i]==0) continue;
			c++;
		}
		gout << c << std::endl;
		//int k=0;
		for(int i=M;i>=1;i--){
			if(result[i] == 0) continue;
			printf("%d %d\n",i,result[i]);
		//	k+= result[i] * i* i;
		}
		//printf("%d*%d = %d(%d)\n",N,M,N*M,k);
		
		freeboard(board,N,M);

	}

}