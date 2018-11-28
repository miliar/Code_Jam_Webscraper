#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <numeric>

using namespace std;

template< typename type > type readOne()
{
    type res;
    char inp[5000];
    gets( inp );
    stringstream ss( inp );
    ss >> res;
    return res;
}

template< typename type > vector<type> readMulti()
{
    vector<type> res;
    char inp[5000];
    gets( inp );
    stringstream ss( inp );
    for ( type t; ss >> t; ) res.push_back( t );
    return res;
}

int doCase(){
    // vector<int> item  = readMulti<int>();
    vector<string> item2  = readMulti<string>();
    for(int i = 0; i < item2.size(); i++) 
        cout << item2[i];
    cout << endl;
    return 0;
}

int doit( int R, int K, int N, vector<int> g ){

    int ret = 0;
    int pos = 0;
    int size_g = g.size();

    while( R > 0 ){
	int people = 0;
	int num_g = 1;
	for( int i = 0; i < g.size(); i++ ){
	    if( pos >= N ) pos-=N; 
	    if( people + g[pos] > K ) break;
	    people += g[pos];
	    pos++;
	}
	ret += people;
	R--;
    }

    return ret;
}


int main()
{
    int cases = readOne<int>(); // cases
    for (int caseno = 1; caseno <= cases; caseno++){
	vector<int> num = readMulti<int>();
	vector<int> g   = readMulti<int>();
        cout << "Case #" << caseno << ": " << doit( num[0], num[1], num[2], g ) << endl; // call doCase()
    }
    return 0;
}
