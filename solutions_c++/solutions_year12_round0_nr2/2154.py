//============================================================================
// Name        : CodeJam.cpp
// Author      : Daniel Rubio
// Version     : 1.0
// Copyright   : FreeWare
// Description : CodeJam 2011 - Qualification 1
//============================================================================

#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
using namespace std;

int main(){
	freopen("d:\\Downloads\\B-large.in", "rt", stdin);
	freopen("d:\\Downloads\\B-large.out", "wt", stdout);

	//declaramos variables
	int T;
	int googlers;
	int valor;
	int surprising;
	int max;
	int results;

	//repeticiones
	cin >> T ;
	for(int r=0;r<T;r++){
		cout << "Case #" << r+1 << ": ";
		cerr << "Case #" << r+1 << ": ";

		results = 0;

		cin >> googlers;
		cin >> surprising;
		cin >> max;
		for(int i = 0; i < googlers ; i++){
			cin >> valor;
			if(max==0){
				results++;
			}else if(valor >= max*3-2){
				results++;
			}else if(valor >= max*3-4 && surprising>0 && valor !=0){
				surprising--;
				results++;
			}
		}

		cout << results << endl;
		cerr << results << endl;

	}
}
