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
typedef unsigned long long uint64;

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
void _flushw(){while(cin.peek()=='\n') cin.ignore(1,'\n');}

template<class T> inline T square(T t){return t*t;}

template<class T> void _print(const vector<T>& v){for(int i = 0; i < v.size(); i++)cout<<i<<" "<<v[i]<<endl;}

template<class T> void alloc2D(T** t, int X, int Y) {t=new T*[X]; for(int i=0;i<X;i++)t[i]=new T[Y];} 
template<class T> void free2D(T** t, int X, int Y) {for(int i=0;i<X;i++)delete [] t[i]; delete [] t;} 

#define LINE() cout<<"line : "<<__LINE__<<endl

// END UTILITY CODE
/*************************************************/

inline int sumPatrick(int A, int B)
{
	return A ^ B;
}

int main()
{
	int T;
	cin>>T;
	
	int data[1024];
	
	int sz = 2000001+1;
	vector< pair<int, int> > kp(sz);
	vector< pair<int, int> > newVals(sz);
		
	for(int t = 1; t <= T; t++)
	{
		int N;
		cin>>N;
		
		int sum = 0;
		int realSum = 0;
		for(int i = 0; i < N; i++)
		{
			cin>>data[i];
			sum = sumPatrick(sum, data[i]);
			realSum += data[i];
		}
		
		if(sum != 0)
		{
			cout<<"Case #"<<t<<": NO"<<endl;
			continue;
		}
		
		// knapsack
		fill(kp.begin(), kp.end(), make_pair(0,0));
		kp[0].first = 1;
		
		int maxID = 0;
		for(int i = 0; i < N; i++)
		{
			int numAdded = 0;
			// scan
			for(int j = 0; j <= maxID; j++)
			{
				if(kp[j].first != 0)
				{
					int newPatrickSum = sumPatrick(j, data[i]);
					int realSum = kp[j].second + data[i];
				
					if( kp[newPatrickSum].second < realSum)
					{			
						newVals[numAdded++] = make_pair(newPatrickSum, realSum);
					}
				}
			}
			
			for(int z = 0; z < numAdded; z++)
			{
				int id = newVals[z].first;
				int val = newVals[z].second;
		
				kp[id].first = 1;
				kp[id].second = max(kp[id].second, val);
				maxID = max(maxID, id);
			}
		}
		
		int best = -1;
		for(int j = sz-1; j > 0; j--)
		{
			best = max(best, kp[j].second);
		}
		
		cout<<"Case #"<<t<<": "<<best<<endl;
	}
	
	return 0;
}
