#include <iostream>
#include <stdio.h>
#include <set>
#include <vector>

using namespace std;

int N;

int main() {
	cin>>N;
	for(int i=0;i<N;i++) {
		int s,q,ret(0);
		set<string> a;
		string tmp;
		cin >> s;
		cin.ignore(100,'\n');
		for(int j=0;j<s;j++) getline(cin,tmp);
		cin >> q;
		cin.ignore(100,'\n');
		for(int j=0;j<q;j++) {
			getline(cin,tmp);
			a.insert(tmp);
			if(a.size()==s) {
				a.clear();
				a.insert(tmp);
				ret++;
			}
		}
		printf("Case #%d: %d\n",i+1,ret);
	}
	return 0;
}
