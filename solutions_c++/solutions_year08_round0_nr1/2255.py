// codejam saveuniv.cpp
#include<iostream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cctype>
#include<climits>
#include<cfloat>

using namespace std;

int main()
{
    int n;
    cin >> n;
    for( int caseno = 0; caseno < n; caseno++ )
    {
	vector<string> se;
	se.clear();
	int sen;
	cin >> sen;
	sen++;
	while( sen-- )
	{
	    string engine;
	    getline( cin, engine );
	    se.push_back( engine );
	}
	se.erase( se.begin() );
	vector<string> qe;
	qe.clear();
	int qen;
	cin >> qen;
	qen++;
	while( qen-- )
	{
	    string query;
	    getline( cin, query );
	    qe.push_back( query );
	}
	qe.erase( qe.begin() );
	int watcher = 0;
	int switches = 0;
        while( watcher != INT_MAX )
	{
	    map<string, int> fo;
	    map<string, bool> fobool;
	    fo.clear();
	    fobool.clear();
	    for( int i = 0; i < se.size(); i++ )
	    {
		fo[se[i]] = INT_MAX;
		fobool[se[i]] = false;
	    }
	    for( int i = watcher; i < qe.size(); i++ )
	    {
		if( fobool[qe[i]] == false )
		{
		    fo[qe[i]] = i;
		    fobool[qe[i]] = true;
		}
	    }
	    int maxindex = 0;
	    for( map<string, int> :: iterator p = fo.begin(); p != fo.end(); p++ )
	    {
		if( ( p -> second ) > maxindex )
		{
		    maxindex = p -> second;
		}
	    }
	    watcher = maxindex;
	    switches++;
	}	    
	printf( "Case #%d: %d\n", caseno+1, switches-1 );
	
    }
  
    return 0;
}









