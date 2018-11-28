#include <stdio.h>
#include <iostream>
#include <map>
using namespace std;

map<char, char> change;
string A1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
string B1 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string C1 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
string A2 = "our language is impossible to understand";
string B2 = "there are twenty six factorial possibilities";
string C2 = "so it is okay if you want to just give up";

int main(int argc, char *argv[])
{
	for (int i = 0; i < A1.length(); i++)
		change[A1[i]] = A2[i];
	for (int i = 0; i < B1.length(); i++)
		change[B1[i]] = B2[i];
	for (int i = 0; i < C1.length(); i++)
		change[C1[i]] = C2[i];
	change['q'] = 'z';
	change['z'] = 'q';
	freopen("input.txt", "r", stdin);
	int n;
	cin >> n;
	int tot = 0;
	string s;
	getline(cin, s);
	while (n) {
		string st;
		tot++;
		cout << "Case #" << tot << ": ";
		getline(cin, st);
		for (int i = 0; i < st.length(); i++)
			cout << change[st[i]];
		cout << endl;
		n--;
	}
	fclose(stdin);
	
	return 0;
}
