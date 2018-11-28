#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main(){
	int n,s,q,i,j;
	string t;
	cin >> n;
	for (i=0;i<n;i++) {
		vector<string> eng;
		int sw=0;
		cin >> s;
		getline(cin,t);
		for (j=0;j<s;j++) {
			getline(cin,t);
			eng.push_back(t);
		}
		cin >> q;
		getline(cin,t);
		map<string,int> flag;
		int count=0;
		for (j=0;j<q;j++) {
			getline(cin,t);
			if (flag[t]==0) {
				count++;
				if (count>=eng.size()) {
					flag.clear();
					sw++;
					count=1;
				}
			}
			flag[t]=1;
		}
		cout << "Case #" <<  (i+1) << ": " << sw << endl;
	}
}

