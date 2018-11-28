//code by Carlo Piovesan
//GCJ 2009, qualification Round, problem A

#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

int main (void) {
	ofstream OUT;
	OUT.open ("OUT.txt");
	ifstream FILE("IN.txt");
	
	//input
	int L,D,N;
	FILE>>L>>D>>N;
	vector <string> W(D);
	for (int i=0; i<D; i++) FILE>>W[i];
	vector <string> X(N);
	for (int i=0; i<N; i++) FILE>>X[i];
	
	vector <int> NUM(N, 0);

	for (int i=0; i<D; i++) for (int j=0; j<N; j++) {
		int a=0;
		bool flag=false;
		bool par=false;
		bool canbe=true;
		
		for (int b=0; b<X[j].size(); b++) {
			if (X[j][b]=='(') {
				par=true;
				flag=false;
				}
			else if (X[j][b]==')') {
				par=false;
				if (flag==false) canbe=false;
				a++;
				}
			else if (X[j][b]==W[i][a]) {
				if (par==true) flag=true;
				else a++;
				}
			else if (par==false) canbe=false;
			}
		if (canbe) NUM[j]++;
		}
	
	//output
	for (int i=0; i<N; i++) OUT<<"Case #"<<i+1<<": "<<NUM[i]<<"\n";
	
	FILE.close();
	OUT.close();
	return 0;
	}
