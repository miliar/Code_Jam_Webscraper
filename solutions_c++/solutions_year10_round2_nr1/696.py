#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;
vector<string> parse( string a)
{
	vector<string> res;
	int cur = 1;
	while(1)
	{
		cur = a.find('/',cur+1);
		if(cur == - 1)
		{
			res.push_back(a);
			return res;
		}
		string t = a.substr(0,cur);
		res.push_back(t);

	}
	return res;
}

#define outputfile cout
int main()
{
	ifstream input("A-large.in");
	ofstream outputfile("output.txt");
	int sz ;
	
	input >> sz ;

	for( int casen = 1 ; casen <= sz;  ++casen)
	{
		int n , m;
		input >> n >> m;
		int res = 0;
		set<string> q;
		string t;
		for( int i = 0 ; i < n ; ++i)
		{
			input >> t ;
			vector<string> a = parse(t);
			for( int j = 0 ; j < a.size();++j) q.insert(a[j]);
		}
		for( int i = 0 ; i < m ; ++i)
		{
			input >> t ;
			vector<string> a = parse(t);
			for( int j = 0 ; j < a.size();++j) 
			{
				if( q.count(a[j])) continue;
				++res;
				q.insert(a[j]);

			}
		}
		outputfile << "Case #" << casen << ": " << res << endl;
	}
	getchar();
	return 0;
}
