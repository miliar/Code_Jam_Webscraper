#include <iostream>
#include <fstream>
using namespace std;

char* Won(int TABLE[4][4]){
	//DRAW=0,NOT END=1,X=2,O=3
	int won=0;
	for(int m=0;m<4;m++){
		for(int n=0;n<4;n++){
			if(TABLE[m][n]==0)
				won=1;
		}
	}
	for(int m=0;m<4;m++){
		int x=0;
		int o=0;
		int t=0;
		for(int n=0;n<4;n++){
			if(TABLE[m][n]==1)
				x++;
			if(TABLE[m][n]==2)
				o++;
			if(TABLE[m][n]==3)
				t++;
		}
		if(x==4 || (x==3 && t==1))
			won =2;
		if(o==4 || (o==3 && t==1))
			won =3;
	}
	for(int m=0;m<4;m++){
		int x=0;
		int o=0;
		int t=0;
		for(int n=0;n<4;n++){
			if(TABLE[n][m]==1)
				x++;
			if(TABLE[n][m]==2)
				o++;
			if(TABLE[n][m]==3)
				t++;
		}
		if(x==4 || (x==3 && t==1))
			won =2;
		if(o==4 || (o==3 && t==1))
			won =3;
	}
	int x=0;
	int o=0;
	int t=0;
	for(int m=0;m<4;m++){
		if(TABLE[m][m]==1)
			x++;
		if(TABLE[m][m]==2)
			o++;
		if(TABLE[m][m]==3)
			t++;
	}
	if(x==4 || (x==3 && t==1))
		won =2;
	if(o==4 || (o==3 && t==1))
		won =3;
	x=0;
	o=0;
	t=0;
	for(int m=0;m<4;m++){
		if(TABLE[3-m][m]==1)
			x++;
		if(TABLE[3-m][m]==2)
			o++;
		if(TABLE[3-m][m]==3)
			t++;
	}
	if(x==4 || (x==3 && t==1))
		won =2;
	if(o==4 || (o==3 && t==1))
		won =3;
	char *out;
	switch(won){
	case 1:
		out="Game has not completed";
		break;
	case 2:
		out="X won";
		break;
	case 3:
		out="O won";
		break;
	case 0:
		out="Draw";
		break;
	}
	return out;
}

int main(){
	ifstream inp;
	ofstream out;
	out.open("d:/out.txt");
	inp.open("d:/a.in");
	int T;
	inp>>T;
	for(int i=1;i<=T;i++){
		int TABLE[4][4];
		for(int m=0;m<4;m++){
			for(int n=0;n<4;n++){
				char tmp;
				int tmp2;
				inp>>tmp;
				switch(tmp){
				case 'X':
					tmp2=1;
					break;
				case 'O':
					tmp2=2;
					break;
				case 'T':
					tmp2=3;
					break;
				default:
					tmp2=0;
				}
				TABLE[m][n]=tmp2;
			}	
		}
		cout<<"Case #"<<i<<": "<<Won(TABLE)<<endl;
		out<<"Case #"<<i<<": "<<Won(TABLE)<<endl;
	}
	system("pause");
	return 0;
}