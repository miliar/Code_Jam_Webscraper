#include "assert.h"
#include "ctype.h"
#include "float.h"
#include "math.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "stdarg.h"
#include "time.h"
#include "algorithm"
#include "numeric"
#include "functional"
#include "utility"
#include "bitset"
#include "vector"
#include "list"
#include "set"
#include "map"
#include "queue"
#include "stack"
#include "string"
#include "sstream"
#include "iostream"
using namespace std;

int main(){
	int casos;
	cin >> casos;
	for (int caso=0 ; caso<casos ; caso++){
		int tam;
		cin >> tam;
		//cout << tam << endl;
		vector<int> a(tam);
		vector<int> b(tam);
		for (int i=0 ; i<tam ; i++){
			cin >> a[i];
		}
		for (int i=0 ; i<tam ; i++){
			cin >> b[i];
		}
		
		sort(a.begin() , a.end());
		sort(b.begin() , b.end());
		/*
		for (int i=0 ; i<tam ; i++){
			cout << a[i] << " ";
		}
		cout << endl;
		for (int i=0 ; i<tam ; i++){
			//cout << b[i] << " ";
		}*/
		//cout << endl;
		long long resultado=0;
		//cout << resultado << endl;
		for (int i=0 ; i<tam ; i++){
			resultado+=(a[i]*b[tam-i-1]);
			//cout << "Resultado " << resultado << endl;
		}
		cout << "Case #" << (caso+1) << ": " << resultado << endl;
	}
	return 0;
}
