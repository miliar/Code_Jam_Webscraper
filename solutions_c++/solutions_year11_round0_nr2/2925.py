#include <fstream>
#include <string>
#include <utility>
#include <map>
#include <set>
using namespace std;

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	string elm;
	int T, C, D, N;
	map<pair<char, char>, char>  combine;
	map<pair<char, char>, char>::iterator combine_finder;
	set<pair<char, char> > opposite;
	set<pair<char, char> >::iterator opposite_finder;

	cin >> T;
	for	(int t = 0; t < T; t++)
	{
		combine.clear();
		opposite.clear();

		cin >> C;
		for(int i = 0; i < C; i++)
		{
			cin >> elm;
			combine[make_pair(elm[0], elm[1])] = elm[2];
		}

		cin >> D;
		for(int i = 0; i < D; i++)
		{
			cin >> elm;
			opposite.insert(make_pair(elm[0], elm[1]));
		}

		cin >> N;
		cin >> elm;
		
		bool isCleared;
		string out;
		for(int i = 0; i < N; i++)
		{
			if(out.size() == 0)
			{
				out += elm[i];
				continue;
			}
			combine_finder = combine.find(make_pair(elm[i], out.back()));
			if(combine_finder == combine.end())
			{
				combine_finder = combine.find(make_pair(out.back(), elm[i]));
			}
			
			if(combine_finder != combine.end())
			{
				out.back() = combine_finder->second;
			}
			else
			{
				isCleared = false;
				int size = out.size();
				for(int j = 0; j < size && !isCleared; j++)
				{
					opposite_finder = opposite.find(make_pair(elm[i], out[j]));
					if(opposite_finder == opposite.end())
					{
						opposite_finder = opposite.find(make_pair(out[j], elm[i]));
					}

					if(opposite_finder != opposite.end())
					{
						out.clear();
						isCleared = true;
					}
				}
				if(!isCleared)
				{
					out += elm[i];
				}
			}
		}
		
		int size = out.size() - 1;
		cout << "Case #" << t + 1 << ": [";
		for(int i = 0; i < size; i++)
		{
			cout << out[i] << ", ";
		}
		if(size >= 0) cout << out[size];
		cout << "]" << endl;
	}

	return 0;
}