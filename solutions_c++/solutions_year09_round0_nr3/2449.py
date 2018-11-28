#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
#include <list>
#include <map>
#include <vector>

using namespace std;

#define MAXBUFFER 502

void FindAvailableString(const char * _base, int & _nbaselen, int _nchar, char * _start, int & currentCount)
{
	while((*_start) != '\0')
	{
		if (*_start == _base[_nchar])
		{
			if (_nchar == _nbaselen - 1) 
			{
				++currentCount;
				if (currentCount > 10000) currentCount %= 10000;
			}
			else FindAvailableString(_base, _nbaselen, _nchar + 1, _start + 1, currentCount);
		}
		++_start;
	}
}

int main(int argc, char * argv[])
{
	if (argc != 2) return -1;
	list<char *> _buffer; 
	ifstream inputFile(argv[1], ios_base::in);

	string strLines;
	std::getline(inputFile, strLines);

	int nLines;
	//inputFile >> nLines;
	nLines = atoi(strLines.c_str());
	// Get the input strings.
	for (int i = 0; i < nLines; ++i)
	{
		char * _tmp = new char[MAXBUFFER];
		memset(_tmp, 0, MAXBUFFER);
		//_getLine(inputFile, _tmp);
		inputFile.getline(_tmp, MAXBUFFER);
		_buffer.push_back(_tmp);
	}

	char _base[] = "welcome to code jam";
	int nbaseLen = strlen(_base);

	ofstream outfile("out.txt", ios_base::out);
	list<char *>::iterator _bufferIt = _buffer.begin();
	for (int i = 0; i < (int)_buffer.size(); ++i, ++_bufferIt)
	{
		int nCurrentCount = 0;
		// Do something to solve the problem.
		FindAvailableString(_base, nbaseLen, 0, (*_bufferIt), nCurrentCount);
		char _result[5] = {0};
		_result[0] = nCurrentCount / 1000 + 48;
		nCurrentCount -= (nCurrentCount / 1000) * 1000;
		_result[1] = nCurrentCount / 100 + 48;
		nCurrentCount -= (nCurrentCount / 100) * 100;
		_result[2] = nCurrentCount / 10 + 48;
		nCurrentCount -= (nCurrentCount / 10) * 10;
		_result[3] = nCurrentCount + 48;
		outfile << "Case #" << i + 1 << ":\t" << _result << endl;
	}

	// Release the resource.
	for(list<char *>::iterator lstIt = _buffer.begin();
		lstIt != _buffer.end(); delete *lstIt, ++lstIt);

	return 0;
}