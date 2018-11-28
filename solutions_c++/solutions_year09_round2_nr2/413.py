#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	freopen("02l.in", "r", stdin);
	freopen("02l.out", "w", stdout);

	char buf[50];
	int i, j, cas, now;
	char t;
	string str;
	string::iterator si;
	scanf("%d\n",&cas);
	
	for(now = 1; now <= cas; now++) {
		cin.getline(buf,50);
		str = buf;
		if(!next_permutation(str.begin(), str.end())) {
			for(si = str.begin();si<str.end();si++) {
				if(*si != '0') break;
			}
			t = *si;
			str.erase(si);
			str.insert(str.begin(), 1, t);
			str.insert(str.begin()+1, 1, '0');
		}
		cout << "Case #" << now << ": " << str << endl;
	}

	return 0;
}