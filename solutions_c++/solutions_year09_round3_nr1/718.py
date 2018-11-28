//#include <iostream>
#include <vector>
#include <map>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;
ifstream cin;
ofstream cout;
map<char,int> zmap;
int main() {
	
	cin.open("A-large.in");
	cout.open("A-large.out");
	
	int N;

	cin >>N;
	ws(cin);
	for (int i=1; i<=N; i++) {
		string temp;
		getline(cin,temp);
		int base=0;
		bool firsttime = false;
		int counter=1;
		for (int j=0; j<temp.length(); j++) {
			if (zmap.find(temp[j]) == zmap.end()) {
				if (counter ==1 && firsttime == false) { zmap[temp[j]] = 1; counter=0; firsttime=true;  } else {
					zmap[temp[j]] = counter++;
					if (counter == 1) { counter++; }
				}
				base++;
			}
		}
		if (base == 1) base = 2;
		long long mx=0;
		for (int j=0; j<temp.length(); j++) {
			mx = mx*base;
			mx += zmap[temp[j]];
		}
		cout <<"Case #"<<i<<": "<<mx<<endl;
		zmap.clear();
	}
}