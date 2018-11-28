
#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

#define MAX_DIGIT 128

class long_integer
{
  public:
	int _digit[MAX_DIGIT];
  public:
	long_integer ()
		{ clear(); }
	void clear ()
	{
		for ( int i = 0; i < MAX_DIGIT; i++ )
		_digit[i] = 0;
	}
	bool is_zero ()
	{
		for ( int i = 0; i < MAX_DIGIT; i++ )
			if ( _digit[i] != 0 )
				return false;
		return true;
	}
	int& operator [] ( int pos )
		{ return _digit[pos]; }
	int digits ()
	{
		int d=MAX_DIGIT;
		for ( int i = 0; i < MAX_DIGIT; i++ )
		{
			if ( _digit[i] != 0 )
				return d;
			d--;
		}
	}
	int first_digit_index ()
	{
		for ( int i = 0; i < MAX_DIGIT; i++ )
			if ( _digit[i] != 0 )
				return i;
		return MAX_DIGIT-1;
	}
	int mul10 ()
	{
		for ( int i = 1; i < MAX_DIGIT; i++ )
			_digit[i-1] = _digit[i];
		_digit[MAX_DIGIT-1] = 0;
	}
	long_integer cut( int start, int end )
	{
		long_integer res;
		res.clear();
		for ( int i = 0; i < end - start + 1; i++ )
			res[MAX_DIGIT-1-i] = _digit[end-i];
		return res;
	}
	void self_adjust ()
	{
		for ( int i = MAX_DIGIT - 1; i >= 0; i-- )
		{
			while ( _digit[i] < 0 )
			{
				_digit[i-1]--;
				_digit[i] += 10;
			}
			while ( _digit[i] >= 10 )
			{
				_digit[i-1]++;
				_digit[i] -= 10;
			}
		}
	}
};

ostream& operator << ( ostream& os, long_integer v )
{
	bool b = false;
	for ( int i = 0; i < MAX_DIGIT; i++ )
	{
		if ( b == false && v[i] == 0 )
			continue;
		b = true;
		cout << v[i];
	}
	if ( b == false )
		cout << 0;
	return os;
}

bool operator < ( long_integer x, long_integer y )
{
	int i;
	for ( i = 0; i < MAX_DIGIT; i++ )
	{
		if ( x[i] < y[i] )
			return true;
		if ( x[i] > y[i] )
			return false;
	}
	return false;
}

bool operator == ( long_integer x, long_integer y )
{
	int i;
	for ( i = 0; i < MAX_DIGIT; i++ )
		if ( x[i] != y[i] )
			return false;
	return true;
}

long_integer operator + ( long_integer x, long_integer y )
{
	int i;
	long_integer res;

	res.clear();
	for ( i = MAX_DIGIT-1; i >= 0; i -- )
		res[i] = res[i] + x[i] + y[i];

	res.self_adjust();
	return res;
}

long_integer operator - ( long_integer x, long_integer y )
{
	int i, j;
	long_integer res;

	res = x;

	for ( i = 0; i < MAX_DIGIT; i++ )
		res[i] = res[i] - y[i];

	res.self_adjust();
	return res;
}

long_integer operator * ( long_integer x, long_integer y )
{
	int i, j;
	long_integer res;

	if ( x < y )
		return ( y * x );

	res.clear();
	for ( i = 0; i < y.digits(); i++ )
	{
		for ( j = 0; j < x.digits(); j++ )
		{
			res[MAX_DIGIT-1-i-j] += ( x[MAX_DIGIT-1-j] * y[MAX_DIGIT-1-i] );
		}
	}
	res.self_adjust();

	return res;
}

long_integer operator / ( long_integer x, long_integer y )
{
	long_integer res, div, sub;

	res.clear();
	div = x;

	while ( !( div < y ) )
	{
		sub = y;
		while ( sub.digits() < div.digits()-1 )
			sub.mul10();
		div = div - sub;
		res[ MAX_DIGIT-1-(sub.digits()-y.digits()) ]++;
	}
	res.self_adjust();
	return res;
}

long_integer operator % ( long_integer x, long_integer y )
{
	long_integer div = x / y;

	return ( x - y * div );
}

int test_round( ifstream& ifs, int round );
long_integer find_apocalypse ( vector<long_integer>& events );

int main ( int argc, char * argv[] )
{
	int round_num;
	int i;

	if ( argc != 2 )
	{
		cout << "Usage: gtest <filename>" << endl;
		return -1;
	}

	ifstream ifs( argv[1] );
	if (!ifs )
	{
		cout << "File does not exist" << endl;
		return( -1 );
	}

	ifs >> round_num;

	for ( i = 0; i < round_num; i++ )
	{
		if ( test_round( ifs, i ) != 0 )
			return -1;
	}

	return( 0 );
}

int test_round( ifstream& ifs, int round )
{
	int event_num;
	string buf;
	vector<long_integer> events;
	int i, j;
	long_integer li;

	ifs >> event_num;
	for ( i = 0; i < event_num; i++ )
	{
		ifs >> buf;
		li.clear();
		for ( j = 0; j < buf.size(); j++ )
			li[ MAX_DIGIT-1-j] = buf[buf.size()-1-j] - '0';
		events.push_back( li );
	}

	li = find_apocalypse ( events );

	cout << "Case #" << round+1 << ": " << li << endl;

	return 0;
}

long_integer find_gcd( long_integer x, long_integer y )
{
	long_integer small, large;

	if ( x < y )
	{
		small = x;
		large = y;
	}
	else
	{
		small = y;
		large = x;
	}
	if ( small.is_zero() )
		return large;

	return find_gcd( small, large - small * ( large / small ) );
}

long_integer find_apocalypse ( vector<long_integer>& events )
{
	long_integer min_gcd, gcd, min, sub;
	int i, j;
	vector<long_integer> diff;

	min_gcd.clear();

	if ( events.size() == 1 )
		return min_gcd;

	min = events[0];
	for ( i = 1; i < events.size(); i++ )
	{
		if ( events[i] < events[i-1] )
			sub = events[i-1] - events[i];
		else
			sub = events[i] - events[i-1];
		if ( !sub.is_zero() )
			diff.push_back( sub );
		if ( events[i] < min )
			min = events[i];
	}

	min_gcd = diff[0];
	if ( diff.size() > 1 )
	{
		for ( i = 0; i < diff.size() - 1; i++ )
		{
			for ( j = i+1; j < diff.size(); j++ )
			{
				if ( diff[i].is_zero() && diff[j].is_zero() )
					continue;
				gcd = find_gcd( diff[i], diff[j] );
				if ( gcd < min_gcd )
					min_gcd = gcd;
			}
		}
	}
	
	min = min % min_gcd;

	if ( min.is_zero() )
		return min;

	return (min_gcd - min);
}
