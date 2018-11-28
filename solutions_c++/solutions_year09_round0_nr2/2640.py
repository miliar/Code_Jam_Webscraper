#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

int W;
int H;

char findBasin(std::vector<std::vector<int>>& altitudeList, 
			   std::vector<std::vector<char>>& sinkMap,
			   int i, int k,
				int currentAltitude)
{
	if (i < 0 || k < 0 || i >= H || k >= W)
	{
		return 'A';
	}

	int left = 101;
	int right = 101;
	int up = 101;
	int down = 101;
	if ( i > 0)
	{
		up = altitudeList.at(i - 1).at(k);
	}
	if (i < H - 1)
	{
		down = altitudeList.at(i + 1).at(k);
	}
	if (k > 0 )
	{
		left = altitudeList.at(i).at(k - 1);
	}
	if (k < W - 1)
	{
		right = altitudeList.at(i).at(k + 1);
	}
	if (up <= down && up <= left && up <= right)
	{
		if (sinkMap.at(i - 1).at(k) != 'A')
		{
			return sinkMap.at(i - 1).at(k); 
		}
		return findBasin(altitudeList, sinkMap, i - 1, k,up);
	}
	if (left <= up && left <= down && left <= right)
	{
		if (sinkMap.at(i).at(k - 1) != 'A')
		{
			return sinkMap.at(i).at(k - 1); 
		}
		return findBasin(altitudeList, sinkMap, i, k - 1, left);
	}
	if (right <= up && right <= left && right <= down)
	{
		if (sinkMap.at(i).at(k + 1) != 'A')
		{
			return sinkMap.at(i).at(k + 1); 
		}
		return findBasin(altitudeList, sinkMap, i, k + 1, right);
	}
	if (down <= up && down <= left && down <= right)
	{
		if (sinkMap.at(i+1).at(k) != 'A')
		{
			return sinkMap.at(i+1).at(k); 
		}
		return findBasin(altitudeList, sinkMap, i + 1, k, down);
	}


	return 'A';
}

std::string findDrainage(std::vector<std::vector<int>>& altitudeList)
{
	std::vector<std::vector<char>> sinkMap;

	sinkMap.resize(H);
	for (int i = 0 ; i < H ; ++i)
	{
		sinkMap[i].resize(W);
		for (int k = 0 ; k < W ; ++k)
		{
			sinkMap[i][k] = 'A';
		}
	}

	char sink = 'a';
	
	for (int i = 0 ; i < H ; ++i)
	{
		for (int k = 0 ; k < W ; ++k)
		{
			int current = altitudeList.at(i).at(k);

			int left = 101;
			int right = 101;
			int up = 101;
			int down = 101;
			if ( i > 0)
			{
				up = altitudeList.at(i - 1).at(k);
			}
			if (i < H - 1)
			{
				down = altitudeList.at(i + 1).at(k);
			}
			if (k > 0 )
			{
				left = altitudeList.at(i).at(k - 1);
			}
			if (k < W - 1)
			{
				right = altitudeList.at(i).at(k + 1);
			}
			if (current <= left && current <= right && current <= up && current <= down && sinkMap[i][k] == 'A')
			{
				sinkMap.at(i).at(k) = sink;
				sink++;
			}
			
			if ((current == left || left == 101) && (current == right ||right == 101)
				&& (current == down || down == 101) && (current == up || up == 101) && sinkMap[i][k] == 'A')
			{
				sinkMap.at(i).at(k) = sink;
				sink++;
			}
		}
	}

	for (int i = 0 ; i < H ; ++i)
	{
		for (int k = 0 ; k < W ; ++k)
		{
			if (sinkMap[i][k] == 'A')
			{
				sinkMap[i][k] = findBasin(altitudeList, sinkMap, i, k, altitudeList.at(i).at(k));
			}
		}
	}

	

	std::stringstream result;
	for (int i = 0 ; i < H ; ++i)
	{
		for (int k = 0 ; k < W ; ++k)
		{
			result << (sinkMap[i][k]) << " " ;
		}
		result << ('\n');
	}

	std::string resultUnsorted = result.str();
	char c = 'a';
		for (int i = 0 ; i < H ; ++i)
		{
			for (int k = 0 ; k < W ; ++k)
			{
				if (sinkMap[i][k] > c)
				{
					char charToReplace = sinkMap[i][k];
					std::replace(resultUnsorted.begin(), resultUnsorted.end(), c, 'X');
					std::replace(resultUnsorted.begin(), resultUnsorted.end(), charToReplace, c);
					std::replace(resultUnsorted.begin(), resultUnsorted.end(), 'X', charToReplace);
					c++;
				}
				if (sinkMap[i][k] == c)
				{
					c++;
				}
			}
		}
	return resultUnsorted;
}

int main()
{
	std::ifstream input("C:\\in.txt");
	std::ofstream output("C:\\out.txt");
	
	std::vector<std::string> resultLisT;
	

	int T;
	input >> T;
	while(T--)
	{
		input >> H >> W;

		std::vector<std::vector<int>> altitudeMap;
		altitudeMap.resize(H);
		for (int i = 0; i < H ; ++i)
		{
			altitudeMap[i].resize(W);
			for (int k = 0 ; k < W ; ++k)
			{
				int altitude;
				input >> altitude;
				altitudeMap[i][k] = altitude;
			}
		}

		std::string result = findDrainage(altitudeMap);
		resultLisT.push_back(result);
	}

	for (int i = 0 ; i < resultLisT.size() ; ++i)
	{
		std::stringstream stream;
		output << "Case #" << i + 1 << ": " << std::endl;
		output << resultLisT.at(i);
	}

	return 0;
}