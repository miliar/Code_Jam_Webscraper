/****** String Library */
#include <string>
#include <sstream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

/****** Containers */
#include <bitset>
#include <deque>
#include <stack>
//#include <queue> //queue - priority_queue
#include <vector>
#include <list>
#include <set> //set - multiset
#include <map> //map - multimap
//#include <iterator> //iterators for !need

/****** Algorithms finds... sorts... merges... */
#include <algorithm>

/****** Functions' Adaptors and Objects */
#include <functional>

/****** Mth and Numeric Ops */
#include <math.h>
#include <complex>
#include <numeric>
#include <limits>

/****** Memory Utils */
#include <memory> 

/****** var */
#include <utility> 
#include <iomanip> 
#include <time.h> 

using namespace std;

#define FOR(i, m, n) for (int i=m, i_end=n; i<i_end; ++i)
#define FORd(i, m, n) for (int i=m-1, i_end=n; i>=i_end; --i)
#define FORit(type,it,cntnr) for (type::iterator it=cntnr.begin(); it!=cntnr.end(); ++it)
#define FORdit(type,it,cntnr) for (type::reverse_iterator it=cntnr.rbegin(); it!=cntnr.rend(); ++it)
#define FORit_(type,it,cntnr) for (type::iterator it=cntnr.begin()+1, _it=cntnr.end()-1;it != _it; ++it)
#define FORdit_(type,it,cntnr) for (type::reverse_iterator it=cntnr.rbegin()+1, _it=cntnr.rend()-1; it!=_it; ++it)

int main()
{
	int N;
	int ns;
	string s;
	string t;

	short int combs[128][128];
	short int opsts[128];
	int co[128];


	cin >> N;
	FOR(c,1,N+1)
	{
		FOR(i,'A','Z'+1)FOR(j,'A','Z'+1) combs[i][j]=0;
		cin >> ns;
		FOR(i,0,ns)
		{
			cin >> s;
			combs[s[0]][s[1]] = s[2];
			combs[s[1]][s[0]] = s[2];
		}
		cin >> ns;
		FOR(i,'A','Z'+1)
		{
		   opsts[i]=co[i]=0;
		}
		FOR(i,0,ns)
		{
			cin >> s;
			opsts[s[0]] = s[1];
			opsts[s[1]] = s[0];
		}

		cin >> ns;
		cin >> s;
		t.clear();
		t.push_back(s[0]);
		FOR(i,1,ns)
		{
//			cerr << s[i] << (*t.rbegin()) << combs[(*t.rbegin())][s[i]] << endl;
			if(combs[(*t.rbegin())][s[i]])
			{
				(*t.rbegin()) = combs[(*t.rbegin())][s[i]];
			}
			else if(t.find(opsts[s[i]])!=string::npos)
			{
				t.clear();
			}
			else
			{
				t.push_back(s[i]);
			}
		}

		cout << "Case #" << c << ": [";

		if (t.size()) cout << t[0];
		FOR(i,1,t.size())
			cout << ", " << t[i];
		cout << "]";
		cout << endl;
	}
	return 0;
}
