#include <boost/foreach.hpp>
#include <boost/lexical_cast.hpp>
#include <cstdlib>
#include <exception>
#include <iomanip>
#include <iostream>
#include <list>
#include <new>
#include <set>
#include <string>
#include <vector>

using namespace std;
using namespace boost;

#define FOR BOOST_FOREACH

string read_line()
{
    string Line;
    getline(cin, Line);
    return Line;
}

int main()
{
    try
    {
	int N = lexical_cast< int >(read_line());
#ifndef NDEBUG
	    cerr << string(80, '-') << endl;
#endif
	for(int n = 0; n < N; ++n)
	{
	    int S = lexical_cast< int >(read_line());
	    set< string > SearchEngines;
	    for(int s = 0; s < S; ++s)
		SearchEngines.insert(read_line());
	    int Q = lexical_cast< int >(read_line());
	    vector< string > Queries;
	    for(int q = 0; q < Q; ++q)
		Queries.push_back(read_line());
	    set< string > Pool = SearchEngines;
	    string Choice;
	    list< string > Choices;
	    while(!Queries.empty())
	    {
		if(Pool.size() == 1)
		    Choice = *Pool.begin();
		Pool.erase(Queries.back());
		if(Pool.empty())
		{
		    Choices.push_front(Choice);
		    Pool = SearchEngines;
		    Pool.erase(Choice);
		}
		Queries.pop_back();
	    }
#ifndef NDEBUG
	    cerr << "Initial choice(s):" << endl;
	    FOR(string Choice, Pool)
		cerr << Choice << endl;
	    cerr << endl;
	    cerr << "Subsequent choice(s):" << endl;
	    FOR(string Choice, Choices)
		cerr << Choice << endl;
	    cerr << endl;
#endif
	    cout << "Case #" << (n + 1) << ": " << Choices.size() << endl;
#ifndef NDEBUG
	    cerr << string(80, '-') << endl;
#endif
	}
	return EXIT_SUCCESS;
    }
    catch(const exception& Exception)
    {
	cerr << "STL exception: " << Exception.what() << endl;
	return EXIT_FAILURE;
    }
}
