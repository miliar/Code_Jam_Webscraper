#include <iostream>
#include <sstream>
#include <fstream>
#include <iterator>
#include <cstdlib>
#include <vector>
#include <list>
#include <algorithm>
#include <climits>

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

inline bool test(unsigned long lhs, unsigned long rhs)
{
	return (lhs > rhs ?
	       (lhs % rhs == 0) :
		   (rhs % lhs == 0) );
}

inline unsigned long gcd(unsigned long lhs, unsigned long rhs)
{
	if (lhs > rhs)
	{
		unsigned long tmp = rhs;
		rhs = lhs;
		lhs = tmp;
	}
	
	unsigned long t;
	while (rhs != 0)
	{
		t = rhs;
		rhs = lhs % rhs;
		lhs = t;
	}
	return lhs;
}

unsigned long solve(int n, unsigned long low, unsigned long high,
                    vector<unsigned long> freqs)
{
	if (low < 1 && high > 1)
		return 1;
	
	bool skip = false;
	for (unsigned long freq = low; freq <= high; ++freq)
	{
		skip = false;
		for (vector<unsigned long>::const_iterator freqsIter = freqs.begin();
		     freqsIter != freqs.end(); ++freqsIter)
		{
			if (!test(freq, *freqsIter))
			{
				skip = true;
				break;
			}
		}
		if (skip)
			continue;
		else
			return freq;
	}
	return 0;
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
		cerr << "Test cases: " << i << endl;
        vector<unsigned long> nlh;
		nlh.resize(3);
		parseStr(input, nlh);
		vector<unsigned long> freqs;
		freqs.resize(nlh[0]);
		parseStr(input, freqs);

		unsigned long freq = solve(nlh[0], nlh[1], nlh[2], freqs);
		if (freq != 0)
			cout << "Case #" << i << ": " << freq << endl;
		else
			cout << "Case #" << i << ": NO" << endl;
    }
}

