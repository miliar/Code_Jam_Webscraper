#include<iostream>
#include<string>
#include<fstream>
using namespace std;

char data[4][4];

bool solve1(int h,char s){

	for(int i=0;i<4;i++){
		if(data[h][i]!=s && data[h][i]!='T'){
			return false;
		}
	}
	return true;
}

bool solve2(int w,char s){

	for(int i=0;i<4;i++){
		if(data[i][w]!=s && data[i][w]!='T'){
			return false;
		}
	}
	return true;
}

bool solve3(char s){
	for(int i=0;i<4;i++){
		if(data[i][i]!=s && data[i][i]!='T'){
			return false;
		}
	}
	return true;
}

bool solve4(char s){
	for(int i=0;i<4;i++){
		if(data[i][3-i]!=s && data[i][3-i]!='T'){
			return false;
		}
	}
	return true;
}

bool solve(char s){
	for(int i=0;i<4;i++){
		if(solve1(i,s) || solve2(i,s)){
			return true;
		}
	}
	if(solve3(s)||solve4(s)){
		return true;
	}
	return false;
}

int main(){
	ifstream ifs("A-large.in");
	ofstream ofs("ans_a_2.txt");

	int T;

	ifs >> T;

	for(int t=0;t<T;t++){
		bool endflag = true;
		
		for(int i=0;i<4;i++){
			string buf;
			ifs >> buf;
			for(int j=0;j<4;j++){
				data[i][j] = buf[j];
				if(buf[j] == '.'){
					endflag = false;
				}
			}
		}

		int ans = 0;
		if(solve('X')){
			ofs << "Case #" << (t+1) << ": X won" << endl;
		}else if(solve('O')){
			ofs << "Case #" << (t+1) << ": O won" << endl;
		}else if(endflag){
			ofs << "Case #" << (t+1) << ": Draw" << endl;
		}else{
			ofs << "Case #" << (t+1) << ": Game has not completed" << endl;
		}
		
	}


	ofs.close();
}