#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <list>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define GETS(s) getline(cin, s);
#define GETI(i) { string _s; getline(cin, _s); i = atoi(_s.c_str()); }

//----------------------------------------------------------------------------
string sample_from("y qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv z");
string sample_to  ("a zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up q");

map<char,char> trans_map;
map<char,char> check_map;

//----------------------------------------------------------------------------
void learn()
{
	FOR(i,'a','z')
      check_map[i]='?';

	int l(sample_from.length());
	FOR(i,0,l-1)
	{
    char c(sample_from[i]);
	  if (c == ' ')
	    continue;

    if (check_map[c] == '?')
	  {
		  check_map[c] = ' ';
	  }
	  else if (check_map[c] == ' ')
	  {
		  if (trans_map[c] != sample_to[i])
        check_map[c] = '!';
	  }
	  trans_map[c]=sample_to[i];
	}

	// display checkmap
	//map<char, char>::iterator i;
	//string from, to;
	//for (i = check_map.begin(); i != check_map.end(); ++i) {
  //  from += i->first;
	//  if (i->second == ' ')
  // 	  to += trans_map[i->first];
	//  else 
	//    to += i->second;
	//};
	//cout << from << endl;
	//cout << to << endl;
}

//----------------------------------------------------------------------------
void translate(string &s)
{
  int l(s.length());
  FOR(i,0,l-1)
  {
    if (s[i] != ' ')
	    s[i] = trans_map[s[i]];
  }
}

//----------------------------------------------------------------------------
int main() {
	freopen("A-small-1.in", "rt", stdin);
	freopen("A-small-1.out", "wt", stdout);

	string result;

	learn();

	int T;
	GETI(T);
	FOR(TestCase, 1, T) {
		result.clear();

		// load data
		GETS(result);

		// algorithm
		translate(result);

		cout << "Case #" << TestCase << ": " << result << endl;
	}

	return EXIT_SUCCESS;
}

