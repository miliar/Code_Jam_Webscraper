// Includes {{{
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <stdio.h>
using namespace std;
// }}}

// Defines úteis {{{
#ifdef DEBUG
#define TRACE(x...) x
#else
#define TRACE(x...) 
#endif
#define PRINT(x...) TRACE(printf (x))
#define WATCH(x) TRACE(cout << #x << ": " << x << endl)
#define SZ(x) ((int) (x).size ())
#define FOREACH(it,c) for (typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it) 
// }}}

const int MAX = 10000;

int s, q, caso, seq[MAX];

map <int, list <int> > engine;
map <string, int> dic;

int toInt (string str) {
	if (dic.find (str) != dic.end ())
		return dic[str];
	return dic[str] = dic.size ();
}

void processa () {
	int i, j, m, cnt, last, current;
	map <int, list <int> > :: iterator it;

	last = -1;
	cnt  = -1;
	for (i = 0; i < q; i++) {
		current = -1;
		m       = i;
		for (it = engine.begin (); it != engine.end (); it++) {
			while (!it->second.empty () && it->second.front () < i)
				it->second.pop_front ();

			if (!it->second.empty () && it->first != last)
				if (m < it->second.front ()) {
					m = it->second.front ();
					current = it->first;
				}
		}
		i    = m - 1;
		last = current;

#ifdef DEBUG
		printf (" processa: m=%d current: %d\n", m, current);
#endif

		cnt++;
	}

	printf ("Case #%d: %d\n", caso, max (cnt, 0));
}

void le () {
	int  i;
	char buff[MAX];

	engine.clear ();
	dic.clear ();

	scanf ("%d\n", &s);
	for (i = 0; i < s; i++) {
		scanf ("%[^\n]\n", &buff);
		engine.insert (make_pair (toInt (buff), list <int> ()));

#ifdef DEBUG
		printf ("engine: %d - %s\n", toInt (buff), buff);
#endif
	}	

	scanf ("%d\n", &q);
	for (i = 0; i < q; i++) {
		scanf ("%[^\n]\n", &buff);

		int query = toInt (buff);
		seq[i] = query;

#ifdef DEBUG
		printf ("query: %d - %s\n", toInt (buff), buff);
#endif

		if (engine.count (query)) {
			engine[query].push_back (i);
		}
	}

	for (i = 0; i < s; i++)
		engine[i].push_back (q);

#ifdef DEBUG
	map <int, list <int> > :: iterator it;
	list <int> :: iterator jt;

	for (it = engine.begin (); it != engine.end (); it++) {
		printf ("%d -> ", it->first);
		for (jt = it->second.begin (); jt != it->second.end (); jt++) {
			printf ("%d ", *jt);
		}
		printf ("\n");
	}
#endif
}

// Função main {{{
int main()
{
	int casos;
	scanf ("%d", &casos);

	for (caso = 1; caso <= casos; caso++) {
		le ();
		processa ();
	}

	return 0;
} 
// }}}
