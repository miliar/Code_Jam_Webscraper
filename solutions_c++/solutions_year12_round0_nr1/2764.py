#include <string>
#include <string.h>
#include <vector>
#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main() {
	int N, i;
	vector <char> tr (128,'-');
	string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string s4 = "y qee";
	string t1 = "our language is impossible to understand";
	string t2 = "there are twenty six factorial possibilities";
	string t3 = "so it is okay if you want to just give up";
	string t4 = "a zoo";

	for (i = 0; i < s1.length(); i++)
		tr[s1[i]] = t1[i];
	for (i = 0; i < s2.length(); i++)
		tr[s2[i]] = t2[i];
	for (i = 0; i < s3.length(); i++)
		tr[s3[i]] = t3[i];
	for (i = 0; i < s4.length(); i++)
		tr[s4[i]] = t4[i];

	tr[' '] = ' ';
	tr['\0'] = '\0';
	tr['\n'] = '\n';
	tr['z'] = 'q'; // too lazy to program something else just for this one..


	// setup

	scanf("%d", &N);
	getchar(); // \n

	for (int C = 1; C <= N; C++) {
		char in[110], out[110];
		char c;
		int ct = 0;

		while ((c = getchar()) != '\n' && c != '\0')
			in[ct++] = c;
		in[ct] = '\0';

		for (i = 0; i < strlen(in); i++) {
			out[i] = tr[in[i]];
		}
		out[i] = '\0';

		printf("Case #%d: %s\n", C, out);
	}

	return 0;
}

