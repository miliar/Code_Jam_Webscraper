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
#define sqr(x) ((x)*(x))
typedef long long ll;

template <class T>
void out(vector<T> v)
{
  cout << "{";
  For(_i,v.size()) {if(_i) cout<<","; cout<<v[_i];}
  cout<<"}"<<endl;
}

string fromdec2(int n, int b)
{
  string res = "";
  string chars("0123456789ABCDEFGHIJ");
  while(n>0)
  {
    //res = res + chars[n%b];
    res = chars[n%b]+res;
    n/=b;
  }
  //reverse(res.begin(),res.end());
  return res;
}

string itos (int i) {stringstream s; s << i; return s.str();}

inline int f(string s)
{
    int cur = 0;
	For(i,sz(s))
	{
		cur += sqr(s[i]-'0');
	}
	return cur;
}

typedef pair<string,int> psi;
map<psi, bool> dp;

bool ok(string s, int b)
{
	psi state = psi(s,b);
	if(dp.count(state))
	    return dp[state];
	//if(b == 2 || b == 4) return 1;
	set<int> my;
	int cur = f(s);
	if(cur == 1) return dp[state] = 1;
	my.insert(cur);
	string t;
	while(1)
	{
		t = (b==10) ? itos(cur) : fromdec2(cur, b);
		//db(t);
		psi st = psi(t,b);
		if(dp.count(st))
		    return dp[state] = dp[st];
		cur = f(t);
		if(cur == 1) return dp[state] = 1;
		//db(cur);
		if(my.count(cur))
		    return dp[state] = 0;
		else
		    my.insert(cur);
		//db(cur);
		if(cur == 1) break;
	}
	return dp[state] = (cur == 1);
}

const int MAX = 12000000;
// SPLIT INTO VECTOR OF STRINGS
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

//SPLIT INTO VECTOR OF INTS
vector<int> splitInt( const string& s, const string& delim =" " ) {
    vector<string> tok = split( s, delim );
    vector<int> res;
    for ( int i = 0 ; i != (int)tok.size(); i++ )
        res.push_back( atoi( tok[i].c_str() ) );
    return res;
}

int stoi (string s) {istringstream in(s); int ret; in >> ret; return ret;}

int main ()
{
	ifstream fin("A-small.in");
	ofstream fout("A-small.out");
	string s;
	
	dp[psi("2",3)] = dp[psi("12",3)] = dp[psi("22",3)] = false;
	dp[psi("4",5)] = dp[psi("23",5)] = dp[psi("33",5)] = false;
	dp[psi("32",6)] = 0;
	dp[psi("2",7)] = dp[psi("34",7)] = dp[psi("13",7)] = dp[psi("23",7)] = dp[psi("63",7)] = dp[psi("44",7)] = 0;
	dp[psi("4",8)] = dp[psi("5",8)] = dp[psi("32",8)] = dp[psi("24",8)] = dp[psi("64",8)] = 0;
	dp[psi("55",9)] = dp[psi("58",9)] = dp[psi("45",9)] = dp[psi("75",9)] = 0;


	/*
	Fori(i,2,MAX)
	{
		bool found = 0;
		Fori(b,3,11)
		{
			if(b == 4) continue;
			s = (b==10) ? itos(i) : fromdec2(i, b);
			bool isok = ok(s, b);
			if(!isok)
			{
				found = 1;
				break;
			}
		}
		if(!found)
		{
			db(i);
		}
	}
	*/
	
	int T;
	string str;
	getline(fin, str);
	T = stoi(str);
	For(z,T)
	{
		getline(fin,str);
		vector<int> v = splitInt(str);
		int res = -1;
		Fori(i,2,MAX)
		{
			bool found = 0;
			Forstl(it,v)
			{
				int b = *it;
				if(b == 4 || b == 2) continue;
				s = (b==10) ? itos(i) : fromdec2(i, b);
				bool isok = ok(s, b);
				if(!isok)
				{
					found = 1;
					break;
				}
			}
			if(!found)
			{
				res = i;
				break;
			}
		}
		char buf[1024];
		sprintf(buf,"Case #%d: %d", z+1, res);
		string ans = buf;
		fout << ans << endl;
	}
	
	db("Done!");
	db("Done!");
	getchar();
	return 0;
}
