#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

int main (void) {
    ofstream OUT;
    OUT.open ("OU.txt");
    ifstream FILE("IN.txt");
    int Num;
    FILE>>Num;
	for (int z=1; z<=Num; z++) {
		int N;
		FILE>>N;
		vector <long long> a(N);
		vector <long long> b(N);
		for (int i=0; i<N; i++) FILE>>a[i];
		for (int i=0; i<N; i++) FILE>>b[i];
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		reverse(b.begin(), b.end());
		long long res=0;
		for (int i=0; i<N; i++) res+=a[i]*b[i];
		OUT<<"Case #"<<z<<": "<<res<<"\n";
		}
    FILE.close();
    OUT.close();
    system("PAUSE");
    return 0;
    }
