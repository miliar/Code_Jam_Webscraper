#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

void Change(char x)
{
	if(x == ' ') { cout << " "; return; }
	if(x == 'q') { cout << "z"; return; }
	if(x == 'w') { cout << "f"; return; }
	if(x == 'e') { cout << "o"; return; }
	if(x == 'r') { cout << "t"; return; }
	if(x == 't') { cout << "w"; return; }
	if(x == 'y') { cout << "a"; return; }
	if(x == 'u') { cout << "j"; return; }
	if(x == 'i') { cout << "d"; return; }
	if(x == 'o') { cout << "k"; return; }
	if(x == 'p') { cout << "r"; return; }
	if(x == 'a') { cout << "y"; return; }
	if(x == 's') { cout << "n"; return; }
	if(x == 'd') { cout << "s"; return; }
	if(x == 'f') { cout << "c"; return; }
	if(x == 'g') { cout << "v"; return; }
	if(x == 'h') { cout << "x"; return; }
	if(x == 'j') { cout << "u"; return; }
	if(x == 'k') { cout << "i"; return; }
	if(x == 'l') { cout << "g"; return; }
	if(x == 'z') { cout << "q"; return; }
	if(x == 'x') { cout << "m"; return; }
	if(x == 'c') { cout << "e"; return; }
	if(x == 'v') { cout << "p"; return; }
	if(x == 'b') { cout << "h"; return; }
	if(x == 'n') { cout << "b"; return; }
	if(x == 'm') { cout << "l"; return; }
}

int main()
{
	int t;
	cin >> t;
	char a = getchar();

	for( int i = 1; i <= t; i++ )
	{
		string a;
		getline(cin, a);

		cout << "Case #" << i <<": ";

		for( int j = 0; j < a.size(); j++ ) Change(a[j]);

		cout << "\n";
	}

	return 0;
}
