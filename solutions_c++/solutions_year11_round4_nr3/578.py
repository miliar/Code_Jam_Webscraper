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
# define eps 1e-5
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
inline void remark(const int& n) { cerr << "Case #" << n << ":" << endl << flush; }

template <typename T> class Point {
public:
	T x, y, z, pos; 
	Point<T> (const T& a,const T& b, const T& c) { x=a; y=b; z=c; } 
	Point<T> (const T& a,const T& b) { x=a; y=b; } 
	Point<T>() { Point<T>(0,0); }
	
	bool operator<(const Point<T>& b) const { return (y < b.y); }
};

bool isPrime(vector<int>& vec, int val)
{
	double root = sqrt(val*1.);
	for(int i=0; i<vec.size() && vec[i] <= root; ++i)
	{
		if (val%vec[i] == 0) return false;
	}
	
	return true;
}

void generate(vector<int>& vec, const int& end)
{
	for(int i=6; i<=end; i += 6)
	{
		if (isPrime(vec, i-1)) vec.push_back(i-1);
		if (isPrime(vec, i+1)) vec.push_back(i+1);
	}
}

void init()
{
	vector<int> primes = {2,3};
	generate(primes, 1e6 + 500);
	set<unsigned long long> pows;
	for(int i=0; i<primes.size(); ++i)
	{
		unsigned long long cur = primes[i]*primes[i];
		while(cur <= 1e13)
		{
			pows.insert(cur);
			cur *= primes[i];
		}
	}
	
	int T;
	cin >> T;
	for(int i=1; i<=T; ++i)
	{
		long long fr; cin >> fr;
		long long ans = 1;
		if (fr == 1) ans = 0;
		else
		{
			for(auto it = pows.begin(); it != pows.end() && *it <= fr; ++it) { ++ans; }
		}
		
		cout << "Case #" << i << ": " << ans << endl;
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
