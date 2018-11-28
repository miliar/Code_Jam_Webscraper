#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <string.h>
#include <queue>
#include <utility>
#include <time.h>
#include <string.h>
using namespace std;


const char *s = "zqour language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
const char *g = "qzejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";

int m[256];

int main()
{
	memset( m, '?', sizeof(m) );
	for(const char *ss = s, *gg = g; *ss; gg ++, ss ++ )
		m[*gg] = *ss;
	int T;
	cin >> T;
	string str;
	getline(cin,str);
	for( int C = 1; C <= T; C ++ ){
		getline(cin,str);
		cout << "Case #" << C << ": ";
		for( int j = 0; j < str.size(); j ++ )
			cout << (char)m[str[j]];
		cout << endl;
	}
	return 0;
}
