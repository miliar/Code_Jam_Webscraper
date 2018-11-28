#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <vector>


using namespace std;

int main()
{
	ifstream infile("b-in.txt");
	ofstream outfile("b-out.txt");

	int t;
	int c,d,n;

	infile >> t;

	for (int icase = 0; icase < t; ++icase)
	{
		cout << "Case " << icase << endl;

		typedef map<char, set<char> >::iterator iter2;
		typedef map<char, vector<pair<char, char> > >::iterator iter1;
		map<char, vector<pair<char, char> > > comb;
		map<char, set<char> > opp;
		infile >> c;

		for (int i = 0; i < c; ++i)
		{
			string s;
			infile >> s;
			comb[s[0]].push_back(make_pair(s[1], s[2]));
			comb[s[1]].push_back(make_pair(s[0], s[2]));
		}

		infile >> d;
		for (int i = 0; i < d; ++i)
		{
			string s;
			infile >> s;

			cout << "d " << s << endl;
			opp[s[0]].insert(s[1]);
			opp[s[1]].insert(s[0]);
		}

		infile >> n;

		string x;
		infile >> x;

		string ans;

		for (int i = 0; i < x.size(); ++i)
		{
			ans += x[i];
			bool loop = true;
			
			
			if (ans.size() > 1 && loop)
			{
				loop = false;
				char p = ans[ans.size()-2];
				char q = ans[ans.size()-1];

				cout << "here " << ans << endl;
				iter1 it = comb.find(p);
				if (it != comb.end())
				{
					for (int a = 0; a < it->second.size(); ++a)
					{
						if (q == (it->second)[a].first)
						{
							ans[ans.size()-2] = (it->second)[a].second;
							ans = ans.substr(0, ans.size()-1);
							loop = true;
							break;
						}
					}
				}

				if (!loop)
				{
					iter2 it1 = opp.find(q);
					if (it1 != opp.end())
					for (int j = 0; j < ans.size() - 1; ++j)
					{
						if (it1->second.count(ans[j]))
						{
							cout << "there j " << j << " " <<  ans << endl;

							ans = "";
							break;
						}
					}
				}

			}

			cout << ans << endl;

		}

		outfile << "Case #" << (icase + 1) << ": [";
		for (int i = 0; i < ans.size(); ++i)
		{
			if (i != 0) outfile << ", ";

			outfile << ans[i];
		}
		outfile << "]" << endl;
	}

	return 0;
}
