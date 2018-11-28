#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int len(int n) {
	int i=0;
	while(n) n = n/10, ++i;
	return i;
}

int toInt(vector<int> &v) {
	int result = 0;
	for(int i=0; i<v.size(); ++i) {
		//printf("%d", v[i]);
		result = (result*10) + v[i];
	}
	//printf("\n");
	return result;
}

bool cmp(string str1, string str2) {
	while(str2.size() != str1.size()) {
		str2.insert(str2.begin(),'0');
	}
	return str1 > str2;
}

int answer(string str) {
	string digits = str;
	string ant = digits;
	vector<bool> mark(10, false);
	for(int i=0; i<str.size(); ++i) {
		mark[str[i]-'0'] = true;
	}
	int mini = 0;
	for(int i=1; i<mark.size(); ++i) {
		if(!mark[i]){ mini = i; break; }
	}
	do {
		//printf("%s\n", digits.c_str());
		if(!next_permutation(digits.begin(), digits.end())){
			ant.insert(ant.begin(), '0');
//			sort(ant.begin(), ant.end());
			digits = ant;
		}
		ant = digits;
		//printf("%d\n", digits<str);
	}while(!cmp(digits, str));
	printf("%s\n", digits.c_str());
}

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int t; scanf("%d", &t);
	for(int ic=0; ic<t; ++ic) {
		char buff[1024]; scanf("%s", buff);
		printf("Case #%d: ", ic+1);
		answer(string(buff));
		fflush(stdout);
	}
	return 0;
}
