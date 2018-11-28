//#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

ifstream cin("B-large.in");
ofstream cout("B-large.out");

int main () {
	int Sc[31][2] = {0};
	for (int i=0; i<=10; i++)
		for (int j=0; j<=10; j++)
			for (int k=0; k<=10; k++) {
				if (abs(i-j)<2 && abs(j-k)<2 && abs(i-k)<2)
					Sc[i+j+k][0] = max(Sc[i+j+k][0], max(max(i,j),k));
				else if (abs(i-j)<=2 && abs(j-k)<=2 && abs(i-k)<=2)
					Sc[i+j+k][1] = max(Sc[i+j+k][1], max(max(i,j),k));
			}
				
	int T; cin >> T >> ws;
	for (int t=0; t<T; t++) {
		int N, S, p; cin >> N >> S >> p;
		int cnt = 0;
		for (int i=0; i<N; i++) {
			int t; cin >> t;
			if (Sc[t][0] >= p) cnt++;
			else if (Sc[t][1] >= p && S>0) {cnt++; S--;}
		}
		cout << "Case #" << t+1 << ": " << cnt << endl;
	}
}
