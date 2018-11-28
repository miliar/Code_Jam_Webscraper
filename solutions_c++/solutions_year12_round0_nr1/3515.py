#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

int n, c;
string s;
char res[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main () {
	freopen ("input.in", "r", stdin);
	freopen ("output.out", "w", stdout);
	scanf ("%d\n", &c);
	for (int j = 0; j < c; j++) {
		getline(cin,s);
		n = s.size();
		printf ("Case #%d: ", j+1);
		for (int i = 0; i < n; i++) {
			if (s[i] >= 'a' && s[i] <='z') printf ("%c",res[s[i]-'a']); else printf (" ");
		}
		printf ("\n");
	}
	return 0;
}