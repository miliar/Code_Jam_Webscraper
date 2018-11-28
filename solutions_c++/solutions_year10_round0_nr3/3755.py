#include <iostream>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <valarray>
#include <queue>

typedef long unsigned int MyInt;

MyInt TestCount = 0;

MyInt calculateMoney(MyInt rollerCoasterRunCount, MyInt rollerCoasterCapacity,  std::valarray<int>& groupMembers)
{
	MyInt totalMoney = 0;

	while(rollerCoasterRunCount--)
	{
		int personCountOnRun = 0;
		
		int i = 0;
		MyInt totalPerson = 0;
		for ( ; i < groupMembers.size() ; ++i)
		{
			if (totalPerson + groupMembers[i] <= rollerCoasterCapacity)
			{
				totalPerson += groupMembers[i];
			}
			else
			break;
		}
		groupMembers = groupMembers.cshift(i);
		totalMoney += totalPerson;
	}

	return totalMoney;
}

int main()
{
	std::ifstream in("data.in");
	std::ofstream out("results.txt");
	in >> TestCount;

	int caseCount = 1;
	while(TestCount--)
	{
		//R
		MyInt rollerCoasterRunCount = 0;
		//k
		MyInt rollerCoasterCapacity = 0;
		//N
		MyInt numberOfGroups = 0;

		in >> rollerCoasterRunCount >>rollerCoasterCapacity >> numberOfGroups;

		std::valarray<int> groupMembers(numberOfGroups);
		int i = 0;
		while(numberOfGroups--)
		{
			int groupMemberCount = 0;
			in >> groupMemberCount;
			groupMembers[i++] = groupMemberCount;
		}

		MyInt euroCounted = calculateMoney(rollerCoasterRunCount, rollerCoasterCapacity, groupMembers);
		
		out << "Case " << "#" << caseCount++ << ": ";
		out << euroCounted << std::endl;
	}
	return 0;
}