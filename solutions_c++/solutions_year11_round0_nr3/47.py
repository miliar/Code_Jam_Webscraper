//#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
ifstream cin("C-large.in");
ofstream cout("C-large.out");
int main() {
int T;
cin >> T;
for (int t=1; t<=T; t++) {
int N;
cin >> N;
int C;
vector<int> theC;
cin >> C;
theC.push_back(C);
int thexor = C;
int thesum = 0;
for (int i=1; i<N; i++) {
	cin >> C;
	thexor ^= C;
	theC.push_back(C);
}
sort(theC.begin(), theC.end());
cout << "Case #"<<t<<": ";
if (thexor == 0) {
	for (int i=1; i<theC.size(); i++)
		thesum += theC[i];
	cout << thesum;
} else
cout << "NO";

cout << endl;
}
return 0;
}
