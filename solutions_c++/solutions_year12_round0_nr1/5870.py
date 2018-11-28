#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int d, l;
char alf[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
string s;
int main(){
	scanf ("%d\n", &d); l = 1;
	while (d--){
		getline (cin, s);
		printf ("Case #%d: ", l);
		for (int i = 0; i < s.size(); i++)
			if (s[i] == ' ')
				cout << " ";
			else
				cout << alf[s[i]-'a'];
		cout << "\n";
		l++;
	}
}
