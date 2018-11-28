#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <sstream>
using namespace std;

int solve(string str){
	int Bt=0,Ot=0,T=0;
	float Op=1,Bp=1;
	stringstream s(str);
	int N;
	s>>N;
	for(int i=0;i<N;i++){
		char C;
		float pos;
		s>>C>>pos;
		if(C=='O'){
			int et=T-Ot;
			int rt=abs(pos-Op);
			if(rt<=et) {
				T++;
				Ot=T;
				Op=pos;
			}
			else {
				T+=rt-et;
				T++;
				Ot=T;
				Op=pos;
			}
		}
		else {
			int et=T-Bt;
			int rt=abs(pos-Bp);
			if(rt<=et) {
				T++;
				Bt=T;
				Bp=pos;
			}
			else {
				T+=rt-et;
				T++;
				Bt=T;
				Bp=pos;
			}
		}
	}
	return T;
}

int main(){
	int T;
	fstream ps("statement.txt");
	fstream output("output.txt",fstream::trunc | fstream::out);
	ps>>T;
	int i=1;
	while(i!=T+1){
		string str;
		do {
			getline(ps,str);
		}while(str=="");
		output<<"Case #"<<i<<": "<<solve(str)<<endl;
		i++;	
	}		
	return 0;
}	
