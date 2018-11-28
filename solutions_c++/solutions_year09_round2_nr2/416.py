/*{{{ boring stuff*/
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <algorithm>
#include <assert.h>
#include <sstream>
#include <memory.h>
using namespace std;

template<class T>/*{{{ assert_equal MACRO */
void check_equal(T a, T b, const char* LABEL1, const char* LABEL2, int line)
{
	if (a!=b)
	{
		cout << "ASSERTION FAILED: " << line << " " << LABEL1 << " == " << LABEL2 << " , values are (" << a << "," << b << ")" << endl;
		exit(1);
	}
}
#define assert_equal(A,B) \
	check_equal( A, B, #A, #B, __LINE__ )
/*}}}*/
#define FOR(VAR,FROM,TO) for(int VAR = FROM; VAR < TO; VAR++)
#define ZERO(X) memset(&X,0,sizeof(X))
bool dispari(int x) { return x & 1; }
bool pari(int x) { return !dispari(x); }
class node/*{{{*/
{
	public:
	int i,j;
	node(int _i,int _j)
	{
		i = _i;
		j = _j;
	}
	node(int v)
	{
		i = v / 100;
		j = v % 100;
	}
	operator int() { return i * 100 + j; }

	string to_string() const
	{
		ostringstream os;
		os << "(" << i << "," << j << ")";
		return os.str();
	}
};/*}}}*/
/*}}}*/

int main()
{
	int C;
	
	cin >> C;

	FOR(c,0,C)
	{
		string s;
		map<char,int> mdigits;
		cin >> s;
		// cout << "S=[" << s << "]" << endl;

		FOR(i,0,s.size())
			mdigits[s[i]] = 1;

		mdigits['0']= 1;

		vector<char> digits;
		
		for( map<char,int>::iterator it=mdigits.begin();it!=mdigits.end();++it)
		{
			it->second = digits.size();
			digits.push_back(it->first);
		}

		int base = digits.size() ;

		// cout << "Base is: " << base << endl;

		string result;
		s = "0" + s;
		for(int i = s.size() - 2; i>=0;i--)
		{
			string substring(s.c_str() + i);
			if (next_permutation( substring.begin(), substring.end() ))
			{
				result = s;
				result.resize(i);
				result += substring;
				break;
			}
		}

		if (result[0]=='0')
			result=result.c_str() + 1;
		cout << "Case #" << c+1 <<": " <<result << endl;
	}

	return 0;
}
