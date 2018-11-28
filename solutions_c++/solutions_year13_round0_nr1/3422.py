
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <string>

using namespace std;


int main(){

	ifstream in;
	in.open("testlarge.in");
	
	ofstream out;
	out.open("out.txt");
	
	int T;
	in>>T;
	
	int x[4][4];
	int o[4][4];
	
	
	for(int u=0;u<T;u++){
		
		int total = 0;
		for(int i=0;i<4;i++){
			string s;
			in>>s;
			for(int j=0;j<4;j++){
				if(s[j]=='.'){
					x[i][j] = 0;
					o[i][j] = 0;
				}
				else{
					total++;
					if(s[j] =='X'){
						x[i][j]=1;
						o[i][j]=0;
					}
					else if(s[j] == 'O'){
						x[i][j]=0;
						o[i][j]=1;
					}
					else{
						x[i][j]=1;
						o[i][j]=1;
					}
				}
			}

		}
		
		int xwon = 0;
		int owon = 0;
		
		for(int i=0;i<4;i++){
			int xrow=0;
			int orow=0;
			for(int j=0;j<4;j++){
				if(x[i][j]) xrow++;
				if(o[i][j]) orow++;
			}
			if(xrow == 4) xwon = 1;
			if(orow == 4) owon = 1;
		}
		
		for(int i=0;i<4;i++){
			int xcol=0;
			int ocol=0;
			for(int j=0;j<4;j++){
				if(x[j][i]) xcol++;
				if(o[j][i]) ocol++;
			}
			if(xcol == 4) xwon = 1;
			if(ocol == 4) owon = 1;
		}
		
		int xdiag = 0;
		int odiag = 0;
		for(int i=0;i<4;i++){
			if(x[i][i]) xdiag++;
			if(o[i][i]) odiag++;
		}
		if(xdiag == 4) xwon = 1;
		if(odiag == 4) owon = 1;
		
		xdiag = 0;
		odiag = 0;
		for(int i=0;i<4;i++){
			if(x[i][3-i]) xdiag++;
			if(o[i][3-i]) odiag++;
		}
		if(xdiag == 4) xwon = 1;
		if(odiag == 4) owon = 1;
		
		//print results
		if(xwon && owon) cout<<"WTF"<<endl;
		
		out<<"Case #"<<(u+1)<<": ";
		if(xwon) out<<"X won"<<endl;
		else if(owon) out<<"O won"<<endl;
		else if(total==16) out<<"Draw"<<endl;
		else out<<"Game has not completed"<<endl;	
		
    }
	in.close();
	out.close();
	
    return 0;
}




