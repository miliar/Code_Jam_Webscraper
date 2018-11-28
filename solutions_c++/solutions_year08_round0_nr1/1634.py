#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

void tc(int cn) {
	int s,q;
	cin>>s;
	vector<int> words(q);
	string tmp;
	getline(cin,tmp);
	map<string, int> dict;
	for (int i=0;i<s;i++) {
		getline(cin,tmp);
		dict[tmp]=i;
	}
	cin>>q;
	getline(cin,tmp);
	for (int i=0;i<q;i++) {
		getline(cin,tmp);
		words[i] = dict[tmp];
	}
	int cnt = 0;
	vector<int> seen(s);
	int ns = 0;
	for (int i=0;i<q;i++) {
		ns += 1 - seen[words[i]];
		seen[words[i]] = 1;
		if (ns == s) {
//			cout << "Switching away from engine " << words[i] <<endl;
			fill(seen.begin(),seen.end(),0);
			cnt++;
			seen[words[i]]=1;
			ns = 1;
		}
	}
	cout << "Case #"<<cn<<": "<<cnt<<endl;
}
int main() {
	int n;
	cin>>n;
	for (int i=0;i<n;i++){
		cerr << i<<endl;
		tc(i+1);
	}
}