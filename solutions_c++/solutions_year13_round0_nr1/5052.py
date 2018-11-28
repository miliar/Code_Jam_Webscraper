#include <iostream>
#include <fstream>
using namespace std;

int main(){
	int testC;
	ifstream fin("test.in");
	ofstream fout("test.out");

	int i,x,y,p;
	char pl[2]={'O','X'};
	char feld[4][4];
	bool undec;

	fin>>testC;
	for(i=0;i<testC;++i){
		fout<<"Case #"<<i+1<<": ";
		for(x=0;x<4;++x)
			for(y=0;y<4;++y)
				fin>>feld[x][y];
		undec=true;
		for(p=0;p<2&&undec;++p){
			if(undec){
				undec=false;
				for(x=0;x<4&&!undec;++x)
					if(feld[x][x]!=pl[p]&&feld[x][x]!='T')
						undec=true;
			}
			if(undec){
				undec=false;
				for(x=0;x<4&&!undec;++x)
					if(feld[3-x][x]!=pl[p]&&feld[3-x][x]!='T')
						undec=true;
			}
			for(y=0;y<4&&undec;++y){
				undec=false;
				for(x=0;x<4&&!undec;++x)
					if(feld[x][y]!=pl[p]&&feld[x][y]!='T')
						undec=true;
			}
			for(y=0;y<4&&undec;++y){
				undec=false;
				for(x=0;x<4&&!undec;++x)
					if(feld[y][x]!=pl[p]&&feld[y][x]!='T')
						undec=true;
			}
			if(!undec)
				fout<<pl[p]<<" won"<<endl;
		}
		for(x=0;x<4&&undec;++x)
			for(y=0;y<4&&undec;++y)
				if(feld[x][y]=='.'){
					fout<<"Game has not completed"<<endl;
					undec=false;
				}
		if(undec)
			fout<<"Draw"<<endl;
	}
	return 0;
}