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

int delta(int &a, int &b, int d)
{
	return (a < b)? -d : d;
}

int delta(int &a, int &b)
{
	return (a < b)? b - a : a - b;
}

int min (int &a, int &b)
{
	return (a < b)? a : b ;
}

int main()
{
	int N;
	int k;
	string s;
	vector <int> b[2];
	int t, p[2];
	vector <int> push; 
	b[0].reserve(110);
	b[1].reserve(110);
	push.reserve(110);
	int nb;

	cin >> N;
	FOR(c,1,N+1)
	{
		cin >> nb;
		
		b[0].clear(); b[0].resize(nb+1,0);
		b[1].clear(); b[1].resize(nb+1,0);
		push.clear(); push.resize(nb+1,0);

		FOR(i,1,nb+1)
		{
			cin >> s >> k;
			push[i] = (s[0] == 'B');
			b[push[i]][i] = k;
		}
		FORd(i,nb,0)
		{
			if(b[0][i] == 0) b[0][i] = b[0][i+1];
			if(b[1][i] == 0) b[1][i] = b[1][i+1];
		}
		t=0;
		p[0]=p[1]=1;

//		cerr << " ps "; FOR(z,1,nb+1) cerr << push[z] << " "; cerr << endl;
//		cerr << " b0 "; FOR(z,1,nb+1) cerr << b[0][z] << " "; cerr << endl;
//		cerr << " b1 "; FOR(z,1,nb+1) cerr << b[1][z] << " "; cerr << endl;
		int md;
		FOR(i,1,nb+1)
		{
			//both moving
			md = min( delta(b[0][i], p[0]), delta(b[1][i], p[1]) );
			p[0] += delta(b[0][i], p[0], md);
			p[1] += delta(b[1][i], p[1], md);
			t+=md;
//			cerr << i << " " << t << " both " << p[0]  << " " << p[1] << endl;

			if(b[push[i]][i] != p[push[i]])
			{
				md = delta(b[push[i]][i], p[push[i]]);
				p[push[i]] += delta(b[push[i]][i], p[push[i]], md);
				t+=md;
//				cerr << i << " " << t << " one  " << p[0]  << " " << p[1] << endl;
			}
			//one push, other move
			md = !push[i];
			if(delta(b[md][i], p[md]))
				p[md] += delta(b[md][i], p[md], 1);
			t++;
//			cerr << i << " " << t << " push " << p[0]  << " " << p[1] << endl;

		}


		cout << "Case #" << c << ": ";
		cout << t; 
		cout << endl;
	}
	return 0;
}
