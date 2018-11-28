#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

#define	MAPITR(a,b)		map<a,b>::iterator
#define	LISTITR(a)		list<a>::iterator

#define ITER(itr,a)		for( itr = (a).begin(); itr != (a).end(); ++itr )
#define ITERNI(itr,a)	for( itr = (a).begin(); itr != (a).end(); )
#define FORI(i,a,b)		for( int i(a), _b(b); i < _b; ++i )
#define FORD(i,a,b) 	for( int i(a), _b(b); i > _b; --i )
#define FORLE(i,a,b)	for( int i(a), _b(b); i <= _b; ++i )
#define FORGE(i,a,b)	for( int i(a), _b(b); i >= _b; --i )

typedef list<int> li;
typedef list<double> ld;
typedef list<string> ls;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;

int main()
{
	int nCases, size;
	li vect1, vect2;
	cin >> nCases;

	FORLE( i, 1, nCases )
	{
        cin >> size;
        
        vect1.clear();
        vect2.clear();
        
        FORI(i, 0, size)
        {
            int n;
            cin >> n;
            vect1.push_back( n );
        }
        
        FORI( i, 0, size )
        {
              int n;
              cin >> n;
              vect2.push_back( n );
        }
        vect1.sort();
        vect2.sort();
        
        int sum = 0;
        LISTITR(int) v1itr;
        list<int>::reverse_iterator v2itr;
        v2itr = vect2.rbegin();
        ITER(v1itr, vect1)
        {
              sum += ((*v1itr)*(*v2itr));
              ++v2itr;
        }
		cout << "Case #" << i << ": " << sum;
		cout << endl;
	}

	return 0;
}

