#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

long long int f1( long long int t, long long int s, long long int p, vector<long long int> v )
{
	long long int k = 0, m = 0, n;
	for( long long int i = 0; i < t; i++ ) {
		if( v[i] / 3 >= p ) {
			k++;
		} else {
			n = v[i] % 3;
			if( n == 0 ) {
				if( v[i] / 3 + 1 >= p && v[i] / 3 - 1 >= 0 ) {
					m++;
				}
			} else if( n == 1 ) {
				if( v[i] / 3 + 1 >= p ) {
					k++;
				}
			} else if( n == 2 ) {
				if( v[i] / 3 + 1 >= p ) {
					k++;
				} else if( v[i] / 3 + 2 >= p && v[i] / 3 >= 0 ) {
					m++;
				}
			}
		}
	}
	if( m > s )
		return s + k;
	return m + k;
}

int main( int argc, char **argv )
{
	string str;
	stringstream ss;
	long long int t, n, s, p, temp;
	vector <long long int> v;
	ifstream fin(argv[1]);
	fin >> n;
	getline( fin, str );
	for( long long int k = 1; k <= n; k++ ) {
		getline( fin, str );
		ss << str;
		cout << "Case #" << k << ": ";
		ss >> t >> s >> p;
		for( long long int i = 0; i < t; i++ ) {
			ss >> temp;
			v.push_back( temp );
		}
		cout << f1( t, s, p, v);
		v.clear();
		ss.clear();
		cout << endl;
	}
	return 0;
}
