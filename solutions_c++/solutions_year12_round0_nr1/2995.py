#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cctype>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>

using namespace std;

#define MAX_CHARS 200
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)

int main()
{
	char trans[26] = { 'y','h','e','s','o','c',
		'v','x','d','u','i','g','l','b','k',
		'r','z','t','n','w','j','p','f','m','a','q'};
	char s[MAX_CHARS];
	memset(s,'\0',MAX_CHARS);

	ifstream in("C:\\input.txt");
	ofstream out("C:\\output.txt");

	if (!in)  {
		cout << "C' file" << endl;
		return 0;
	}
	if (!out) {
		cout << "c' file" << endl;
		return 0;
	}

	int n = 0;
	in >> n;
	in.getline(s,sizeof(s));
	memset(s,'\0',MAX_CHARS);
	forn(i, n) {
		in.getline(s,sizeof(s));
		int j = 0;
		while(s[j] != '\0') {
			if (s[j] == ' ') {
				j++;
				continue;
			} else {
				s[j] = trans[s[j]-97];
				j++;
			}
		}
		out << "Case #" << i+1 << ": " << s << "\n";
		memset(s,'\0',MAX_CHARS);
	}
	in.close();
	out.close();

	return 0;
}