#include <iostream>
#include <string>
#include <vector>
#include <map>
using std::cerr;
using std::string;
using std::cout;
using std::cin;
using std::map;
using std::vector;
using std::ostream;

typedef map<string, char> ICM;

string normpair(char x, char y)
{
	string s;
	if(x<y)
	{
		s += x;
		s += y;
	}
	else
	{
		s += y;
		s += x;
	}
	return s;
}

void opd(ostream & os, const vector<char> & res)
{
	for(int i =0; i < res.size(); i++)
	{
		if(i != 0)
			os << ", ";
		os << res[i];
	}
}

bool wantnuke(const ICM  & danger, const vector<char>  & list, char x)
{
	for(int i =0; i < list.size(); i++)
	{
		if(danger.find(normpair(list[i], x) ) != danger.end() )
			return true;
	}
	return false;
}


int main()
{
	int tc_count;
	cin >> tc_count;
	for(int tc_index=1; tc_index <= tc_count; tc_index++)
	{
		int c,d,sl;
		string t;

		ICM comb, die;
		
		cin >>c;
		for(int i = 0; i < c;i++)
		{
			cin >> t;
			comb[ normpair(t[0], t[1]) ] = t[2];
		}

		cin >>d;
		for(int i = 0; i < d;i++)
		{
			cin >> t;
			die[ normpair(t[0], t[1]) ] = 1;
		}

		cin >> sl;

		vector<char> res;
		for(int i = 0; i < sl; i++)
		{
			char c;
			cin >> c;
			if(res.size() == 0)
			{
				res.push_back(c);
				continue;
			}

			char p = res[res.size() -1];
			ICM::iterator ir = comb.find( normpair(c,p));
			if(ir != comb.end())
			{
				//combine
				res.pop_back();
				res.push_back(ir->second);
			}

			else if(wantnuke(die, res, c) )
			{
				res.clear();
			}
			else
			{
				res.push_back(c);
			}
//			opd(cerr, res);
//			cerr << "\n";
		}


		cout << "Case #" << tc_index <<  ": [" ;
		/*
		for(int i =0; i < res.size(); i++)
		{
			if(i != 0)
				cout << " ,";
			cout << res[i];
		}
		*/
    	opd(cout, res);
		cout << "]\n";
	}
	return 0;
}
