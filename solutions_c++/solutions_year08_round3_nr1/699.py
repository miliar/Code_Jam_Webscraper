
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

// separator assumend : whitespace
template<class A>
void parseInputLine(istream &in, A &a)
{
	string line;
	getline(in, line);
	istringstream ss(line);
	ss >> a;
}

// separator assumend : whitespace
template<class A, class B>
void parseInputLine(istream &in, A &a, B &b)
{
	string line;
	getline(in, line);
	istringstream ss(line);
	ss >> a >> b;
}

// separator assumend : whitespace
template<class A, class B, class C>
void parseInputLine(istream &in, A &a, B &b, C &c)
{
	string line;
	getline(in, line);
	istringstream ss(line);
	ss >> a >> b >> c;
}

// separator assumend : whitespace
template<class A>
void parseInputLine(istream &in, vector<A> &a)
{
	string line;
	getline(in, line);
	istringstream ss(line);

	A tmp;
	while( ss >> tmp )
	{
		a.push_back(tmp);
	}
}

struct LetterFreq
{
	int letter;
	int freq;

	bool operator<(const LetterFreq &lf)
	{
		return this->freq < lf.freq;
	}
	bool operator==(const LetterFreq &lf)
	{
		return this->freq == lf.freq;
	}
};

int doit(int p, int k, int l, vector<int> freq)
{
	int *keys = new int[k];
	int *alph = new int[l];
	memset(keys, 0, sizeof(int)*k);
	memset(alph, 0, sizeof(int)*l);

	vector<LetterFreq> vlf;

	for(int i=0; i<freq.size(); i++)
	{
		LetterFreq lf;
		lf.freq = freq[i];
		lf.letter = i;
		vlf.push_back(lf);
	}

	sort(vlf.begin(), vlf.end());

	int curkey=0;
	for(int i=vlf.size()-1; i>=0; i--)
	{
		if(keys[curkey] == p)
		{
			delete[] keys;
			delete[] alph;
			return -1;
		}
		else
		{
			keys[curkey]++;
			alph[vlf[i].letter] = keys[curkey];
			curkey++;
			curkey = curkey % k;
		}
	}

	int count=0;
	for(int i=0; i<freq.size(); i++)
	{
		count += alph[i] * freq[i];
	}


	delete[] keys;
	delete[] alph;
	return count;
}

int main(int argc, char *argv[])
{
	int n;
	string line;
	ifstream in("C:/Documents and Settings/Yada Kishore/Desktop/A-small-attempt0.in");
	ofstream out("C:/Documents and Settings/Yada Kishore/Desktop/output.txt");
	parseInputLine(in, n);

	for(int i=0; i<n; i++)
	{
		int p, k, l;
		parseInputLine(in, p, k, l);
		vector<int> freq;
		parseInputLine(in, freq);

		int result = doit(p,k,l,freq);

		//copy(freq.begin(), freq.end(), ostream_iterator<int>(cout, " " ));
		//cout << endl;

		if(result == -1)
		{
		out << "Case #" << (i+1) << "**************************************" << result << endl;
		cout << "Case #" << (i+1) << ": " << result << endl;
		}
		else
		{
		out << "Case #" << (i+1) << ": " << result << endl;
		cout << "Case #" << (i+1) << ": " << result << endl;
		}
	}

	return 0;
}
