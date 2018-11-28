#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip.h>
#include <string>
using namespace std;

int GCD(int a, int b){
		if (b==0) return a;
		return GCD(b, a%b);
}

void print(int n, bool possible){
		cout<<"Case #"<<n<<": ";
		if (possible)
				cout<<"Possible"<<endl;
		else 
				cout<<"Broken"<<endl;
}
int main(int argc, char *argv[]){
		ifstream ins;
		ins.open(argv[1]);
		int Ncase;
		ins>>Ncase;
		int the_case = 0;
		while (the_case++ < Ncase){
				long N;
				int pd, pg;
				bool possible = false;
				ins>>N>>pd>>pg;
				if ( pg == 0) {
						if (pd == 0 ) {
								possible = true;
						} else possible = false;
						print(the_case, possible);
						continue;
				}
				if ( pg == 100){
						if (pd == 100 ){
						possible = true;
						} else possible = false;
						print(the_case, possible);
						continue;
				}
				if (N>100){
						possible = true;
						print(the_case, possible);
						continue;
				}
				if (100/GCD(100, pd)<= N){
						possible = true;
						print(the_case, possible);
						continue;
				}
				print(the_case, false);
		}
		ins.close();
		return 0;
}

