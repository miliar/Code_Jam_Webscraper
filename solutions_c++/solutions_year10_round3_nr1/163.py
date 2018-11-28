#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <list>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cmath>

// #define DEBUG

using namespace std;

/*************************************************/
// BEGIN UTILITY CODE
typedef unsigned char byte;
typedef long long int64;

const double E5 = .00001;
const double E9 = .000000001;

void _print(string& lead, string& str) {cout<<lead<<'\"'<<str<<'\"'<<endl;} 
void _print(const char* lead, string& str) {cout<<lead<<'\"'<<str<<'\"'<<endl;} 
template<class T> string toString(T x){ostringstream oss; oss<<x; return oss.str();}

bool _isUpperCase(char c){return 'A' <= c && c <= 'Z';}
bool _isLowerCase(char c){return 'a' <= c && c <= 'z';}
bool _isAlpha(char c){return _isUpperCase(c) || _isLowerCase(c);}
bool _isNum(char c){return '0' <= c && c <= '9';}

char _toLower(char c){if(_isUpperCase(c)) return c + 'a' - 'A'; else return c;}
void _toLower(string& s){for(int i = 0; i < s.size(); i++) s[i] = _toLower(s[i]);}
char _toUpper(char c){if(_isLowerCase(c)) return c + 'A' - 'a'; else return c;}
void _toUpper(string& s){for(int i = 0; i < s.size(); i++) s[i] = _toUpper(s[i]);}
void _flush(){if(cin.peek()=='\n') cin.ignore(1,'\n');}

template<class T> void _print(const vector<T>& v){for(int i = 0; i < v.size(); i++)cout<<i<<" "<<v[i]<<endl;}


// END UTILITY CODE
/*************************************************/
bool intersect(int a0, int b0, int a1, int b1)
{
	
	if(a1 > a0 && b1 < b0) return true;
	if(a1 < a0 && b1 > b0) return true;
	return false;
}

int main()
{
	int T;
	cin>>T;
	
	for(int i = 0; i < T; i++)
	{
		int N;
		cin>>N;
		vector< pair<int, int> > vec(N, make_pair(0,0));
		
		for(int j = 0; j < N; j++)
			cin>>vec[j].first>>vec[j].second;
	
		int result = 0;
		for(int x = 0; x < vec.size()-1; x++)
		for(int y = x+1; y < vec.size(); y++)
			if(intersect(vec[x].first, vec[x].second, vec[y].first, vec[y].second))
				result++;
		
					
		cout<<"Case #"<<i+1<<": "<<result<<endl;
	}

	return 0;
}
