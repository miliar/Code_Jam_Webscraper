#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

void dostep(int t) {
	int combine[26][26];
	bool opposed[26][26];
	for (int i=0;i<26;i++)for(int j=0;j<26;j++){combine[i][j]=-1;opposed[i][j]=false;}
	

	int c;
	cin >> c;
	for (int i=0;i<c;i++) {
		string com;
		cin >> com;
		combine[com[0]-'A'][com[1]-'A']=com[2]-'A';
		combine[com[1]-'A'][com[0]-'A']=com[2]-'A';
	}
	cin >> c;
	for(int i=0;i<c;i++) {
		string opp;
		cin >> opp;
		opposed[opp[0]-'A'][opp[1]-'A']=true;
		opposed[opp[1]-'A'][opp[0]-'A']=true;
	}
	string str;
	cin >> c;
	cin >> str;
	
	vector<int> q;
	for (int i=0;i<str.size();i++) {
		int c = str[i]-'A';
		if (q.size()==0) {
			q.push_back(c);
			continue;
		}
		int a = combine[q[q.size()-1]][c];
		if (a != -1) {
			q[q.size()-1] = a;
			continue;
		}
		bool clear = false;
		for (int j=0;j<q.size();j++) {
			if (opposed[q[j]][c]) {
				q.clear();
				clear = true;
				break;
			}
		}
		if (clear) continue;
		q.push_back(c);
	}
	
        cout << "Case #" << t << ": [";
	for (int i=0;i<q.size();i++) {
		if (i != 0) cout << ", ";
		cout << ((char)(q[i]+'A'));
	}
        cout << "]" << endl;
}

int main() {
        int n;
        cin>>n;
        for (int i=1;i<=n;i++)dostep(i);
        return 0;
}
