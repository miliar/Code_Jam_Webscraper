#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

int map[26];
string x;

int main() {
	string inp[3];
	string oup[3];
	inp[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	inp[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	inp[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	oup[0] = "our language is impossible to understand";
	oup[1] = "there are twenty six factorial possibilities";
	oup[2] = "so it is okay if you want to just give up";
	
	for (int i = 0; i < 26; i++) 
		map[i] = -1;
	
	map['q' - 97] = 'z' - 97;
	map['z' - 97] = 'q' - 97;
		
	for (int i = 0; i < 3; i++) 
		for (int j = 0; j < inp[i].size(); j++) {
			if (inp[i][j] == ' ') continue;
			map[inp[i][j] - 97] = oup[i][j] - 97;
		}
		
	int t;
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	cin >> t;
	getline(cin, x);
	for (int i = 0; i < t; i++) {
		getline(cin,x);
		printf("Case #%d: ", i + 1);
		for (int j = 0; j < x.size(); j++)
			if (x[j] == ' ') printf(" ");
		else
			printf("%c", map[x[j] - 97] + 97);
		printf("\n");
	}
	//fclose(stdin);
	//fclose(stdout);
	return 0;
}