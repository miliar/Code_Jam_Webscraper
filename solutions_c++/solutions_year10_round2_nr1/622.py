//============================================================================
// Name        : A.cpp
// Author      : Artem A. Khizha
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <set>
#include <utility>
using namespace std;

typedef unsigned int uint;

set<string> dir;

int main() {
    int tnum;
	cin >> tnum;
	for (int ti = 1; ti <= tnum; ti++) {
	    dir.clear();
	    long cnt = 0,  n, m;
	    cin >> n >> m;
	    string s, c;
	    for (int i = 0; i < n; i++)    {
            cin >> s;
            c.clear();
            for (uint k = 0; k < s.size(); k++) {
                c.push_back(s[k]);
                if (k == s.size()-1)    {
                    c.push_back('/');
                    dir.insert(c);
                }
                if (s[k] == '/' )   {
                    dir.insert(c);
                }
            }
	    }
        for (int i = 0; i < m; i++)    {
            cin >> s;
            c.clear();
            for (uint k = 0; k < s.size(); k++) {
                c.push_back(s[k]);
                if (k == s.size()-1)
                    c.push_back('/');
                if ((k && s[k] == '/') || k == s.size()-1)   {
                    if (dir.find(c) == dir.end())   {
                        dir.insert(c);
                        cnt++;
                    }
                }
            }
        }
	    cout << "Case #" << ti << ": " << cnt << endl;
	}
	return 0;
}
