#pragma once

#include <vector>
#include <string>

class TestCase
{
public:
	TestCase(int EngineCount);
	virtual ~TestCase();

	void AddEngine(const char *NewName) { EngineA.push_back(NewName); }
	
	void SetQueryCount(unsigned int QCount) { QueryA.reserve(QCount); }
	void AddQuery(const char *NewQuery) { QueryA.push_back(NewQuery); }

	int RunQuerys();

private:
	class UseArray
	{
	public:
		UseArray(unsigned int Size) { UsageA.resize(Size,false); MarkedCount=0; }
		~UseArray() { }

		void Reset();
		void Mark(unsigned int Index);
		void UnMark(unsigned int Index);

		unsigned int GetMarkedCount() { return MarkedCount; }
		bool IsFull() { return MarkedCount==UsageA.size(); }

	private:
		std::vector<bool> UsageA;
		unsigned int MarkedCount;
	};

	std::vector<std::string> EngineA;
	std::vector<std::string> QueryA;

	int GetEngineI(std::string &Query);
};