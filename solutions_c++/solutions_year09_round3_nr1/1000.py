#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>
#include <sstream>
#include <set>
#include <algorithm>

using namespace std;

void create_vector(string s, vector<int>& v, int &base)
{
	int i;
	int changes = 0;
	string t = s;
	v.clear();
	v.resize(s.size(), 0);
	set<char> used;
	int first_not_visited;
	int first_digit_available = 1;

	char current = s[0];

	for(i = 0; i < s.size(); ++i)
	{
		if( s[i] == current )
		{
			t[i] = '.';
			v[i] = 1;
			++changes;
		}
	}



	if( changes < s.size() )
	{
		first_not_visited = t.find_first_not_of('.', 0);
		current = s[first_not_visited];
		for(i = first_not_visited; i < s.size(); ++i)
		{
			if( s[i] == current )
			{
				t[i] = '.';
				++changes;
			}
		}

		while( changes < s.size() )
		{
			++first_digit_available;
			first_not_visited = t.find_first_not_of('.', first_not_visited);
			current = s[first_not_visited];
			for(i = first_not_visited; i < s.size(); ++i)
			{
				if( s[i] == current )
				{
					t[i] = '.';
					v[i] = first_digit_available;
					++changes;
				}
			}
		}
	}

	base = first_digit_available + 1;

	reverse(v.begin(), v.end());
}


int convert_vector_to_base10(const vector<int>& v, int b)
{
	int result = 0;
	int pos = 1;
	for(int i = 0; i < v.size(); ++i)
	{
		result += pos * v[i];
		pos *= b;
	}

	return result;
}

void print_vector(const vector<int>& v)
{
	int i = v.size() - 1;
	cout << v[i];
	for(--i; i >= 0; --i)
	{
		cout << " " << v[i];
	}
	cout << endl;
}

int main(int argc, char** argv)
{
	int T;

	string str;
	vector<int> str_equiv;
	int base, num;

//#	define __USINGFILE 1
#	if defined( __USINGFILE)
	if( argc < 2 )
	{
		cerr << "error: no input file" << endl;
		return -1;
	}
	ifstream in(argv[1]);
#	else
	istream& in = cin;
#	endif


	in >> T;
	//cout << "T: " << T << endl;
	for(int t = 0; t < T; ++t)
	{
		in >> str;

		//cout << "Line: " << str << endl;

		create_vector(str, str_equiv, base);

		//cout << "str_equiv: "; print_vector(str_equiv);
		//cout << "base: " << base << endl;

		num = convert_vector_to_base10(str_equiv, base);

		cout << "Case #" << (t+1) << ": " << num << endl;
	}

	return 0;
}
