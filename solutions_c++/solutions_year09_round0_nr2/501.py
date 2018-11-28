#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <utility>
using namespace std;
typedef vector<int> VI;
pair<int, int> dirs[] =
{
	make_pair(-1, 0),
	make_pair(0, -1),
	make_pair(0, 1),	
	make_pair(1, 0)
};
bool In(int i, int j, int n, int m)
{
	return i < n && i >= 0 && j < m && j >= 0;
}
char Mark(const vector<VI> & heights, vector<VI> & answer, int i, int j, char & sink)
{
	if(answer[i][j] != 0)
		return answer[i][j];
	int minH = INT_MAX;
	for(int d = 0; d < 4; d++)
	{
		int i0 = i + dirs[d].first;
		int j0 = j + dirs[d].second;
		if(In(i0, j0, heights.size(), heights[0].size()))
			minH = min(minH, heights[i0][j0]);		
	}
	if(minH >= heights[i][j])
		minH = INT_MAX;
	for(int d = 0; d < 4; d++)
	{
		int i0 = i + dirs[d].first;
		int j0 = j + dirs[d].second;
		if(In(i0, j0, heights.size(), heights[0].size()) && heights[i0][j0] == minH)		
			return answer[i][j] = Mark(heights, answer, i0, j0, sink);
	}
	return answer[i][j] = sink++;
}
int main()
{
	int t, n, m;
	ifstream in("in.txt");
	in >> t;
	vector<VI> answer;
	vector<VI> heights;		
	for(int i = 0; i < t; i++)
	{
		in >> n >> m;
		heights.assign(n, VI(m, 0));
		answer.assign(n, VI(m, 0));
		for(int j = 0; j < n; j++)
			for(int k = 0; k < m; k++)
				in >> heights[j][k];
		char sink = 'a';
		for(int j = 0; j < n; j++)
			for(int k = 0; k < m; k++)
				Mark(heights, answer, j, k, sink);
		cout << "Case #" << i + 1 << ": " << endl;
		for(int j = 0; j < n; j++)
		{
			for(int k = 0; k < m; k++)
				cout << char(answer[j][k]) << ' ';
			cout << endl;
		}
	}
	return 0;
}