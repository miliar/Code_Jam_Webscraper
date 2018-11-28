#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>
#include<complex>
#include<set>
using namespace std;
#define MP make_pair
#define F first
#define S second
#define PB push_back
string Input[3];
string Output[3];
char Map[26];
bool exist[26];
int main() {
	freopen("A.inp", "r", stdin);
	freopen("A.out", "w", stdout);
	Input[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	Output[0] = "our language is impossible to understand";
	Input[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	Output[1] = "there are twenty six factorial possibilities";
	Input[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	Output[2] = "so it is okay if you want to just give up";		
	memset(exist, 0, sizeof(exist));
	for(int i = 0; i < 3; i ++)
		for(int j = 0; j < Input[i].size(); j ++) {
			if (Input[i][j] == ' ') continue;
			Map[Input[i][j] - 'a'] = Output[i][j]; 
//			cout << Input[i][j] - 26 << " " << exist[Input[i][j] - 26] << endl;
			exist[Input[i][j] - 'a'] = true;
		}
	for(int i = 0; i < 26; i ++) {
		if (!exist[i]) {
//			cout << exist[i] << " "; 
			Map[i] = 'z';
//			cout << i << endl;
		}
	}
	Map['z' - 'a'] = 'q';
	int t;
	scanf("%d\n", &t);
	for(int test = 0; test < t; test ++) {
		string Input;
		getline(cin, Input);
		printf("Case #%d: ", test + 1);		
		for(int i = 0; i < Input.size(); i ++) 
			if (Input[i] != ' ') printf("%c", Map[Input[i] - 'a']);
			else printf(" ");
		if (test != t - 1) printf("\n");
	}
	return 0;
}
