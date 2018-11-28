#include <iostream>
#include <tchar.h>

#include <list>
#include <string>

using namespace std;

int doIt(list<string> &orgEngines, list<string>::const_iterator &it, list<string>::const_iterator &itLast, string &currentEngine)
{
	list<string> engines = orgEngines;
	if (!currentEngine.empty())
		engines.remove(currentEngine);

	while (engines.size() && it != itLast)
	{
		for (; it != itLast && engines.size(); ++it)
		{
			currentEngine = *(engines.begin());
			engines.remove(*it);
		}
	}
	if (it == itLast)
		return engines.size() == 0;
	else
		return 1 + doIt(orgEngines, it, itLast, currentEngine);
}

int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
	int nRetCode = 0;

	int _caseCount;
	cin >> _caseCount;

	for (int _case = 0; _case < _caseCount; ++_case)
	{
		list<string> _engines;
		list<string> _searchStrings;
		const int BUF_SIZE = 101;
		char _buf[BUF_SIZE];

		//odczytaj wyszukiwarki
		int _enginesCount;
		cin >> _enginesCount;
		cin.getline(_buf, BUF_SIZE);
		for (int _engine = 0; _engine < _enginesCount; ++_engine)
		{
			cin.getline(_buf, BUF_SIZE);
			_engines.push_back(_buf);
		}

		//odczytaj frazy
		int _frazeCount;
		cin >> _frazeCount;
		cin.getline(_buf, BUF_SIZE);
		for (int _engine = 0; _engine < _frazeCount; ++_engine)
		{
			cin.getline(_buf, BUF_SIZE);
			_searchStrings.push_back(_buf);
		}

		string tempStr;
		cout << "Case #" << _case + 1 << ": " << doIt(_engines, _searchStrings.begin(), _searchStrings.end(), tempStr);
		cout << "\n";

		//do it
	}	

	return 0;
}
