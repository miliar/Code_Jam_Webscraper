// 2011-qual-B.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <utility>


using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::map;
using std::set;
using std::vector;
using std::pair;
using std::make_pair;


int n(char c)
{
	return c - 'A';
}

char l(int i)
{
	return 'A' + i;
}


void test_case(int case_num)
{
	int num_combs = 0, num_opposers = 0, num_elements = 0;
	string input;
	int a, b;

	typedef map<pair<int, int>, int> comb_T;
	typedef set<pair<int, int> > opp_T;
	comb_T combinations;
	opp_T opposers;
	
	vector<int> element_list;

	cin >> num_combs;

	for (int i = 0; i < num_combs; i++)
	{
		cin >> input;
		a = n(input[0]);
		b = n(input[1]);

		combinations[make_pair(a, b)] = n(input[2]);
		combinations[make_pair(b, a)] = n(input[2]);
	}

	cin >> num_opposers;

	for (int i = 0; i < num_opposers; i++)
	{
		cin >> input;
		a = n(input[0]);
		b = n(input[1]);

		opposers.insert(make_pair(a, b));
		opposers.insert(make_pair(b, a));
	}

	cin >> num_elements >> input;

	for (int i = 0; i < num_elements; i++)
	{
		int v = n(input[i]);

		element_list.push_back(v);

		comb_T::iterator c;
		while (element_list.size() > 1 && (c = combinations.find(make_pair(a = *element_list.rbegin(), b = *(element_list.rbegin() + 1)))) != combinations.end())
		{
			element_list.pop_back();
			element_list.pop_back();
			element_list.push_back(c->second);
		}


		for (vector<int>::const_iterator j = element_list.begin(); j != element_list.end(); j++)
		{
			if (opposers.find(make_pair(*j, *element_list.rbegin())) != opposers.end())
			{
				element_list.clear();
				break;
			}
		}
	}

	cout << "Case #" << case_num + 1 << ": [";

	bool first = true;
	for (vector<int>::const_iterator i = element_list.begin(); i != element_list.end(); i++)
		if (first) {
			cout << l(*i); first = false;
		} else
			cout << ", " << l(*i);
	
	cout << "]" << endl;

}




int main(int argc, char* argv[])
{
	int num_cases = 0;

	cin >> num_cases;

	for (int i = 0; i < num_cases; i++)
		test_case(i);

	return 0;
}

