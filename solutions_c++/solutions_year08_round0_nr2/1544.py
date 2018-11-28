#include <iostream>
#include <tchar.h>

#include <list>
#include <string>

using namespace std;

void readData(list<int> &_station, list<int> &_train, const int _turnTime, int count)
{
	while (count)
	{
		int _depH, _depM, _arrH, _arrM;
		scanf("%d:%d %d:%d", &_depH, &_depM, &_arrH, &_arrM);
		_depM += _depH * 60;
		_arrM += _arrH * 60;
		
		_station.push_back(_depM);
		_train.push_back(_arrM + _turnTime);

		--count;
	}
	_station.sort();
	_train.sort();
}

int doIt(list<int> &_station, list<int> &_train)
{
	int count = 0;
	list<int>::iterator itT = _train.begin();

	for (list<int>::iterator itS = _station.begin(); itS != _station.end(); itS++)
	{
		if (itT != _train.end())
		{
			if ((*itS) < (*itT))
				++count;
			else
				++itT;
		}
		else
			++count;
	}
	return count;
}

int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
	int nRetCode = 0;

	int _caseCount;
	cin >> _caseCount;

	for (int _case = 0; _case < _caseCount; ++_case)
	{
		int _turnTime;
		cin >> _turnTime;

		int _aCount, _bCount;
		cin >> _aCount;
		cin >> _bCount;
		char _buf[100];
		cin.getline(_buf, 100);
		
		list<int> _stationA;
		list<int> _stationB;

		list<int> _trainA;
		list<int> _trainB;
	
		readData(_stationA, _trainB, _turnTime, _aCount);
		readData(_stationB, _trainA, _turnTime, _bCount);	
	
		cout << "Case #" << _case + 1 << ": " << doIt(_stationA, _trainA) << " " << doIt(_stationB, _trainB);
		cout << "\n";

		//do it
	}	

	return 0;
}
