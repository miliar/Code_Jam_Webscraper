#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <conio.h>
#include <algorithm>
#include <queue>
#include <list>
#include <math.h>
#include <sstream>
using namespace std;
#define int64 long long
#define int32 int
#define d64 long double

int64 doit( int32 P, int32 K, int32 L, list<int64> freq )
{
	list<int64> placement;
	list<int64>::iterator it,it1;
	int64 cnt, res;
	bool done;

	cnt = 0;
	done = false;
	for( int64 i=0; i<L && !done; i++ )
	{
		if( P <= 0 ) break;
		for( int64 t=0; t<K && !done; t++ )
		{
			placement.push_back(i+1);
			cnt++;
			if( cnt >= L ) done = true;
		}
		P--;
	}

	if( freq.size() != placement.size() ) 
		return -1;

	freq.sort(greater<int>());
	
	it = freq.begin();
	it1 = placement.begin();
	res = 0;
	while( it != freq.end() )
	{
		res += (*it) * (*it1);
		it++;
		it1++;
	}

	return res;
}

int main()
{	
	int64 n, P, K, L, res;
	list<int64> freq;
	ifstream input;
	ofstream out;
	string line;

	input.open("A-large.in", ios::in);
	out.open("A-large.out", ios::out);

	//input.open("A-small-attempt0.in", ios::in);
	//out.open("A-small-attempt0.out", ios::out);

	input >> n;
	// test cases
	for( int64 i=0; i<n; i++ )
	{
		input >> P;
		input >> K;
		input >> L;

		for( int64 t=0; t<L; t++ )
		{
			int64 f;
			input >> f;
			freq.push_back( f );
		}

		res = doit( P, K, L, freq );
		cout << "Case #" << i+1 << ": " << res << endl;
		out << "Case #" << i+1 << ": " << res << endl;

		freq.clear();
	}

	input.close();
	out.close();
	getch();

	return 0;
 }