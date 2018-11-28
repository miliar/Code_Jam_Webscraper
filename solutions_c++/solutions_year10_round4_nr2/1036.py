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

int resolver(int* m, int l, int h, int p);

int main(){
	ifstream entrada("B-small.in");
    ofstream salida("B-small.out");
    int t;
    int res;
    int p;
    int aux;
    int aux2;
    int bas;
    entrada >> t;
    for(int i=1;i<=t;++i){
		res = 0;
		entrada >> p;
		aux = 1;
		//cout << "p: " << p << endl;
		for(int j=1;j<=p;++j){
			aux *= 2;
		}
		//cout << aux << endl;
		
		
		int m[aux];
		for(int j=0;j<aux;++j){
			entrada >> m[j];
			//cout << m[j];
		}
		//cout << endl;
		aux2 = aux/2;
		for(int j=0;j<p;++j){
			for(int h=0;h<aux2;++h){
				entrada >> bas;
			}
			aux2 /= 2;
		}
		
		
		//cout << "primera: "  << "l: " << 0 << " h: " << aux << " p: " << p << endl;
		res = resolver(m, 0, aux, p);
		salida << "Case #" << i << ": " << res << endl;
	}
}


int resolver(int* m, int l, int h, int p){
	int res = 0;
	if(p>0){
		bool ok = true;
		
		//cout << "l: " << l << " h: " << h << " p: " << p << endl;
		
		for(int i=l;i<h;++i){
			//cout << "estoy" << endl;
			//cout << m[i] << " ";
			if(m[i]<p){
				ok = false;
				break;
			}
		}
		//cout << endl;
		
		if(!ok){
			res = 1 + resolver(m, l, ((h-l)/2)+l, p-1) + resolver(m, ((h-l)/2)+l, h, p-1);
		}
		//cout << endl;
		//cout << "Esto es res: " << res << endl;
	}
	return res;
}
