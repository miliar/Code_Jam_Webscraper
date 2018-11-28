//#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

ifstream cin("C-large.in");
ofstream cout("C-large.out");

int main () {
	int pows[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};
	int T; cin >> T >> ws;
	for (int t=0; t<T; t++) {
		int cnt = 0;
		int A, B; cin >> A >> B;
		map <pair<int,int>, char> M;
		for (int a=A; a<B; a++) {
			for (int i=1; pows[i]<=a; i++) {
				int tens = (a/pows[i]);
				for (int j=1; j<8; j++)
					if (pows[j]>tens) {tens=pows[j]; break;}
				int b = a/pows[i] + (a%pows[i])*tens;
				if (b>a && b<=B && !M.count(make_pair(a,b))) {cnt++; M[make_pair(a,b)]=1;}
			}
		}
		cout << "Case #" << t+1 << ": " << cnt << endl;
	}
}
