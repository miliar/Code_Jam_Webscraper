#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <boost/regex.hpp>

using namespace std;

typedef vector<string>::iterator vst;
typedef vector<int>::iterator vit;

int main(int argc, char** argv)
{
	if(argc<2)
		exit(0);

	//file input
	ifstream in;
	in.open(argv[1]);

	vector<string> h,v;

	boost::regex xWins("[XT]{4}");
	boost::regex oWins("[OT]{4}");

	int n = 0;
	in >> n;
	for(int i=0; i<n; i++)
	{
		cout << "Case #" << i+1 << ": ";
		bool bNoDrawPossible = false;
		h.clear(); v.clear();
		for(int idx=0; idx<4; idx++)
			v.push_back("");

		for(int j=0; j<4; j++)
		{
			string s;
			in >> s;
			h.push_back(s);
			for(int k=0; k<s.size(); k++)
			{
				v[k] += s[k];
				if(s[k] == '.')
					bNoDrawPossible = true;
			}
		}

		// Check diagonals first
		string d1="", d2="";
		for(int j=0; j<4; j++)
		{
			d1 += h[j][j];
			d2 += h[3-j][j];
		}

		if( boost::regex_match(d1, xWins) || boost::regex_match(d2, xWins) ) {
			cout << "X won" << endl;
			continue;
		}

		if( boost::regex_match(d1, oWins) || boost::regex_match(d2, oWins) ) {
			cout << "O won" << endl;
			continue;
		}

		//cout << d1 << endl << d2 << endl << "Diags ^^" << endl;

		bool bC = false;
		for(vst it = h.begin(); it != h.end(); it++)
		{
			//cout << *it << endl;
			if( boost::regex_match(*it, xWins) )
			{
				cout << "X won" << endl;
				bC = true;
				continue;
			}

			if( boost::regex_match(*it, oWins) )
			{
				cout << "O won" << endl;
				bC = true;
				continue;
			}
		}
		if(bC)
			continue;

		//cout << "transpose" << endl;
	
		for(vst it = v.begin(); it != v.end(); it++)
		{
			//cout << *it << endl;
			if( boost::regex_match(*it, xWins) )
			{
				cout << "X won" << endl;
				bC = true;
				continue;
			}

			if( boost::regex_match(*it, oWins) )
			{
				cout << "O won" << endl;
				bC = true;
				continue;
			}
		}

		if(bC)
			continue;
	
		if(bNoDrawPossible)
			cout << "Game has not completed" << endl;
		else
			cout << "Draw" << endl;
	}

	//cout << "Hello!" << endl;
	in.close();
	return 0;
}

