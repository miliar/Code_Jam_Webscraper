#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

const unsigned int NumDigits = 50;

const string
reverse (
	const string &str
) {
	string result;

	for (string::const_iterator it = str.begin();
	     it != str.end();
	     it++)
	{
		result = *it + result;
	}

	return result;
}

const string
add (
	const string &u,
	const string &v
) {
	if (u.length() != NumDigits
	||  v.length() != NumDigits)
	{
		return string();
	}

	int k = 0;
	string w(NumDigits, '0');

	for (unsigned int j = 0; j < NumDigits; j++)
	{
		int i = NumDigits - 1 - j;
		int tmp = (u[i] - '0') + (v[i] - '0') + k;
		w[i] = '0' + ((tmp + 10) % 10);
		k = (tmp + 10) / 10- 1;
	}

	if (k != 0)
	{
		cerr << "Overflow!" << endl;
	}

	return w;
}

const string
subtract (
	const string &u,
	const string &v
) {
	if (u.length() != NumDigits
	||  v.length() != NumDigits)
	{
		return string();
	}

	if (u.compare(v) < 0)
	{
		cerr << "Error! (" << __LINE__ << ")" << endl;
		cerr << "u: " << u << endl;
		cerr << "v: " << v << endl;
	}

	int k = 0;
	string w(NumDigits, '0');

	for (unsigned int j = 0; j < NumDigits; j++)
	{
		int i = NumDigits - 1 - j;
		int tmp = (u[i] - '0') - (v[i] - '0') + k;
		w[i] = '0' + ((tmp + 10) % 10);
		k = (tmp + 10) / 10 - 1;
	}

	if (k != 0)
	{
		cerr << "Error! (" << __LINE__ << ")" << endl;
	}

	return w;
}

int
main (
	int argc,
	char **argv
) {
	if (argc < 2)
	{
		cerr << "no input data specified." << endl;
		return -1;
	}

	fstream fin(argv[1], ios::in);

	int C;
	fin >> C;

	for (int c = 0; c < C; c++)
	{
		cout << "Case #" << (c + 1) << ": ";

		int N;
		fin >> N;

		vector< string >::iterator it;
		vector< string > seconds;
		for (int n = 0; n < N; n++)
		{
			string buffer;
			fin >> buffer;
			while (buffer.length() < NumDigits)
			{
				buffer = '0' + buffer;
			}
			seconds.push_back(buffer);
		}
		sort(seconds.begin(), seconds.end());
		it = unique(seconds.begin(), seconds.end());
		seconds.resize(it - seconds.begin());

		vector< string > diffs;
		for (int n = 0, size = seconds.size(); n < size - 1; n++)
		{
			diffs.push_back(subtract(seconds[n + 1], seconds[n]));
		}
		sort(diffs.begin(), diffs.end());
		it = unique(diffs.begin(), diffs.end());
		diffs.resize(it - diffs.begin());

		string interval;
		while (true)
		{
			/*
			cout << "diffs: " << endl;
			for (int i = 0, size = diffs.size(); i < size; i++)
			{
				cout << diffs[i] << endl;
			}
			cout << endl;
			*/

			if (diffs[0].compare(string("00000000000000000000000000000000000000000000000000")) == 0)
			{
				cerr << "Error! (" << __LINE__ << ")" << endl;
				exit(-1);
			}

			if (diffs.size() == 1
			||  diffs[0].compare(string("00000000000000000000000000000000000000000000000001")) == 0)
			{
				interval = diffs[0];
				break;
			}

			vector< string > _diffs;
			_diffs.push_back(diffs.front());
			for (int i = 1, size = diffs.size(); i < size; i++)
			{
				_diffs.push_back(subtract(diffs[i], diffs[i - 1]));
			}
			sort(_diffs.begin(), _diffs.end());
			it = unique(_diffs.begin(), _diffs.end());
			_diffs.resize(it - _diffs.begin());

			diffs = _diffs;
		}

		string buffer = string(interval);
		while (buffer.compare(seconds.front()) < 0)
		{
			buffer = add(buffer, interval);
		}
		//cerr << "buffer: " << buffer << endl;
		//cerr << "last: " << seconds.front() << endl;

		string answer = subtract(buffer, seconds.front());
		while (answer[0] == '0')
		{
			answer.erase(answer.begin());
		}
		if (answer.empty())
		{
			answer = '0';
		}
		//cerr << "answer: " << answer << endl;

		cout << answer;

		cout << endl;
	}

	fin.close();

	return 0;
}
