#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

string a = "abcdefghijklmnopqrstuvwxyz ", b = "yhesocvxduiglbkrztnwjpfmaq ";
			
int n;

int main () {
	scanf ("%d\n", &n);
	for (int i = 0; i < n; i ++) {
		string str, str2 = "";
		getline (cin, str);
		int l = str.length ();
		for (int j = 0; j < l; j ++)
			str2 = str2 + b[a.find (str[j])];
		printf ("Case #%d: %s\n", i + 1, str2.c_str ());
	}
	
	return 0;
}
