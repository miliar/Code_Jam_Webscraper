#include<iostream>
#include<fstream>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<stack>
#include<queue>
#include<sstream>

using namespace std;

int gcd(int a, int b){
	if(b==0){
		return a;
	} else{
		return gcd(b, a%b);
	}
}

int main(){

	ifstream entrada("A-large.in");
	ofstream salida("A-large.out");

	int Casos;
	entrada >> Casos;
	for(int caso=1;caso<=Casos;++caso){
		string res = "Broken";
		long long int N;
		int Pd;
		int Pg;
		entrada >> N >> Pd >> Pg;
		if(Pg != 100){
			if(Pg == 0){
				if(Pd == 0){
					res = "Possible";
				}
			}else{
				int aux = 100;
				aux /= gcd(100, Pd);
				if(aux <= N){
					res = "Possible";
				}
			}
		}else{
			if(Pd == 100){
				res = "Possible";
			}
		}
		salida << "Case #" << caso << ": " << res << endl;
	}
	return 0;
}
