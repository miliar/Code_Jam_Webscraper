#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime> 
using namespace std;

int main() {
	map<char,char> mp;
	mp['a']='y';
	mp['o']='e';
	mp['z']='q';
	mp['q']='z';	

	ifstream fin ("dict.txt");
	vector<string> a,b;

	string line;
	for (int i=0; i<3; i++) {
		getline(fin, line);
		a.push_back(line);
	}

	for (int i=0; i<3; i++) {
		getline(fin, line);
		b.push_back(line);
	}
	
	for (int i=0; i<3; i++) {
		string s=a[i], t=b[i];
		int sz=s.size();
		for (int j=0; j<sz; j++) mp[s[j]]=t[j];
	}

	fin.close();

	int t;
	getline(cin, line);
	stringstream ss(line); ss>>t;
	for (int i=0; i<t; i++) {
		getline(cin, line);
		int sz=line.size();
		string ans;
		for (int j=0; j<sz; j++) ans+=mp[line[j]];
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}
