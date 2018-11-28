//code by Carlo Piovesan
//Google Code Jam, round 2, problem A

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
		int N;
		FILE>>N;
		string S;
		vector <int> LAST(N);
//		vector <int> HOWMANY(N,0);
		for (int j=0; j<N; j++) {
			FILE>>S;
			int last=0;
			for (int i=0; i<N; i++) if (S[i]=='1') last=i;
			LAST[j]=last;
//			HOWMANY[last]++;
			}
		
//		vector <int> A;
//		for (int j=0; j<N; j++) A.push_back(LAST[j]);
//		sort(A.begin(), A.end());
		
		int COUNT=0;
//			for (int iii=0; iii<N; iii++) cout<<LAST[iii]<<"\t";
//			cout<<"\n";		

		for (int i=0; i<N; i++) {
			bool K=true;
			for (int j=i; K && j<N; j++) if (LAST[j]<=i) {
				K=false;
				for (int ii=j-1; ii>=i; ii--) {
					swap(LAST[ii], LAST[ii+1]);
					COUNT++;
					}
				}
//			for (int iii=0; iii<N; iii++) cout<<LAST[iii]<<"\t";
//			cout<<"\t\t"<<COUNT<<"\n";		
			}
//					system("PAUSE");
//					cout<<"\n";
		OUT<<"Case #"<<ZZZ<<": "<<COUNT<<"\n";
		}
	FILE.close();
	OUT.close();
	return 0;
	}
