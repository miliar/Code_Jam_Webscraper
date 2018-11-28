//code by Carlo Piovesan
//Google Code Jam, round 1B, problem B (large set)

#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <set>

using namespace std;

int main (void) {
	ofstream OUT;
	OUT.open ("OUT.txt");
	ifstream FILE("IN.txt");
	
	int Num;
	FILE>>Num;
	for (int z=1; z<=Num; z++) {
//		system("PAUSE");
		string A;
		FILE>>A;
//		cout<<A<<"\n";
		vector <int> B(30, 0);
		int size=A.size();
		int k=29;
		int L=size-1;
		while (L>=0) {
			B[k]=A[L]-'0';
			L--;
			k--;
			}
		next_permutation(B.begin(), B.end());
		OUT<<"Case #"<<z<<": ";
		bool f=false;
		for (int i=0; i<30; i++) {
			if (B[i]!=0) f=true;
			if (f) OUT<<(char)(B[i]+'0');
			}

		OUT<<"\n";
		}
//	system("PAUSE");
	FILE.close();
	OUT.close();
//	system("PAUSE");
	return 0;
	}
