# include <iostream>
# include <cstdio>
# include <cstdlib>
# include <vector>
# include <string>
# include <cmath>
# include <algorithm>
# include <iomanip>
# include <deque>
# include <queue>
# include <stack>
# include <numeric>
# include <ios>
# include <set>
# include <map>
# include <sstream>
# include <iterator>
# include <limits>
# include <cstring>
# include <string.h>
# include <list>
# include <bitset>
# include <climits>
# include <cassert>

# define INF numeric_limits<long double>::infinity()
# define Fi 1.6180339887
# define eps 1e-6
# define quadro __float128
# define abc() printf("\nUnexpected in \"%s\" at line %d\n", __func__, __LINE__)

# define startt clock_t start,end; start = clock()
# define endt end = clock(); printf("\nFunction \"%s\" executed in %.2f seconds\n", __func__, (float)(end-start)/CLOCKS_PER_SEC)
# define checktime() startt; init(); endt

using namespace std;

template <typename T> void read(T& val) { cin >> val; }
template <typename T> void read(vector<T>& vec) { for(int i=0; i<vec.size(); ++i) { read(vec[i]); } }
template <typename T> void readSafe(T& val) { cin >> val; }
template <typename T> void readSafe(vector<T>& vec) { for(int i=1; i+1<vec.size(); ++i) { readSafe(vec[i]); } }
template <typename T> void print(const T& val) { cout << val << " " ; }
template <typename T> void print(const vector<T>& vec) { for(int i=0; i<vec.size(); ++i) { print(vec[i]); } cout << endl; }
template <typename T> string toString(const T& val) { ostringstream ostr; ostr << val; return ostr.str(); }
inline long double fromString(const string& str) { long double res; istringstream(str) >> res; return res; }
inline bool isDigit(const char& ch) { return (ch >= '0' && ch <='9'); }
inline bool isAlpha(const char& ch) { return (ch >= 'a' && ch <='z' || ch >='A' && ch <= 'Z'); }
inline string trimString(string& str){ while(*str.begin()==' ') { str.erase(str.begin()); } while(*str.rbegin()==' ') {str.erase(str.end()-1); } return str;}
inline void skip() { while (cin.peek() == ' ' || cin.peek() == '\n' || cin.peek() == '\r' || cin.peek() == '\t') cin.get(); }

template <typename T> class Point {
public:
	T x, y, z, pos; 
	Point<T> (const T& a,const T& b, const T& c) { x=a; y=b; z=c; } 
	Point<T> (const T& a,const T& b) { x=a; y=b; } 
	Point<T>() { Point<T>(0,0); }
	
	bool operator<(const Point<T>& b) const { return (y > b.y); }
};

typedef struct _s
{
	char who;
	int which;
} Task;

void magik()
{
	int n;
	cin >> n;
	vector<Task> general;
	vector<int> orange, blue;
	for(int i=0; i<n; ++i)
	{
		Task tmp;
		cin >> tmp.who;
		scanf("%d", &tmp.which);
		general.push_back(tmp);
		//cout << "! " << tmp.who << " " << tmp.which << endl;
		
		if (tmp.who == 'O')
		{
			orange.push_back(tmp.which);
		}
		else if (tmp.who == 'B') 
		{
			blue.push_back(tmp.which);
		}
		else abc();
	}
	
	int orangeRoll = (orange.empty() ? -1:0),orangePos = 1, blueRoll = (blue.empty() ? -1:0), bluePos = 1;
	unsigned long long orangeTime = 0, blueTime = 0;
	int genRoll = 0;
	
	while( genRoll != general.size() )
	{
		if (general[genRoll].who == 'O')
		{
			if (orangePos == general[genRoll].which)
			{
				++orangeTime;
				orangeRoll = (orangeRoll+1 == orange.size() ? -1:(orangeRoll+1) );
				++genRoll;
			}
			else
			{
				orangeTime += abs( orange[orangeRoll] - orangePos );
				orangePos = orange[orangeRoll];
			}
			
			if (blueRoll != -1)
			{
				blueTime += abs( blue[blueRoll] - bluePos);
				bluePos = blue[blueRoll];
			}
			
			blueTime = max(blueTime, orangeTime);
		}
		else if (general[genRoll].who == 'B')
		{
			if (bluePos == general[genRoll].which)
			{
				++blueTime;
				blueRoll = (blueRoll +1 == blue.size() ? -1:(blueRoll+1) );
				++genRoll;
			}
			else
			{
				blueTime += abs( blue[blueRoll] - bluePos);
				bluePos = blue[blueRoll];
			}
			
			if (orangeRoll != -1)
			{
				orangeTime += abs( orange[orangeRoll] - orangePos );
				orangePos = orange[orangeRoll];
			}
			
			orangeTime = max(orangeTime, blueTime);
		}
	}
	
	cout << max(blueTime, orangeTime) << endl;
}

void init()
{
	int n;
	cin >> n;
	for(int i=1; i<=n; ++i)
	{
		printf("Case #%d: ", i);
		magik();
	}
}

void test()
{
    
}

int main()
{
  freopen ("/home/idainet/code/in.txt", "r", stdin);
  freopen ("/home/idainet/code/out.txt", "w", stdout);

   
   //checktime();
   init();
   
   //test();
   
   fflush(stdout);
   return 0;
} 
