#include <iostream>
#include <fstream>
using namespace std;
int t,T;
char box[4][5];

char win;
ifstream fin;
ofstream fout;
bool isequal(int ax,int ay,int bx,int by){
	return ((box[ax][ay]=='T'||box[bx][by]=='T'||box[ax][ay]==box[bx][by])&&(box[ax][ay]!='.'&&box[bx][by]!='.'));
}

void inputbox(){
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			fin>>box[i][j];
		}
	}
	
};

bool judgediag(){
	if(isequal(0,0,1,1)&&isequal(0,0,2,2)&&isequal(0,0,3,3)){
		fout<<"Case #"<<t+1<<": "<<((box[0][0]!='T')?box[0][0]:box[1][1])<<" won"<<endl;
		return true;
	}
	if(isequal(0,3,1,2)&&isequal(0,3,2,1)&&isequal(0,3,3,0)){
		fout<<"Case #"<<t+1<<": "<<((box[0][3]!='T')?box[0][3]:box[3][0])<<" won"<<endl;
		return true;
	}
	return false;
};

bool judgecol(){
	for(int j=0;j<4;j++){
		if(isequal(0,j,1,j)&&isequal(0,j,2,j)&&isequal(0,j,3,j)){
			fout<<"Case #"<<t+1<<": "<<((box[0][j]!='T')?box[0][j]:box[1][j])<<" won"<<endl;
			return true;			
		}
	}
	return false;
};
bool judgerow(){
	for(int j=0;j<4;j++){
		if(isequal(j,0,j,1)&&isequal(j,0,j,2)&&isequal(j,0,j,3)){
			fout<<"Case #"<<t+1<<": "<<((box[j][0]!='T')?box[j][0]:box[j][1])<<" won"<<endl;
			return true;
		}
	}
	return false;
};
bool isfull(){
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++){
			if(box[i][j]=='.')return false;
		}
	return true;
};

int main(){
	fin.open("A-small-attempt0.in");
	fout.open("A-small-attempt0.out");
	fin>>T;
	for(t=0;t<T;t++){
		inputbox();
		if(judgediag()) continue;
		if(judgecol()) continue;
		if(judgerow()) continue;
		if(isfull()) {
			fout<<"Case #"<<t+1<<": Draw"<<endl;	
			continue;
		}
		//not finish
		fout<<"Case #"<<t+1<<": Game has not completed"<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}