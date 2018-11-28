#include <set>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <cstdlib>
#include <numeric>
#include <iterator>
#include <iostream>
#include <algorithm>
using namespace std;

int n;
std::vector<int> pos;
std::vector<int> length;

bool Solve(int reach)
{	
	std::deque<std::pair<int, int> > q;
	std::set<std::pair<int, int> > visit;
	q.push_back(std::make_pair(0, pos[0]));
	while(q.size())
	{
		int nowPos = q.front().first;
		int nowLength = q.front().second;
		q.pop_front();
		if(pos[nowPos] + nowLength >= reach)
		{
			return true;
		}

		for(int i = nowPos + 1; i < pos.size() && pos[nowPos] + nowLength >= pos[i]; i++)
		{
			std::pair<int, int> nextState = std::make_pair(i, std::min(length[i], abs(pos[i] - pos[nowPos])));
			if(visit.count(nextState) == 0)
			{
				visit.insert(nextState);
				q.push_back(nextState);
			}
		}
	}

	return false;
}

int main(int argc, char * argv[])
{
	int reach;
	int testCount;
	freopen("in.txt", "r", stdin);
	std::cin >> testCount;
	for(int test = 1; test <= testCount; test++)
	{
		std::cin >> n;
		pos.resize(n);
		length.resize(n);
		pos[0] = length[0] = 0;
		for(int i = 0; i < n; i++)
		{
			std::cin >> pos[i] >> length[i];
		}

		std::cin >> reach;
		std::cout << "Case #" << test << ": " << (Solve(reach) ? "YES" : "NO") << std::endl;
	}

	return 0;
}