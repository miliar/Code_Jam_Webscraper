
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main()
{
	ifstream in("B-large.in");
	//ifstream in("sample.txt");
	ofstream out("B_large.txt");

	int T;
	in >> T;


	for (int i=0; i<T; ++i)
	{
		map<pair<char, char>, char> combinations;
		vector<pair<char, char> > cancels;

		int C;
		in >> C;

		for (int j=0; j<C; ++j)
		{
			string s;
			in >> s;
			pair<char, char> key(s[0], s[1]);
			combinations[key] = s[2];
			pair<char, char> key2(s[1], s[0]);
			combinations[key2] = s[2];
		}

		int D;
		in >> D;

		for (int j=0; j<D; ++j)
		{
			string s;
			in >> s;
			pair<char, char> opp(s[0], s[1]);
			cancels.push_back(opp);
			pair<char, char> opp2(s[1], s[0]);
			cancels.push_back(opp2);
		}

		int N;
		in >> N;

		string s;
		in >> s;

		vector<char> result;
		for (int j=0; j<N; ++j)
		{
			result.push_back(s[j]);

			int size = result.size();
			if (size > 1)
			{
				map<pair<char, char>, char>::iterator itr = combinations.find(pair<char, char>(result[size-2], result[size-1]));
				if (itr != combinations.end())
				{
					result.pop_back();
					result.pop_back();
					result.push_back(itr->second);
				}
				else
				{
					for (size_t k=0; k<cancels.size(); ++k)
					{
						if (s[j] == cancels[k].first)
						{
							if (result.size() > 1)
							{
								for (size_t l=0; l<result.size()-1; ++l)
								{
									if (result[l] == cancels[k].second)
									{
										result.clear();
										break;
									}
								}
							}
						}
					}
				}
			}
		}

		cout << "Case #" << i+1 << ": [";
		out << "Case #" << i+1 << ": [";
		
		for (size_t j=0; j<result.size(); ++j)
		{
			if (j != 0)
			{
				cout << ", ";
				out << ", ";
			}

			cout << result[j];
			out << result[j];
		}

		cout << "]" << endl;
		out << "]" << endl;
	}

	return 0;
}
