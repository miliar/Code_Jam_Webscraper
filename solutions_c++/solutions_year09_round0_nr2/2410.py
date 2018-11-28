#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <deque>
#include <list>
#include <map>
#include <bitset>
#include <functional>
#include <numeric>
#include <string>
#include <iterator>
#include <limits>
#include <sstream>
#include <iostream>
#include <stack>
using namespace std;

int main()
{
	ifstream in("B.in");
	ofstream out("B.out");
	int cases = 0;
	in >> cases;
	for(unsigned int case_number = 0; case_number < cases; ++case_number)
	{
		int h, w;
		in >> h >> w;
		vector<vector<int> > map(h, vector<int>(w, 0));
		for(int i = 0; i < h; ++i)
		{
			for(int j = 0; j < w; ++j)
			{
				in >> map[i][j];
			}
		}

		vector<vector<vector<pair<int, int> > > > adj_list(h, vector<vector<pair<int, int> > >(w));

		for(int i = 0; i < h; ++i)
		{
			for(int j = 0; j < w; ++j)
			{
				int target_alt = map[i][j];
				int target_i = -1;
				int target_j = -1;

				// North.
				if(i > 0 && map[i - 1][j] < target_alt)
				{
					target_alt = map[i - 1][j];
					target_i = i - 1;
					target_j = j;
				}

				// West.
				if(j > 0 && map[i][j - 1] < target_alt)
				{
					target_alt = map[i][j - 1];
					target_i = i;
					target_j = j - 1;
				}

				// East.
				if(j < w - 1 && map[i][j + 1] < target_alt)
				{
					target_alt = map[i][j + 1];
					target_i = i;
					target_j = j + 1;
				}

				// South.
				if(i < h - 1 && map[i + 1][j] < target_alt)
				{
					target_alt = map[i + 1][j];
					target_i = i + 1;
					target_j = j;
				}

				if(target_alt != map[i][j])
				{
					adj_list[i][j].push_back(pair<int, int>(target_i, target_j)); 
					adj_list[target_i][target_j].push_back(pair<int, int>(i, j));
				}
			}
		}

		int next_label = 0;
		vector<vector<bool> > visited(h, vector<bool>(w, false));
		vector<vector<int> > labels(h, vector<int>(w, 0));

		for(int i = 0; i < h; ++i)
		{
			for(int j = 0; j < w; ++j)
			{
				if(visited[i][j])
					continue;
				
				++next_label;
				stack<pair<int, int> > search;
				search.push(pair<int, int>(i, j));
				while(!search.empty())
				{
					pair<int, int> current = search.top();
					search.pop();
					labels[current.first][current.second] = next_label;
					visited[current.first][current.second] = true;
					for(int k = 0; k < adj_list[current.first][current.second].size(); ++k)
					{
						pair<int, int> next_node = adj_list[current.first][current.second][k];
						if(!visited[next_node.first][next_node.second])
						{
							search.push(next_node);
						}
					}
				}
			}
		}

		out << "Case #" << case_number + 1 << ":" << endl;
		for(int i = 0; i < h; ++i)
		{
			for(int j = 0; j < w; ++j)
			{
				if(j != 0)
					out << ' ';
				out << char(96 + labels[i][j]);
			}
			out << endl;
		}
	}
}