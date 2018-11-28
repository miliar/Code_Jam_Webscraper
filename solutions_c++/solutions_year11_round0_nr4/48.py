//#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
ifstream cin("D-large.in");
ofstream cout("D-large.out");
int main() {
int T;
cin >> T;
for (int t=1; t<=T; t++) {
vector<int> theorder;
vector<int> copy;
	int N;
	cin >> N;
	for (int i=0; i<N; i++) {
		int s;
		cin >> s;
		theorder.push_back(s);
	}
	copy = theorder;
	sort(copy.begin(),copy.end());
	int total =0;
	for (int i=0; i<theorder.size(); i++)
	if (theorder[i] == copy[i]) total++;
	
	int left =(theorder.size() - total);
	cout << "Case #"<<t<<": "<<left<<".000000"<< endl;
}
return 0;
}
