#include "SaveUniversity.h"

void SaveUniversity::readFromFile(string filename)
{
	ifstream in;
	in.open(filename.c_str());
	string numOfCases;
	getline(in, numOfCases, '\n');
	istringstream iss(numOfCases);
	iss >> m_Cases;
	cout << "Num of cases:" << m_Cases << endl;
	
	for (int k = 0; k < m_Cases; ++k)
	{	
		vector<string> engines;
		m_Engines.push_back(engines);
		vector<string> queries;
		m_Queries.push_back(queries);
		//	read engines
		string sNumOfEngines;
		getline(in, sNumOfEngines, '\n');
		int numOfEngines;
		istringstream iss2(sNumOfEngines);
		iss2 >> numOfEngines;
		//cout << "Num of engines:" << numOfEngines << endl;
		int i = 0;
		while(i < numOfEngines)
		{
			string engine;
			getline(in, engine, '\n');
			m_Engines[k].push_back(engine);
			++i;
		}
		//cout << m_Engines[k].size() << endl;

		//	read queries
		string sNumOfQueries;
		getline(in, sNumOfQueries, '\n');
		int numOfQueries;
		istringstream iss3(sNumOfQueries);
		iss3 >> numOfQueries;
		//cout << "Num of queries:" << numOfQueries << endl;
		i = 0;
		while(i < numOfQueries)
		{
			string query;
			getline(in, query, '\n');
			m_Queries[k].push_back(query);
			++i;
		}
		//cout << m_Queries[k].size() << endl;
		//cout << m_Engines[k].size() << ":" << m_Queries[k].size() << endl;
	}

}

int SaveUniversity::minTurn(int index)
{
	int min = 0;

	if (m_Queries[index].size() == 0)
	{
		return 1;
	}

	int visited = 0;
	while(visited <= m_Queries[index].size() - 1)
	{
		//	find the suitable engine
		int maxQuery = 0;
		int pos = -1;
		deque<string>::iterator itr;


		for (int i = 0; i < m_Engines[index].size(); ++i)	//	find each engine
		{

			int numOfQuery = 0;
			for (int j = visited; j < m_Queries[index].size(); ++j)
			{
				if (m_Engines[index][i] != m_Queries[index][j])
				{
					++numOfQuery;
				}
				else	//	if equal, change engine
				{
					break;
				}
			}
			if (numOfQuery > maxQuery)
			{
				maxQuery = numOfQuery;
				pos = i;
			}
		}

		visited = visited + maxQuery;	//	next start query

		cout << m_Engines[index][pos] << ":" << maxQuery << endl;
		++min;

	}

	return min;
}

void SaveUniversity::mins()
{
	int *minQ = new int[m_Cases];
	cout << "In mins\n";
	for (int i = 0; i < m_Cases; ++i)
	{
		minQ[i] = minTurn(i) - 1;
		cout << "Case #" << (i + 1) << ": " << minQ[i] << ", with " << m_Engines[i].size() << " engines and " << m_Queries[i].size() << " queries." << endl;
	}
	

	string filename("./outputSaveUniversity.txt");
	ofstream out;
	out.open(filename.c_str());
	for (int i = 0; i < m_Cases; ++i)
	{
		out << "Case #" << (i + 1) << ": " << minQ[i] << endl;
	}
}