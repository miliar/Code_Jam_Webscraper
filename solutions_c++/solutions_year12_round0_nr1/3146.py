#include <cstdlib>
#include <iostream>
#include <sstream>
#include <stdio.h>
using namespace std;

char trans(char c){
	if(c == ' ') return ' ';
	char from[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
	char to[] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q'};
	for(int i = 0; i < 26; i++)
	{
		if(c == to[i]) return from[i];
		if(c == to[25-i]) return from[25-i];
	}
}

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	int T; char s[200]; stringstream ss;
	
	cin.getline(s, 100);
	ss << s;
	ss >> T;
	
	for(int i = 0; i < T; i++)
	{
		cin.getline(s, 256);
		int n = sizeof(s) / sizeof(char);
		cout << "Case #" << i+1 << ": ";
		for(int j = 0; j < n; j++)
			if(!(s[j] >= 'a' && s[j] <= 'z' || s[j] == ' ')) break;
			else cout << trans(s[j]);
		cout << endl;
	}

    return 0;
}
