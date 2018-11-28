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

void init()
{
	int t;
	cin >> t;
	for(int i=1; i<=t; ++i)
	{
		long long n,today,total;
		cin >> n >> today >> total;
	//	cerr << n << " " << today << " " << total << endl;
		
		bool possible = true;
		if ( (today != 0 && total == 0) || (today != 100 && total == 100) )
		{
			possible = false;
		}
		else
		{
		/*	int two = 0, five = 0, nToday = today;
			for(int k=1; k<=2 && (nToday%2) == 0; ++k)
			{
				nToday /= 2;
				++two;
			}
			
			for(int k=1; k<=2 && (nToday%5) == 0; ++k)
			{
				nToday /= 5;
				++five;
			}
			
			int res = 1;
			if (two != 2) res *= (2-two)*2;
			if (five != 2) res *= (2-five)*5;
			
			possible = (res <= n && (nToday*res)*100/today <= n); */
			
			//cerr << n << " " << res << endl;
			int g = __gcd(today, 100ll);
			possible = (100/g <= n);
		}
		
		printf("Case #%d: %s\n", i, possible ? "Possible":"Broken");
	}
}

void test()
{
   
}

int main()
{
  freopen ("/home/idainet/code/in.txt", "r", stdin);
  freopen ("/home/idainet/code/out.log", "w", stderr);
  freopen ("/home/idainet/code/out.txt", "w", stdout);

   
   //checktime();
   init();
   
   //test();
   
   fflush(stdout);
   return 0;
} 
