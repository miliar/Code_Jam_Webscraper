#include<algorithm>
#include<cmath>
#include<iomanip>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main(){
	ifstream entrada("C-large.in");
    ofstream salida("C-large.out");
    int t;
    int r;
    int k;
    int n;
    unsigned long long int res;
    entrada >> t;
    for(int i=1;i<=t;++i){
		res = 0;
		entrada >> r >> k >> n;
		unsigned long long int grupos[n];
		unsigned long long int euros[n];
		unsigned long long int prox[n];
		for(int j=0;j<n;++j){
			entrada >> grupos[j];
		}
		for(int j=0;j<n;++j){
			int act;
			act = j+1;
			if(j+1==n){
				act = 0;
			}
			unsigned long long int plata = grupos[j];
			while((plata + grupos[act] <= k) && (act!=j)){
				plata += grupos[act];
				act++;
				if(act==n){
					act=0;
				}
			}
			euros[j] = plata;
			prox[j] = act;
		}
		int actual = 0;
		for(int j=1;j<=r;++j){
			res += euros[actual];
			actual = prox[actual];
		}
		salida << "Case #" << i << ": " << res << endl;
	}
	
}
