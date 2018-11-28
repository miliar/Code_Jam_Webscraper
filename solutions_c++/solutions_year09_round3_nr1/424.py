//code by Carlo Piovesan
//Google Code Jam, round 1C, problem A

#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <set>
#include <cmath>

using namespace std;

int main (void) {
	ofstream OUT;
	OUT.open ("OUT.txt");
	ifstream FILE("IN.txt");
	
	int Num;
	FILE>>Num;
	for (int ZZZ=1; ZZZ<=Num; ZZZ++) {
		vector <unsigned long long> A(300, -1);
		
		string S;
		FILE>>S;
		
		unsigned long long c=1;
		for (int i=0; i<S.size(); i++) {
//			cout<<S[i]<<" ";
			
			if (A[(int)S[i]]==-1) {
				A[(int)S[i]]=c;
				if (c==1) c=0;
				else if (c==0) c=2;
				else	c++;
				}
//			cout<<A[(int)S[i]]<<"\n";
			}
//		cout<<c<<"\n";
//		system("PAUSE");
//		cout<<"\n";
		
		if (c<2) c=2;
		
		unsigned long long RES=0;
		
		for (int i=0; i<S.size(); i++) {
			RES*=c;
			RES+=A[(int)S[i]];
			}
		
		OUT<<"Case #"<<ZZZ<<": "<<RES<<"\n";
		}
	FILE.close();
	OUT.close();
	return 0;
	}
