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

const double E6 = .000001;
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

int main() 
{
	int T, N, K;
	cin>>T;
	
	for(int i = 0; i < T; i++)
	{
		cin>>N>>K;
	
		
		int power_of_two = 1 << N;
		//cout<<"\n\t"<<power_of_two<<endl;
		cout<<"Case #"<<i+1<<": ";
		if(K % power_of_two == power_of_two-1)
			cout<<"ON"<<endl;
		else
			cout<<"OFF"<<endl;
	}
	
	return 0;
}
