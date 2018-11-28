//code by Carlo Piovesan
//GCJ 2009, qualification Round, problem C

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
	int Num;
	FILE>>Num;
	
	char AA[50];
	FILE.getline(AA, 45);
	
	string S="Xwelcome to code jam";
	for (int z=1; z<=Num; z++) {
		//input
		char A[600];
		FILE.getline(A, 550);
		
		vector <int> B(20, 0);
		B[0]=1;
		int CURR=0;
		while (A[CURR]!='\0') {
			for (int i=19; i>=1; i--) if (A[CURR]==S[i]) B[i]=(B[i]+B[i-1])%10000;
			CURR++;
			}
		
		//output
		OUT<<"Case #"<<z<<": "<<(B[19]/1000)%10<<(B[19]/100)%10<<(B[19]/10)%10<<B[19]%10<<"\n";
        	}
    FILE.close();
    OUT.close();
    return 0;
    }
