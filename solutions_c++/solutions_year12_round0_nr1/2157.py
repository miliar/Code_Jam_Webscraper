#include <iostream>
#include <cstdio>

using namespace std;

int hash[] = {24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};

int main()
{
	int n, a, b;
	string s;
	char ch;
	
	scanf("%d",&n);
	scanf("%c",&ch);

	for( a = 1; a <= n; a ++ ) {
		getline(cin,s);
		for( b = 0; b < s.size(); b ++ ) {
			if( s[b] == ' ' ) {
				continue;
			}
			s[b] = hash[ s[b]-'a' ] + 'a';
		}
		cout << "Case #" << a << ": " << s << endl;
	}

	return 0;
}
