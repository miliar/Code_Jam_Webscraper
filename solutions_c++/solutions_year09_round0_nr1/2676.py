#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define For(i,b) for(int i = 0; i < (int)b; ++i)
#define Fori(i,a,b) for(int i = a; i < (int)b; ++i)
#define Ford(i,a,b) for(int i = a; i >=b; --i)
#define All(t) t.begin(),t.end()
#define Sort(a) sort(All(a))
#define Fill(a,b) memset(a,b,sizeof(a))
#define Forstl(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)
#define db(x) cout << #x << " = " << x << endl
#define mod(A, B) ((((A) % (B)) + (B)) % (B))
#define Exist(container, element) (container.find(element) != container.end())
#define sz(a) int((a).size()) 
typedef long long ll;

template <class T>
void out(vector<T> v)
{
  cout << "{";
  For(_i,v.size()) {if(_i) cout<<","; cout<<v[_i];}
  cout<<"}"<<endl;
}

vector<string> split( const string& s, const string& delim =" " ) {
    vector<string> res;
    string t;
    for ( int i = 0 ; i != (int)s.size() ; i++ ) {
        if ( delim.find( s[i] ) != string::npos ) {
            if ( !t.empty() ) {
                res.push_back( t );
                t = "";
            }
        } else {
            t += s[i];
        }
    }
    if ( !t.empty() ) {
        res.push_back(t);
    }
    return res;
}

int charMask[50];

bool isMatch(string word, vector<int> v)
{
	int len = sz(word);
	assert(len == sz(v));
	For(i,len)
	{
		if((v[i] & charMask[word[i]-'a']) == 0)
		    return 0;
	}
	return 1;
}

inline int getMask(string s)
{
	int res = 0;
	For(i,sz(s))
	{
		res |= (1<<(s[i]-'a'));
	}
	return res;
}

int main ()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.txt");
	for(char c = 'a'; c<='z'; ++c)
	{
		charMask[c-'a'] = (1<<(c-'a'));
	}
	int L, D, N;
	fin >> L >> D >> N;
	vector<string> words(D);
	For(z,D)
	{
		fin >> words[z];
	}
	string test;
	For(t,N)
	{
		fin >> test;
		vector<int> pattern;
		bool open = 0;
		string cur;
		For(i,sz(test))
		{
			if(test[i] == '(')
			{
				open = 1;
				continue;
			}
			if(test[i] == ')')
			{
				assert(cur != "");
				pattern.push_back(getMask(cur));
				cur = "";
				open = 0;
				continue;
			}
			if(open)
			    cur += test[i];
			else
			{
				pattern.push_back(charMask[test[i]-'a']);
				cur = "";
			}
		}
		//out(pattern);
		int res  = 0;
		For(i,D)
		{
			if(isMatch(words[i],pattern))
			{
				//db(words[i]);
				//out(pattern);
				//cout << endl;
			    ++res;
			}
		}
		char buf[1024];
		sprintf(buf,"Case #%d: %d", t+1, res);
		string ans = buf;
		fout << ans << endl;
	}
	fout.close();
	db("Done");
	getchar();
	return 0;
}
