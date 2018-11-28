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

int main()
{
	int T;
	cin>>T;
	
	pair<int,int> instrA[120];
	pair<int,int> instrB[120];

	for(int t = 1; t <= T; t++)
	{
		int cntA = 0;		
		int cntB = 0;
	
		// input read
		int cnt;
		cin>>cnt;
		char x; int y;
		for(int i = 0; i < cnt; i++)
		{
			cin>>x>>y;
			
			if(x == 'O')
				instrA[cntA++] = make_pair(y,i);
			else
				instrB[cntB++] = make_pair(y,i);
		}

		int iA = 0;
		int iB = 0;
			
		// position
		int posA = 1;
		int posB = 1;
		
		int time = 0;
		int buttonCnt = 0;
		while(iA != cntA || iB != cntB)
		{
			time++;
			
			bool buttonA = false;
			bool buttonB = false;
			
			bool doneA = (iA == cntA);
			bool doneB = (iB == cntB);
			if(!doneA && posA == instrA[iA].first && buttonCnt == instrA[iA].second)
				buttonA = true;
			
			if(!doneB && posB == instrB[iB].first && buttonCnt == instrB[iB].second)
				buttonB = true;
				
			if(buttonA || buttonB)
				buttonCnt++;
				
			// decide what to do
			if(iA != cntA)
				if(buttonA)
				{
					iA++;
				}
				else
				{
					// move
					int dir = instrA[iA].first - posA;
					if(dir > 0) posA++;
					else if(dir < 0) posA--;
				}
				
			if(iB != cntB)
				if(buttonB)
				{
					iB++;
				}
				else
				{
					// move
					int dir = instrB[iB].first - posB;
					if(dir > 0) posB++;
					else if(dir < 0) posB--;
				}		
		}
	
	
		cout<<"Case #"<<t<<": "<<time<<endl;
	}
	
	return 0;
}
