#include <string>
#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
	int cas, cass=0;
	for (scanf("%d", &cas); cas--; ) {
		printf("Case #%d: ", ++cass);
		string s;
		cin>>s;
		if (next_permutation(s.begin(), s.end())) {
			cout<<s<<endl;
		}
		else {
			sort(s.begin(), s.end());
			int i=0;
			while (s[i]=='0') ++i;
			swap(s[i], s[0]);
			cout<<s[0]<<'0'<<s.substr(1, s.size()-1)<<endl;
		}
	}
	return 0;
}
		
