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

typedef map<string, bool> stringmap;
stringmap features;
const char* eat_space( const char* s )
{
	while( isspace(*s) ) 
		s++;
	return s;
}
const char* get_token( const char* s, string & token )
{
	token.clear();

	s = eat_space( s );

	while( *s && !isspace(*s) ) 
	{
		token += *s;
		s++;
	}

	s = eat_space( s );

	return s;
}
const char* get_double( const char* s, double & val )
{
	string token;
	const char* ret = get_token( s, token );

	istringstream is( s );
	is >> val;

	return ret;
}

const char* parse( const char* s, double & value )
{
	string token;
	s = eat_space( s );

	// cout << "s: [" << s << "]" << endl;
	bool parentesi = false;
	if (*s == '(')
	{
		parentesi = true;
		++s;
	}
	{
		s = eat_space( s );

		double weight;
		s = get_double( s, weight );
		// cout << "weight: " << weight << endl;

		s = eat_space( s );

		if (*s == ')')
		{
			value = weight;
			// cout << "Leaf: " << weight << endl;
			s = eat_space( s+1 );
			return s;
		}
		
		string f;
		s = get_token( s, f );

		double yes, no;
		s = parse( s, yes );
		s = parse( s, no );

		if (features.find(f)!=features.end())
		{
			// cout << "Has " << f << endl;
			value = weight * yes;
		}
		else
		{
			// cout << "Misses " << f << endl;
			value = weight  * no;
		}

		if(parentesi)
			s = get_token( s, token );

			s = eat_space(s);
		// cout << "endtoken: " << token << endl;
	}
	return s;
}

int main()
{
	int C;
	string dummy;
	
	cin >> C;

	FOR(c,0,C)
	{
		long result = 0;
		int L;
		cin >> L;
		getline( cin, dummy );
		string text ;
		// cout << "L:" << L << endl;
		FOR(l,0,L)
		{
			string line;
			getline( cin, line );
			// replace_if(line.begin(), line.end(), std::bind2nd(std::equal_to<char>(),')'), ' ');
			// replace_if(line.begin(), line.end(), std::bind2nd(std::equal_to<char>(),'('), ' ');
			text += " ";
			text += line;
		}
		// cout << "Text: [" << text << "]" << endl;

		string text0 = text;
		text.clear();
		FOR(t,0,text0.size())
		{
			char x = text0[t];
			switch (x)
			{
				case ')':
				case '(':
				 text+=" ";
				 text+=x;
				 text+=" ";
				 break;
				 default:
				 text+=x;
			}
		}

		cout << "Case #" << c+1 <<": " << endl;

		int T;
		cin >> T;
		FOR(t,0,T)
		{
			string animal;
			features.clear();
			int F;
			cin >> animal >> F;
			// cout << "Animal: " << animal << " feats: " << F << endl;
			FOR(f,0,F)
			{
				string feature;
				cin >> feature;
				// cout << "F: " << feature << endl;
				features[feature] = true;
			}
			double p = 1.0;
			parse( text.c_str(), p );
			cout.precision( 7 );
			cout << fixed << p << endl;

			string line;
			getline( cin, line );
		}

	}

	return 0;
}
