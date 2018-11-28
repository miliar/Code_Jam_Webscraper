#include<iostream>
#include<fstream>
#include<string>
#include<cstdlib>
/*

jwkim0000@gmail.com
CodeJam nickname : JackRabbit

*/
using namespace std;

const int XWIN=1;
const int OWIN=2;
const int DRAW=3;
const int NOTCOM=0;

int getResult(char matrix[4][4]){
	//	가로행 검사 X
	for(int i=0;i<4;i++){
		if((matrix[i][0]=='X')||(matrix[i][0]=='T')){
			if((matrix[i][1]=='X')||(matrix[i][1]=='T')){
				if((matrix[i][2]=='X')||(matrix[i][2]=='T')){
					if((matrix[i][3]=='X')||(matrix[i][3]=='T')){
						return XWIN;
					}
				}
			}
		}
	}

	//	세로 검사 X
	for(int i=0;i<4;i++){
		if((matrix[0][i]=='X')||(matrix[0][i]=='T')){
			if((matrix[1][i]=='X')||(matrix[1][i]=='T')){
				if((matrix[2][i]=='X')||(matrix[2][i]=='T')){
					if((matrix[3][i]=='X')||(matrix[3][i]=='T')){
						return XWIN;
					}
				}
			}
		}
	}

	//	대각선 검사 X
	if((matrix[0][0]=='X')||(matrix[0][0]=='T')){
		if((matrix[1][1]=='X')||(matrix[1][1]=='T')){
			if((matrix[2][2]=='X')||(matrix[2][2]=='T')){
				if((matrix[3][3]=='X')||(matrix[3][3]=='T')){
					return XWIN;
				}
			}
		}
	}
	if((matrix[0][3]=='X')||(matrix[0][3]=='T')){
		if((matrix[1][2]=='X')||(matrix[1][2]=='T')){
			if((matrix[2][1]=='X')||(matrix[2][1]=='T')){
				if((matrix[3][0]=='X')||(matrix[3][0]=='T')){
					return XWIN;
				}
			}
		}
	}

	//	가로행 검사 O
	for(int i=0;i<4;i++){
		if((matrix[i][0]=='O')||(matrix[i][0]=='T')){
			if((matrix[i][1]=='O')||(matrix[i][1]=='T')){
				if((matrix[i][2]=='O')||(matrix[i][2]=='T')){
					if((matrix[i][3]=='O')||(matrix[i][3]=='T')){
						return OWIN;
					}
				}
			}
		}
	}

	//	세로 검사 O
	for(int i=0;i<4;i++){
		if((matrix[0][i]=='O')||(matrix[0][i]=='T')){
			if((matrix[1][i]=='O')||(matrix[1][i]=='T')){
				if((matrix[2][i]=='O')||(matrix[2][i]=='T')){
					if((matrix[3][i]=='O')||(matrix[3][i]=='T')){
						return OWIN;
					}
				}
			}
		}
	}

	//	대각선 검사 O
	if((matrix[0][0]=='O')||(matrix[0][0]=='T')){
		if((matrix[1][1]=='O')||(matrix[1][1]=='T')){
			if((matrix[2][2]=='O')||(matrix[2][2]=='T')){
				if((matrix[3][3]=='O')||(matrix[3][3]=='T')){
					return OWIN;
				}
			}
		}
	}
	if((matrix[0][3]=='O')||(matrix[0][3]=='T')){
		if((matrix[1][2]=='O')||(matrix[1][2]=='T')){
			if((matrix[2][1]=='O')||(matrix[2][1]=='T')){
				if((matrix[3][0]=='O')||(matrix[3][0]=='T')){
					return OWIN;
				}
			}
		}
	}


	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(matrix[i][j]=='.')
				return NOTCOM;
		}
	}

	return DRAW;

	
}

int main(){
	int howMany=0;
	char matrix[4][4];
	string str;

	ifstream fin("A-small-attempt0.in");
	ofstream out("A-small-attempt0.out");

	fin>>howMany;
	for(int k=0; k<howMany;k++){
		for(int i=0;i<4;i++){
			fin>>str;
			//cout<<"test :"<<str<<endl;	//	debug code
			matrix[i][0] = str[0];
			matrix[i][1] = str[1];
			matrix[i][2] = str[2];
			matrix[i][3] = str[3];
		}
		out<<"Case #"<<(k+1)<<": ";
		switch(getResult(matrix)){
			case XWIN:
				out<<"X won"<<endl;
				break;
			case OWIN:
				out<<"O won"<<endl;
				break;
			case DRAW:
				out<<"Draw"<<endl;
				break;
			case NOTCOM:
				out<<"Game has not completed"<<endl;
				break;
			default:
				break;
		}
	}

	return 0;
}