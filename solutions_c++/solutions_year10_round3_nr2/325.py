#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#define MAX 1005

using namespace std;

int power(int base, int exp) {
	if(exp==1)
		return base;
	return base*power(base,exp-1);
}

int main() {
	int T,L,P,C,ct,aux;
	cin >> T;
	for(int c=1;c<=T;c++) {
		cin >> L >> P >> C;
		if(L*C >= P) {
			cout << "Case #" << c << ": 0" << '\n';
			continue;
		}
		ct=1;
		aux=L*power(C,2);
		while(aux<P) {			
			aux*=power(C,power(2,ct));
			ct++;
		}
		cout << "Case #" << c << ": " << ct << '\n';
	}
	return 0;
}
