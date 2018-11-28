#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <set>
#include <sstream>

using namespace std;

int main (void) {
	ofstream OUT;
	OUT.open ("OU.txt");
	ifstream FILE("IN.txt");
	int Num;
	FILE>>Num;
	for (int z=1; z<=Num; z++) {
		int k;
		string s;
		FILE>>k>>s;
//		cout<<k<<"\n"<<s<<"\n\n";
		vector <int> p(k);
		for (int i=0; i<k; i++) p[i]=i;
		int num=s.size();
		
		do {
			int sum=0;
			char t='5', n;
			int v=0;
			for (int i=0; i<s.size(); i++) {
				v=i/k;
				n=s[v*k+p[i%k]];
				if (t!=n) sum++;
				t=n;
				}
			if (sum<num) num=sum;
			} while ( next_permutation (p.begin(),p.end()) ) ;
		
		
		OUT<<"Case #"<<z<<": "<<num<<"\n";
		}
	FILE.close();
	OUT.close();
	system("PAUSE");
	return 0;
	}
