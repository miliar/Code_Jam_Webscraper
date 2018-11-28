#include <iostream>
#include <map>
#include <sstream>
using namespace std;

#define foreach(I,S) for (typeof((S).begin()) I=(S).begin();(I)!=(S).end();++(I))


int parsetime(string s) {
	string hh(s,0,2);
	string mm(s,3,2);
	stringstream hhh(hh);
	stringstream mmm(mm);
	int h,m;
	hhh >> h;
	mmm >> m;
	return h*60+m;
}


int main() {
	int N;
	cin >> N;
	for (int t=1;t<=N;++t) {
		int T;
		cin >> T;
		int NA,NB;
		cin >> NA >> NB;
		map<int,int> a,b;
		for (int i=0;i<NA;++i) {
			string s,ss;
			cin >> s >> ss;
			a[parsetime(s)]++;
			b[parsetime(ss)+T]--;
		}
		for (int i=0;i<NB;++i) {
			string s,ss;
			cin >> s >> ss;
			b[parsetime(s)]++;
			a[parsetime(ss)+T]--;
		}
		int na=0,nb=0;
		int j=0;
		foreach(it,a) {
			j+=it->second;
			na=max(na,j);
		}
		j=0;
		foreach(it,b) {
			j+=it->second;
			nb=max(nb,j);
		}
		cout << "Case #" << t << ": " << na << " " << nb << endl;		
	}
}
