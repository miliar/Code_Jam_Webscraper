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
	vector <T> E;
	vector <T> Q;
	int En;
	int Qn;
	int res;
	public:
		Solution()
		{
			this->res = 0;
		}

		void print();

		void solve();

		void setData(int En, int Qn, vector <T> &E, vector <T> &Q);

		int calculate(int curQ, int ch, int curE);

		int getResult();

		void del(vector <T> &cur, string s);
};

template <class T>
void Solution<T>::print()
{
	int i;
	FOR (i, 0, (int)this->E.size())
	{
		cout << this->E[i] << " ";
		
	}
	cout << endl;
	FOR (i, 0, (int)this->Q.size())
	{
		cout << this->Q[i] << " ";
		
	}
	cout << endl;
}

template <class T>
void Solution<T>::setData(int En, int Qn, vector <T> &E, vector <T> &Q)
{
	this->E = E;
	this->Q = Q;
	this->En = En;
	this->Qn = Qn;
}
/*
template <class T>
void Solution<T>::solve()
{
	int ch = 0;
	int i, j;
	vector <int> changes;
	int min = 0;

	if (Qn > 0)
	{

		FOR(i, 0, En)
		{
			if (E[i] != Q[0])
			{
				changes.push_back(calculate(1, ch, i));
			}
		}

		min = *min_element(changes.begin(), changes.end());

		res = min;
	}
}
*/

template <class T>
void Solution<T>::solve()
{
	int ch = 0;
	int i;
	vector <T> changes;
	int min = 0;

	i = 0;

	vector <T> cur;

	if (Qn > 0)
	{
		cur = E;
		/*
		cur.resize(E.size());
		FOR(j, 0, (int)E.size())
		{
			cur[j] = E[j];
		}
		*/

		del(cur, Q[0]);
		i++;

		while (i < Qn)
		{
			del(cur, Q[i]);
			if (cur.size() == 0)
			{
				ch++;
				cur = E;
				del(cur, Q[i]);
			}
			i++;
		}

		res = ch;
	}
}

template <class T>
void Solution<T>::del(vector <T> &cur, string s)
{
	int i;
	FOR(i, 0, (int)cur.size())
	{
		if (cur[i] == s)
		{
			cur[i] = cur[cur.size() - 1];
			cur.pop_back();
		}
	}
}

template <class T>
int Solution<T>::calculate(int curQ, int ch, int curE)
{
	int i = curQ;
	int j;

	int min;
	vector <int> changes;

	while (i < Qn && Q[i] != E[curE])
	{
		i++;
	}

	if (i < Qn)
	{
		ch++;

		FOR(j, 0, En)
		{
			if (E[j] != Q[i])
			{
				changes.push_back(calculate(i, ch, j));
			}
		}

		min = *min_element(changes.begin(), changes.end());

		return min;

	}
	else
	{
		return ch;
	}
}

template <class T>
int Solution<T>::getResult()
{
	return res;
}

int main()
{
	ifstream f_in;
    ofstream f_out;
	int n;
	vector <string> tokens;
	string line;

	int i, j;

	//f_in.open("sample_in.in", ios::in);
	//f_in.open("A-small-attempt1.in", ios::in);
	f_in.open("A-large.in", ios::in);
	f_out.open("out.out", ios::out);

	f_in >> n;

	getline (f_in, line);

	FOR(i, 0, n)
	{
		int En;
		vector <string> E;
		int Qn;
		vector <string> Q;

		f_in >> En;
		getline (f_in, line);
		E.resize(En);

		FOR(j, 0, En)
		{
			getline (f_in, line);
			E[j] = line;
		}

		f_in >> Qn;
		getline (f_in, line);
		Q.resize(Qn);

		FOR(j, 0, Qn)
		{
			getline (f_in, line);
			Q[j] = line;
		}

		Solution <string> * C;

		C = new Solution <string>;

		C->setData(En, Qn, E, Q);

		C->print();

		C->solve();

		cout << "Case #" << i + 1 << ": " << C->getResult() << endl;

		f_out << "Case #" << i + 1 << ": " << C->getResult() << endl;
	}

	f_out.close();
	f_in.close();

	system("pause");
	return 0;
}
