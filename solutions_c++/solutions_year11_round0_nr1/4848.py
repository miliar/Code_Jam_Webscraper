#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

#define MAPITR(a,b)	map<a,b>::iterator
#define LISTITR(a)	list<a>::iterator

#define ITER(itr,a)	for( itr = (a).begin(); itr != (a).end(); ++itr )
#define ITERNI(itr,a)	for( itr = (a).begin(); itr != (a).end();  )
#define FORI(i,a,b)	for( int i(a), _b(b); i < _b; ++i )
#define FORD(i,a,b)	for( int i(a), _b(b); i > _b; --i )
#define FORLE(i,a,b)	for( int i(a), _b(b); i <= _b; ++i )
#define FORGE(i,a,b)	for( int i(a), _b(b); i >= _b; --i )

typedef list<bool> lb;
typedef list<char> lc;
typedef list<int> li;
typedef list<double> ld;
typedef list<string> ls;

typedef vector<bool> vb;
typedef vector<char> vc;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;


bool move_robot( int &pos, int dst )
{
	if (pos == dst)
		return false;

	if (pos < dst)
		++pos;
	else
		--pos;

	return true;
}

int main()
{
	bool val;
	char c;
   int nCases, cnt, N, bNum, oPos, bPos;
   lb combo;
   li oList, bList;

   cin >> nCases;

   FORLE( i, 1, nCases )
   {
	   combo.clear();
	   oList.clear();
	   bList.clear();
	   
	   cnt = 0;
	   oPos = bPos = 1;

	   cin >> N;
	   
	   FORI (j, 0, N)
	   {
		   cin >> c;
		   cin >> bNum;

		   combo.push_back(c == 'O');
		   
		   if (c == 'O')
			   oList.push_back( bNum );
		   else
			   bList.push_back( bNum );
	   }

	   while (!combo.empty())
	   {
		   ++cnt;
		   val = false;

		   if (!oList.empty() && !move_robot( oPos, oList.front() ) && combo.front())
		   {
			   val = true;
			   oList.pop_front();
		   }
		   
		   if (!bList.empty() && !move_robot( bPos, bList.front() ) && !combo.front())
		   {
			   val = true;
			   bList.pop_front();
		   }

		   if (val)
			   combo.pop_front();
	   }

      cout << "Case #" << i << ": " << cnt;
      cout << endl;
   }

   return 0;
}  
