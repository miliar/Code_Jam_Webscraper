// P1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

class TestCase
{
public:
	TestCase() 
		: m_ChangeCount(0)
		, m_CurrentEngineIndex(0)
	{
		
	}

	~TestCase() 
	{
		m_SearchEngines.clear();
		m_Queries.clear();
	}

	bool Init(ifstream& stream)
	{
		string temp;

		int engineCount = 0;
		stream >> engineCount;
		
		if (!engineCount)
			return false;

		getline(stream, temp);

		for (int i = 0; i < engineCount; i++)
		{
			getline(stream, temp);

			m_SearchEngines.push_back(temp);
		}

		int queryCount = 0;
		stream >> queryCount;
		if (queryCount)
		{
			getline(stream, temp);

			for (int i = 0; i < queryCount; i++)
			{
				getline(stream, temp);

				m_Queries.push_back(temp);
			}
		}
		
		return true;
	}

	void Process()
	{
		map<string, bool> checked;
		for (int i = 0; i < m_SearchEngines.size(); i++)
		{
			checked[m_SearchEngines[i]] = false;
		}

		int count = m_SearchEngines.size();

		for (int i = 0; i < m_Queries.size(); i++)
		{
			string query = m_Queries[i];
			if (checked.find(query) != checked.end() && !checked[query])
			{
				checked[query] = true;
				count--;

				if (!count)
				{
					count = m_SearchEngines.size();
					m_ChangeCount++;

					for (int i = 0; i < m_SearchEngines.size(); i++)
					{
						checked[m_SearchEngines[i]] = false;
					}

					checked[query] = true;
					count--;
				}
			}
		}
	}

	int GetChangeCount()
	{
		return m_ChangeCount;
	}

private:
	vector<string> m_SearchEngines;
	vector<string> m_Queries;
	int m_CurrentEngineIndex;
	int m_ChangeCount;
};

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inputStream("A-Large.in");
	
	int testCount = 0;
	inputStream >> testCount;

	vector<TestCase*> testCases;
	testCases.reserve(testCount);

	for (int i = 0; i < testCount; i++)
	{
		TestCase *tc = new TestCase();
		
		if (!tc->Init(inputStream))
		{
			delete tc;
			break;
		}

		tc->Process();
		
		testCases.push_back(tc);
	}
	
	ofstream outputStream("A-Large.out");
	
	for (int i = 0; i < testCount; i++)
	{
		outputStream << "Case #" << i + 1 << ": " << testCases[i]->GetChangeCount() << endl;
		delete testCases[i];
	}

	testCases.clear();

	return 0;
}

