#include <iostream>
#include <fstream>

using namespace std;

int ans[4]={'O'+'O'+'O'+'O','O'+'O'+'O'+'T','X'+'X'+'X'+'X','X'+'X'+'X'+'T'};

inline bool fun(int sum, ofstream &out){
	if(sum==ans[0] || sum==ans[1]){out<<"O won"; return true;}
	if(sum==ans[2] || sum==ans[3]){out<<"X won"; return true;}
	return false;
}

int main(){
	//ifstream cin("A-large.in");
	ofstream out("out.txt");
	int T; cin>>T;
	int sum;
	
	for (int t=1; t<=T; t++){
		out<<"Case #"<<t<<": ";
		int puz[4][4];
		bool incomp=false;
		char c;
		for (int i=0; i<4; i++){
			for (int j=0; j<4; j++){
				cin>>c; puz[i][j]=c;
				if(puz[i][j]=='.')incomp=true;
			}
		}
		
		if(fun(puz[0][0]+puz[0][1]+puz[0][2]+puz[0][3],out));
		else if(fun(puz[1][0]+puz[1][1]+puz[1][2]+puz[1][3],out));
		else if(fun(puz[2][0]+puz[2][1]+puz[2][2]+puz[2][3],out));
		else if(fun(puz[3][0]+puz[3][1]+puz[3][2]+puz[3][3],out));
		else if(fun(puz[0][0]+puz[1][0]+puz[2][0]+puz[3][0],out));
		else if(fun(puz[0][1]+puz[1][1]+puz[2][1]+puz[3][1],out));
		else if(fun(puz[0][2]+puz[1][2]+puz[2][2]+puz[3][2],out));
		else if(fun(puz[0][3]+puz[1][3]+puz[2][3]+puz[3][3],out));
		else if(fun(puz[0][0]+puz[1][1]+puz[2][2]+puz[3][3],out));
		else if(fun(puz[0][3]+puz[1][2]+puz[2][1]+puz[3][0],out));
		else if(incomp){out<<"Game has not completed";}
		else {out<<"Draw";}
		
		
		out<<"\n";
	}
	
	return 0;
}
