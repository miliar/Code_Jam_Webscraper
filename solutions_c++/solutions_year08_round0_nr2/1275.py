#include <iostream>
#include <cmath>
#include <vector>
#include <sstream>
#include <string>
#include <stdexcept>
#include <map>
#include <utility>
#include <algorithm>
#include <fstream>

using namespace std;

#define FOR(i, a, b) for (i = a; i < b; i++)
#define RFOR(i, a, b) for (i = a - 1; i >= b; i--)

class BadConversion : public std::runtime_error {
 public:
   BadConversion(const std::string& s)
     : std::runtime_error(s)
     { }
};
 
template <class T>
inline T convertToNumber(const std::string& s)
{
   std::istringstream i(s);
   T x;
   if (!(i >> x))
     throw BadConversion("convertToNumber(\"" + s + "\")");
   return x;
} 


void Tokenize(const string& str, vector<string> &tokens, const string &delimiters = " ")
{
    // Skip delimiters at beginning.
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // Find first "non-delimiter".
    string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        // Found a token, add it to the vector.
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        // Skip delimiters.  Note the "not_of"
        lastPos = str.find_first_not_of(delimiters, pos);
        // Find next "non-delimiter"
        pos = str.find_first_of(delimiters, lastPos);
    }
}

template <class T>
class Solution
{
	T t, NA, NB;
	vector <pair <T, T> > dA;
	vector <pair <T, T> > aA;
	vector <pair <T, T> > dB;
	vector <pair <T, T> > aB;

	T fromA;
	T fromB;

	public:
		Solution()
		{
			fromA = 0;
			fromB = 0;
		}

		void print();

		void solve();

		void setData(T t, T NA, T NB, vector <pair <T, T> > &dA, vector <pair <T, T> > &aA, vector <pair <T, T> > &dB, vector <pair <T, T> > &aB);

		T getA();
		T getB();

		int departs(vector <pair <T, T> > &d, int h, int m);
		int canGo(vector <pair <T, T> > &a, int h, int m);
};

template <class T>
void Solution<T>::print()
{
	int i;
	FOR (i, 0, (int)this->dA.size())
	{
		cout << this->dA[i].first << ":" << dA[i].second << " ";
	}
	cout << endl;
	FOR (i, 0, (int)this->aA.size())
	{
		cout << this->aA[i].first << ":" << aA[i].second << " ";
	}
	cout << endl;
	FOR (i, 0, (int)this->dB.size())
	{
		cout << this->dB[i].first << ":" << dB[i].second << " ";
	}
	cout << endl;
	FOR (i, 0, (int)this->aB.size())
	{
		cout << this->aB[i].first << ":" << aB[i].second << " ";
	}
	cout << endl;
}

template <class T>
void Solution<T>::setData(T t, T NA, T NB, vector <pair <T, T> > &dA, vector <pair <T, T> > &aA, vector <pair <T, T> > &dB, vector <pair <T, T> > &aB)
{
	this->t = t;
	this->NA = NA;
	this->NB = NB;

	this->dA = dA;
	this->aA = aA;
	this->dB = dB;
	this->aB = aB;
}

template <class T>
void Solution<T>::solve()
{
	T inA = 0;
	T inB = 0;

	int i, j;

	T d;
	T f;

	FOR(i, 0, 24)
	{
		FOR(j, 0, 60)
		{
			f = canGo(aA, i, j);

			while (f > 0)
			{
				inA++;
				f--;
			}

			f = canGo(aB, i, j);

			while (f > 0)
			{
				inB++;
				f--;
			}

			d = departs(dA, i, j);
			while (inA > 0 && d > 0)
			{
				inA--;
				d--;
			}

			while (d > 0)
			{
				fromA++;
				d--;
			}

			d = departs(dB, i, j);
			while (inB > 0 && d > 0)
			{
				inB--;
				d--;
			}
			while (d > 0)
			{
				fromB++;
				d--;
			}

		}
	}
}

template <class T>
int Solution<T>::departs(vector <pair <T, T> > &d, int h, int m)
{
	int i;
	int cnt = 0;

	FOR(i, 0, (int)d.size())
	{
		if (d[i].first == h && d[i].second == m)
		{
			cnt++;
		}
	}

	return cnt;
}

template <class T>
int Solution<T>::canGo(vector <pair <T, T> > &a, int h, int m)
{
	int cnt = 0;
	int i;

	T hh;
	T mm;

	FOR(i, 0, (int)a.size())
	{
		mm = a[i].second + t;
		if (mm > 59)
		{
			mm = mm - 60;
			hh = a[i].first + 1;
		}
		else
		{
			hh = a[i].first;
		}

		if (hh == h && mm == m)
		{
			cnt++;
		}
	}

	return cnt;
}

template <class T>
T Solution<T>::getA()
{
	return fromA;
}

template <class T>
T Solution<T>::getB()
{
	return fromB;
}

int main()
{
	ifstream f_in;
    ofstream f_out;
	int n;
	int T, NA, NB;
	vector <int> data;
	vector <string> tokens;
	vector <string> timeToks;
	string line;

	int h, m;

	int i, j;

	vector <pair <int, int> > dA;
	vector <pair <int, int> > aA;
	vector <pair <int, int> > dB;
	vector <pair <int, int> > aB;

	//f_in.open("sample_in.in", ios::in);
	//f_in.open("B-small-attempt0.in", ios::in);
	f_in.open("B-large.in", ios::in);
	f_out.open("out.out", ios::out);

	f_in >> n;

	getline (f_in, line);

	FOR(i, 0, n)
	{
		dA.resize(0);
		dB.resize(0);
		aA.resize(0);
		aB.resize(0);

		f_in >> T;
		f_in >> NA;
		f_in >> NB;

		getline (f_in, line);

		FOR(j, 0, NA)
		{
			tokens.resize(0);
			getline (f_in, line);
			Tokenize(line, tokens);
			timeToks.resize(0);
			Tokenize(tokens[0], timeToks, ":");
			h = convertToNumber<int>(timeToks[0]);
			m = convertToNumber<int>(timeToks[1]);

			dA.push_back(make_pair(h, m));

			timeToks.resize(0);
			Tokenize(tokens[1], timeToks, ":");
			h = convertToNumber<int>(timeToks[0]);
			m = convertToNumber<int>(timeToks[1]);

			aB.push_back(make_pair(h, m));

		}

		FOR(j, 0, NB)
		{
			tokens.resize(0);
			getline (f_in, line);
			Tokenize(line, tokens);
			timeToks.resize(0);
			Tokenize(tokens[0], timeToks, ":");
			h = convertToNumber<int>(timeToks[0]);
			m = convertToNumber<int>(timeToks[1]);

			dB.push_back(make_pair(h, m));

			timeToks.resize(0);
			Tokenize(tokens[1], timeToks, ":");
			h = convertToNumber<int>(timeToks[0]);
			m = convertToNumber<int>(timeToks[1]);
			
			aA.push_back(make_pair(h, m));
		}

		Solution <int> * C;

		C = new Solution <int>;

		C->setData(T, NA, NB, dA, aA, dB, aB);

		C->print();

		C->solve();

		cout << "Case #" << i + 1 << ": " << C->getA() << " " << C->getB() << endl;

		f_out << "Case #" << i + 1 << ": " << C->getA() << " " << C->getB() << endl;
	}

	f_out.close();
	f_in.close();

	system("pause");
	return 0;
}
