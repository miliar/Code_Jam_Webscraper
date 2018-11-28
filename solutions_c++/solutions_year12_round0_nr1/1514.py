#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
using namespace std;

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define PI 2*acos(0)
#define EPS 1e-7
#define LL long long
#define INF 1000000000
#define PQ priority_queue

typedef pair<int, int> i2;
typedef pair<int, i2> i3;
typedef pair<i2, i2> i4;

map<char, char> peta;
int len, tc;
char line[105];

map<char, char> generate_mapping() {
	
	string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv a zoo";
	string s2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up y qee";
	
	map<char, char> res;
	bool used[26];
	for (int i = 0; i < 26; i++) used[i] = false;
	
	int len = s1.size();
	for (int i = 0; i < len; i++)
		if (!res.count(s1[i])) res[s1[i]] = s2[i], used[s2[i] - 'a'] = true;
	
	for (int i = 0; i < 26; i++)
		if (!used[i]) res['q'] = (char) (i + 'a');
	
	return res;
}

int main() {

	//freopen("file.in", "r", stdin);
	
	peta = generate_mapping();
	
	/*
	for (map<char, char>::iterator it = peta.begin(); it != peta.end(); it++)
		printf("%c -> %c\n", it->first, it->second);
	*/
	
	scanf("%d\n", &tc);
	for (int t = 1; t <= tc; t++) {
		printf("Case #%d: ", t);
		gets(line);
		len = strlen(line);
		for (int i = 0; i < len; i++)
			printf("%c", peta[line[i]]);
		printf("\n");
	}
	
	return 0;
}
