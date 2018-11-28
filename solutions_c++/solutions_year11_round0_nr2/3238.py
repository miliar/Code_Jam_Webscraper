#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#include <utility>
#include <set>

#define REP(i, n) for( i = 0; i < n; i++ )

using namespace std;

typedef pair<char, char> elem_pair;
typedef map< elem_pair, char > combine_map;
typedef set< elem_pair > poof_set;

int main()
{
	freopen("b-small-attempt0.in", "r", stdin);
	//freopen("b-small.out", "w", stdout);
	freopen("b-large.out", "w", stdout);

	int T;	cin >> T;
	for( int cas = 1; cas <= T; cas++ )
	{
		//cout << "Case : " << cas << endl;
		int C;	cin >> C;
		int i;

		combine_map cm;
		poof_set ps;

		// create combine_map
		REP(i, C)
		{
			string str;	cin >> str;
			char a, b, c;
			a = str[0];	b = str[1];	c = str[2];
			cm.insert(combine_map::value_type(elem_pair(a,b),c));
			cm.insert(combine_map::value_type(elem_pair(b,a),c));
		}

		int D;	cin >> D;
		// create poof_set
		REP(i, D)
		{
			string str;	cin >> str;
			char a, b;
			a = str[0];	b = str[1];
			ps.insert(poof_set::value_type(elem_pair(a, b)));
			ps.insert(poof_set::value_type(elem_pair(b, a)));
		}

		int N;	cin >> N;
		string str; cin >> str;
		string curr_elems = "";
		REP( i, str.size() )
		{
			curr_elems = str[i] + curr_elems;
			bool first_time = true;
			while( curr_elems.size() >= 2 )
			{
				char a, b;
				a = curr_elems[0];
				b = curr_elems[1];
				if( cm.find(elem_pair(a, b)) != cm.end() )
				{
					first_time = false;
					curr_elems = curr_elems.substr(2);
					curr_elems = cm[elem_pair(a,b)] + curr_elems;
				}
				else if (first_time)
				{
					first_time = false;
					char x = curr_elems[0];
					for( int j = 1; j < curr_elems.size(); j++ )
					{
						char y = curr_elems[j];
						if( ps.find(elem_pair(x, y)) != ps.end() )
						{
							curr_elems = "";
							break;
						}
					}
				}
				else
					break;
			}
		}
		cout << "Case #" << cas << ": [";
		if( curr_elems.size() != 0 )
		{
			for( i = curr_elems.size()-1; i > 0; i-- )
				cout << curr_elems[i] << ", ";
			cout << curr_elems[i];
		}
		cout << "]" << endl;
	}
}

//The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of a single line,
//containing the following space-separated elements in order:
//
//First an integer C, followed by C strings, each containing three characters: two base elements followed by a non-base element.
//This indicates that the two base elements combine to form the non-base element. Next will come an integer D, followed by D strings,
//each containing two characters: two base elements that are opposed to each other. Finally there will be an integer N, followed by
//a single string containing N characters: the series of base elements you are to invoke. You will invoke them in the order they
//appear in the string (leftmost character first, and so on).
