#include<iostream>
#include<algorithm>
#include<string>
#include<stdio.h>
using namespace std;
char a[256];

string x[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
string y[3] = {"our language is impossible to understand",
"there are twenty six factorial possibilities", 
"so it is okay if you want to just give up"};
void process() {
	for(int i=0;i<3;i++) {
		for(int j=0;j<x[i].size();j++) {
			a[x[i][j]] = y[i][j];
		}
		a['q'] = 'z';
		a['z'] = 'q';
	}
}

void print(char *s, int len) {
	for(int i=0;i<len;i++) {
		printf("%c", a[s[i]]);
	}
	printf("\n");
}
int main() {
	process();
	char a[111];
	int n;
	scanf("%d", &n);
	string s;
	getline(cin, s);
	for(int i=0;i<n;i++) {
		gets(a);
		int len = strlen(a);
		printf("Case #%d: ", i + 1);
		print(a, len);
	}
}

