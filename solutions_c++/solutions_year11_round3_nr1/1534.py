#include <iostream>
#include <sstream>
#include <fstream>
#include <iterator>
#include <cstdlib>
#include <vector>
#include <list>
#include <algorithm>
#include <climits>
#include <string.h>

using namespace std;

template <class T>
void parseStr(ifstream& stream, vector<T>& intVector)
{
    string str;
    getline(stream, str);

    istringstream iss(str);
    copy(istream_iterator<T>(iss), istream_iterator<T>(), intVector.begin());
}

template <class T>
void debugV(T& intVector)
{
    for (typename T::const_iterator iter = intVector.begin(); iter != intVector.end(); ++iter)
    {
        cout << *iter << " ";
    }
    cout << endl;
}

template <class T>
void parseStr(ifstream& stream, T& value)
{
    string str;
    getline(stream, str);

    istringstream iss(str);
    iss >> value;
}

bool solve(int r, int c, vector<string>& arr)
{
	for (int i = 0; i < r - 1; ++i)
	{
		for (int j = 0; j < c - 1; ++j)
		{
			if (arr[i][j] == '#' && arr[i][j + 1] == '#' && arr[i + 1][j] == '#' && arr[i + 1][j + 1] == '#')
			{
				arr[i][j] = '/';
				arr[i][j + 1] = '\\';
				arr[i + 1][j] = '\\';
				arr[i + 1][j + 1] = '/';
			}
		}
	}
	
	for (int i = 0; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
		{
			if (arr[i][j] == '#')
				return false;
		}
	}
	return true;
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        cerr << "Input file missing" << endl;
        exit(-1);
    }
    ifstream input;
    input.open(argv[1]);
    if (!input.is_open())
    {
        cerr << "Cannot open file " << argv[1] << endl;
        exit(-2);
    }

    int testCases;
    parseStr(input, testCases);
    cerr << "Test cases " << testCases << " total" << endl;

    for (int i = 1; i <= testCases; ++i)
    {
		vector<int> rc;
		rc.resize(2);
		parseStr(input, rc);
		int r = rc[0];
		int c = rc[1];
		cerr << "Test case: " << i << "(" << r << "/" << c << ")" << endl;
		
		vector<string> arr;
		arr.resize(r);
		for (int j = 0; j < r; ++j)
		{
			getline(input, arr[j]);
		}

		bool found = solve(r, c, arr);
		
		cout << "Case #" << i << ":" << endl;
		if (!found)
			cout << "Impossible" << endl;
		else
		{
			for (int j = 0; j < r; ++j)
			{
				cout << arr[j] << endl;
			}
		}
    }
}

