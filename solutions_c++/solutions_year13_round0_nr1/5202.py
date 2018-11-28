#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ofstream fout ("solution.txt");
	ifstream fin ("in.txt");
	
	int t;cin>>t;
	char p [4][4];
	for(int i (0);i!=t;++i){
		
		for(int j (0);j!=4;++j){
			for(int k (0);k!=4;++k){
				cin>>p[j][k];
			}
		}
		
		
		char c='X';
		bool nedok=0, iks=0, X=0, OO=0;
		
		//
		for(int j (0);j!=4;++j){
			int stej=0;
			for(int k (0);k!=4;++k){
				if(p[j][k]=='.')nedok=1;
				if(p[j][k]==c or p[j][k]=='T')++stej;
			}
			if(stej==4)iks=1;
		}
		for(int k (0);k!=4;++k){
			int stej=0;
			for(int j (0);j!=4;++j){
				if(p[j][k]=='.')nedok=1;
				if(p[j][k]==c or p[j][k]=='T')++stej;
			}
			if(stej==4)iks=1;
		}
		
		int stej=0;
		for(int j (0);j!=4;++j){
			if(p[j][j]=='.')nedok=1;
			if(p[j][j]==c or p[j][j]=='T')++stej;
			
			if(stej==4)iks=1;
		}
		
		stej=0;
		for(int j (0);j!=4;++j){
			if(p[j][3-j]=='.')nedok=1;
			if(p[j][3-j]==c or p[j][3-j]=='T')++stej;
			
			if(stej==4)iks=1;
		}
		X=iks;
		/////////////
		c='O';iks=0;
		for(int j (0);j!=4;++j){
			int stej=0;
			for(int k (0);k!=4;++k){
				if(p[j][k]=='.')nedok=1;
				if(p[j][k]==c or p[j][k]=='T')++stej;
			}
			if(stej==4)iks=1;
		}
		for(int k (0);k!=4;++k){
			int stej=0;
			for(int j (0);j!=4;++j){
				if(p[j][k]=='.')nedok=1;
				if(p[j][k]==c or p[j][k]=='T')++stej;
			}
			if(stej==4)iks=1;
		}
		
		stej=0;
		for(int j (0);j!=4;++j){
			if(p[j][j]=='.')nedok=1;
			if(p[j][j]==c or p[j][j]=='T')++stej;
			
			if(stej==4)iks=1;
		}
		
		stej=0;
		for(int j (0);j!=4;++j){
			if(p[j][3-j]=='.')nedok=1;
			if(p[j][3-j]==c or p[j][3-j]=='T')++stej;
			
			if(stej==4)iks=1;
		}
		OO=iks;
		///////
		
		fout<<"Case #"<<i+1<<": ";
		if(X)fout<<"X won";
		else if(OO)fout<<"O won";
		else if(nedok)fout<<"Game has not completed";
		else fout<<"Draw";
		fout<<endl;
		
		
		
	}
}
