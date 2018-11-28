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
#include <list>

//#define DEBUG


using namespace std;

#define REP(i,a,b) for(i=a;i<b;i++)


int main(int argc, char** argv)
{
	//freopen("test.in", "r", stdin );
	//freopen("test.out", "w", stdout );
	//freopen("A-small-attempt3.in", "r", stdin );
	//freopen("A-small-attempt3.out", "w", stdout );
	freopen("A-large.in", "r", stdin );
	freopen("A-large.out", "w", stdout );

	int T;
	string line;

	cin >> T;
	getline(cin, line, '\n');
	for( int iT=0; iT < T; iT++){
		string enc;
		cin >> enc;

		//if( enc.size() == 1){
		//	printf( "Case #%d: %d\n", iT+1, 0);
		//	continue;
		//}

		set<char> dig( enc.begin(), enc.end() );
#ifdef DEBUG
		printf( "Line: %s\n", enc.c_str());
		for( set<char>::iterator it = dig.begin(); it != dig.end(); ++it){
			printf("%c\n", *it);
		}
#endif //DEBUG

		int base = dig.size();
		if( base == 1 ) base =2;
		
		int idx = 0;
		map<char,int> dm;
		dm.insert( pair<char,int>( enc.at(0), 1 ) );
		idx = 0;
		for( int i = 1; i < (int)enc.size(); i++){
			if( dm.find( enc.at(i) ) == dm.end() ){
				dm.insert( pair<char,int>( enc.at(i), idx ) );
				idx = ( idx == 0 ? 2: idx+1);
			}
		}


#ifdef DEBUG
		printf("=============\n");
		list<string> ssL;
		for(map<char,int>::iterator it = dm.begin(); it != dm.end();++it){
			char c = it->first;
			int v = it->second;

			char line[1024];
			sprintf( line, "%d %c", v, c);
			//printf("%s\n", line);
			//ssL.insert( line );
			ssL.push_back( line );
		}

		ssL.sort( );
		//sort( ssL.begin(), ssL.end(), less<string>() );

		for(list<string>::iterator it = ssL.begin(); it != ssL.end(); ++it)
		{
			printf("%s\n", (*it).c_str());
		}

		printf("=============\n");
#endif //DEBUG


		unsigned long long num10Base = 0;


		unsigned long long pivot = 1;
		for( int i = enc.size() - 1; i >= 0; i--){
			char c = enc.at(i);
			unsigned long long d = (unsigned long long)dm.find(c)->second;

			d = d * pivot;

			num10Base += d;

			pivot *= base;
		}



		printf( "Case #%d: %lld\n", iT+1, num10Base);

	}


}