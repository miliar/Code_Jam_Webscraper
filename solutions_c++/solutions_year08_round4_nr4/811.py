#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

string s;
int ans, len, k;

void calc(string s2) {
	int j, temp = 1;
	for (j=1; j < len; j++)
		if (s2[j] != s2[j-1])
			temp++;
	if (temp < ans)
		ans = temp;
}

void apply(vector <int> v) {
	string nova = "";
	for (int i=0; i < len; i++)
		nova += s[(i/k)*k + v[i%k]];
	calc(nova);
}

int main() {
	int cases, t = 1;
	
	scanf("%d",&cases);
	while (cases--) {
		scanf("%d\n",&k);
		vector <int> v(k);
		cin >> s;
		
		ans = len = s.length();
		for (int i=0; i < k; i++)
			v[i] = i;
		do {
			apply(v);
		} while (next_permutation(v.begin(),v.end()));
		
		printf("Case #%d: %d\n",t++,ans);
	}
	
	return 0;
}
