/*
 * Google Code Jam 2010. Round 1 - sub-round A
 * (C)Copyright jclin (j i a n c h e n g [at] g_m_a_i_l [dot] c_o_m)
 */
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <ext/hash_map>

using namespace std;
using namespace __gnu_cxx;

#define FOR(i,N)	for(int i=0;i<N;++i)

hash_map<char, char> table;

	static const char * a[] = {
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv"
	};
	static const char * b[] = {
		"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give up"
	};

int main(int ac, char**av)
{
	int T;
	char tbl1[30], tbl2[30];

	for (unsigned int i = 0; i < sizeof(a)/sizeof(char*); ++i) {
		const char * from = a[i];
		const char * to = b[i];
		while (*from) {
			table[*from] = *to;
			from++;
			to++;
		}
	}
	table['z'] = 'q';
	table['q'] = 'z';

	cin >> T;
	static char buf[2000];
	gets(buf);
	FOR(i,T) {
		gets(buf);
		char * ptr = buf;
		while (*ptr) {
			*ptr = table[*ptr];
			ptr++;
		}
		cout << "Case #" << (i+1) << ": " << buf << endl;
	}
	return 0;
}

