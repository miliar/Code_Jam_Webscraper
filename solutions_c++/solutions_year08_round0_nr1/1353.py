#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
#include <utility>
#include <cmath>
using namespace std;

#define foreach(I,S) for (typeof((S).begin()) I=(S).begin();(I)!=(S).end();++(I))

int main() {
	int N;
	cin >> N;
	for (int t=1;t<=N;++t) {
		int S;
		cin >> S;
		string dummy;
		getline(cin,dummy);
		map<string,bool> vist;
		for (int i=0;i<S;++i) {
			string s;
			getline(cin,s);
			vist[s]=false;
		}
		int Q;
		cin >> Q;
		int nswitches=0;
		int navail=S;
		getline(cin,dummy);
		string last="";
		for (int i=0;i<Q;++i) {
			string s;
			getline(cin,s);
			if (!vist[s]) {
				vist[s]=true;
				navail--;
				if (navail==0) {
					nswitches++;
					navail=S-1;
					foreach(it,vist) it->second=false;
					vist[s]=true;
				}
			}
		}
		cout << "Case #" << t << ": " << nswitches << endl;
	}
}
