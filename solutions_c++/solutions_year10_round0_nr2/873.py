#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <complex>
#include <stdlib.h>

//#define DEBUG

using namespace std;

unsigned long long gcd(unsigned long long a, unsigned long long b)
{
	if(b == 0)
	{
		return a;
	}
	else
	{
		return gcd(b, a % b);
	}
}

typedef unsigned long long U64;

U64 StringToU64(const char * sz)
{
	U64 u64Result = 0;
	while (*sz != '\0')
	{
		u64Result *= 10 ;
		u64Result += *sz
			- '0';
		sz ++ ;
	}
	return u64Result;
}

template <class charT, class T>
bool FromString(const std::basic_string<charT>& InputString, T& Value)
{
	std::basic_istringstream<charT> in(InputString);
	return (in >> Value && in.eof());
}

int main(int argc, char** argv)
{
	//freopen("test.in", "r", stdin );
	//freopen("test.out", "w", stdout );
	freopen("B-small-attempt2.in", "r", stdin );
	freopen("B-small-attempt2.out", "w", stdout );
	//freopen("A-large.in", "r", stdin );
	//freopen("A-large.out", "w", stdout );

	int T;
	string line;

	cin >> T;
	getline(cin, line, '\n');
	for( int iT=0; iT < T; iT++){
		int N;
		vector<unsigned long long> v;
		vector<unsigned long long> d;

#ifdef DEBUG
		printf( "iT: %d\n", iT);
#endif //DEBUG

		cin >> N;
		for( int iN = 0; iN < N; iN++){
			unsigned long long t;
			//string t;
			
			//cin >> t;
			//cout << t << endl;

			fscanf( stdin, "%llu", &t);
			//printf("%llu\n", t );
			v.push_back( t );

			//printf("%llu\n", t );
			//printf("%s\n", t);
	

			//v = atoll( t.c_str() );

			//v = StringToU64(t.c_str() );
			//printf("%llu\n", v );

		}

		sort( v.begin(), v.end() );


#ifdef DEBUG
		for( unsigned int i = 0; i < v.size(); i++){
			printf("%llu ", v[i] );	
		}
		printf("\n");
#endif //DEBUG

		//// Get diff values
		unsigned long long lastValue = v[0];
		for( unsigned int i = 1; i < v.size(); i++){
			unsigned long long value = v[i];
			d.push_back( value - lastValue );
#ifdef DEBUG
			printf("%llu\n", value - lastValue );	
#endif//DEBUG
			lastValue = value;
		}

		unsigned long long lastGCD = d[0];
		for( unsigned int i = 1; i < d.size(); i++){
			unsigned long long value = d[i];
			lastGCD = gcd( lastGCD, value );
		}
#ifdef DEBUG
		printf("GCD: %llu\n", lastGCD );
#endif//DEBUG

		unsigned long long y = 0;
		if( lastGCD == 1 ){
			y = 0;
		}else{

			//unsigned long long lastY = 0;
			for( unsigned int i = 0; i < v.size(); i++){
				unsigned long long r = v[0] % lastGCD;

				if( r != 0 ){
					y = lastGCD - r;
				}else{
					y = 0;
				}

				//if( i > 0 && lastY != y ){
				//	printf("Miss\n");
				//}
				//lastY = y;
			}


		}

		printf("Case #%d: %llu\n", iT + 1, y);

		//for( unsigned int i = 0; i < v.size(); i++){
		//	unsigned long long value = v[i];
		//	printf("%llu\n", value );			
		//}




	}

	//long double v = pow((long double)10,(int)50);
	//printf( "%llu\n", v );
	//printf( "%d\n", sizeof(long double) );

	//unsigned long long v2 = (unsigned long long)1 << (unsigned long long)63;
	//printf( "%llu\n", v2 );
	//printf( "%d\n", sizeof(unsigned long long) );

	//printf( "%u\n", 2 );

	
	//printf( "%d\n", sizeof(unsigned long int) );

}