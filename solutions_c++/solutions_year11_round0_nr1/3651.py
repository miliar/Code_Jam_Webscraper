# include <fstream>
# include <iostream>
# include <map>

using namespace std;

int main(int argc, char **argv)
{
	ifstream in("input.in");
	ofstream out("output.out");
	int totalCase;
	in >> totalCase;
	char color;
	int value, count;


	for(int k = 1; k <= totalCase; k++)
	{
		map<int, map<char, int>> dataMap;
		in >> count;
		for(int i = 1; i <= count; i++)
		{
			map<char, int> tempMap;
			in >> color >> value;
			tempMap[color] = value;
			dataMap[i] = tempMap;
		}

		map<char, int> tempMap;
		map<char, int>::iterator it;
		tempMap = dataMap[1];
		it = tempMap.begin();
		int answer = 0;
		char currentRobot = it->first;
		int currentValue = 0;
		int oCount = 1, bCount = 1;
		int oButton = 1, bButton = 1;

		if(currentRobot == 'B'){bButton = it->second;}
		else if(currentRobot == 'O'){oButton = it->second;}

		currentValue = it -> second;
		answer += currentValue;
		for(int i = 2; i <= count; i++)
		{
			tempMap = dataMap[i];
			it = dataMap[i].begin();

			if(it->first != currentRobot)
			{
				if(it->first == 'B')
				{
					if(abs(bButton - it->second) - currentValue >= 0){
						currentValue = abs(bButton - it->second) - currentValue + 1;
					}
					else
					{
						currentValue=1;
					}
					bButton = it->second;
				}
				else if(it->first == 'O')
				{
					if(abs(oButton - it->second) - currentValue >= 0){
						currentValue = abs(oButton - it->second) - currentValue + 1;
					}
					else
					{
						currentValue=1;
					}
					oButton = it->second;
				}

				currentRobot = it->first;
				answer += currentValue;
			}
			else
			{
				if(currentRobot == 'B')
				{
					currentValue += abs(bButton - it->second) + 1;
					answer += abs(bButton - it->second) + 1;
					bButton = it->second;
				}
				else if(currentRobot == 'O')
				{
					currentValue += abs(oButton - it->second) + 1;
					answer += abs(oButton - it->second) + 1;
					oButton = it->second;
				}
			}
		}

		out << "Case #" << k << ": " << answer << endl;

	}
	return 0;
}