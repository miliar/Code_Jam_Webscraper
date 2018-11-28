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
	for(int q=1; q<=t; ++q)
	{
		int n;
		cin >> n;
		vector<vector<int> > base(n, vector<int>(n));
		for(int i=0; i<n; ++i)
		{
			for(int k=0; k<n; ++k)
			{
				static char next;
				cin >> next;
				base[i][k] = (next == '.' ? -1:(next-'0') );
			}
		}
//		print(vec); cout << "!!" << endl;
		
		vector<double> ow(n);
		vector<int> played(n, 0);
		for(int i=0; i<n; ++i)
		{
			int win=0;
			for(int k=0; k<n; ++k)
			{
				if (base[i][k] != -1)
				{
					++played[i];
					win += (base[i][k] == 1);
				}
			}
			ow[i] = (double)win/played[i];
		}
		
		vector<double> owp(n);
		for(int i=0; i<n; ++i)
		{
			double tmp = 0;
			for(int k=0; k<n; ++k)
			{
				if (base[i][k] != -1) 
				{
					tmp += (ow[k]*played[k]-base[k][i])/(played[k]-1);
					//cout << i <<  << " " << k << " tmp " << tmp << endl;
				}
			}
			owp[i] = tmp/played[i];
		}
		
		vector<double>oowp(n);
		for(int i=0; i<n; ++i)
		{
			double tmp = 0;
			for(int k=0; k<n; ++k)
			{
				if (base[i][k] != -1) tmp += owp[k];
			}
			oowp[i] = tmp/played[i];
		}
		
/*		print(ow); cout << endl;
		print(owp); cout << endl;
		print(oowp); cout << endl;
*/		
		printf("Case #%d:\n", q);
		for(int i=0; i<n; ++i)
		{
			double res = ow[i]*0.25 + owp[i]*0.50 + oowp[i]*0.25;
			cout << fixed << setprecision(12) << res << endl;
		}
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
