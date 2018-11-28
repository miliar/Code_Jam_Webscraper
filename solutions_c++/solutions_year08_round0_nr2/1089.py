#pragma once

#include <vector>

class TestCase
{
public:
	TestCase(unsigned int NewTATime, unsigned int MoveCount)
	{
		TATime=NewTATime;
		TimeTable.reserve(MoveCount);
	}
	virtual ~TestCase();

	void AddEntry(unsigned int Time, bool IsArrival);

	void DumpTT();

	int GetMinTrains();

private:
	struct TTEntry
	{
		unsigned int Time;
		bool IsArrival;

		/*bool operator<(const TTEntry &Op1)
		{
			if (Op1.Time==Time)
				return Op1.IsArrival;
			else
				return Op1.Time<Time;
		}*/
	};

	unsigned int TATime;
	std::vector<TTEntry> TimeTable;

	static bool Sorter(TTEntry Op1, TTEntry Op2);
};
