#include <string>
#include <vector>
#include <stdint.h>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <cassert>
#include <cstdio>
#include <list>
#include <cmath>
#include <climits>
#include <stack>

#define ASSERT(statement, obj) { typeof(obj) x=(statement); if(x!=(obj)){std::cout<<x<<std::endl;assert(false);}}
#define FOR(index, from, to) for (typeof(to) index=from; index<(to); ++index)
#define VFOR(index, v) for (typeof(v.size()) index=0; index<(v.size()); ++index)
#define ITER(it, list) for(typeof(list.begin()) it=list.begin(); it!=list.end();++it)
#define PRINT_VECTOR_INT(v) FOR(i, 0, v.size())cout<<v[i]<<" "
using namespace std; 

char G[200];

int main()
{
	map<char,char> m;
	m['y'] = 'a';
	m['n'] = 'b';
	m['f'] = 'c';
	m['i'] = 'd';
	m['c'] = 'e';
	m['w'] = 'f';
	m['l'] = 'g';
	m['b'] = 'h';
	m['k'] = 'i';
	m['u'] = 'j';
	m['o'] = 'k';
	m['m'] = 'l';
	m['x'] = 'm';
	m['s'] = 'n';
	m['e'] = 'o';
	m['v'] = 'p';
	m['z'] = 'q';
	m['p'] = 'r';
	m['d'] = 's';
	m['r'] = 't';
	m['j'] = 'u';
	m['g'] = 'v';
	m['t'] = 'w';
	m['h'] = 'x';
	m['a'] = 'y';
	m['q'] = 'z';
	m[' '] = ' ';

	string line;
	int T=0;
	getline(cin, line);
	stringstream ss(line);
	ss >> T;
	FOR(i, 0, T)
	{
		//scanf("%[a-z ]", G);
		//cout<<G<<endl;
		//string line(G);
		getline(cin, line);
		string out = "";
		FOR(j, 0, line.length())
			out += m[line[j]];
		printf("Case #%d: %s\n", i+1, out.c_str());
	}
}
