#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

vector <long> A;
vector <long> B;
map< string, int > alldirs;
//vector<long long>	inpt;
long long p,q;

typedef vector<int>		dvi;
typedef long long		dll;
typedef istringstream	dios;

// always pass a value (rather than someVecOrString.size()) to these macros. 
// that way optimizer can perform a better job.
#define dsz(i,v)	(i) = (v).size()
#define dsl(i,v)	(i) = (v).length()

#define dfor(i,b,e)	for(int i = (b); i < (e);  i++)
#define drof(i,b,e)	for(int i = (b); i >= (e); i--)
#define dfo(i,n)	for(int i = 0;   i < (n);  i++)
#define dof(i,n)	for(int i = (n)-1; i >= 0;   i--)
#define dfo1(i,n)	for(int i = 1;   i <= (n);  i++)
#define dof1(i,n)	for(int i = (n); i >= 1;   i--)

#define dall(c) c.begin(), c.end()
#define dpb push_back

map<long long, int> bitnum;
void initbitnum()
{
	int j = 0;
	for(long long i = 1; i > 0; i<<=1LL)
		bitnum[i] = j++;

	map<long long, int>::const_iterator iter;
}

int lowestbit(long long N)
{
	if( (N < 0) ||(N&0x01LL) )	// half the numbers are gonna be odd on average
		return 0;				// so we improve responsiveness here						

	if(bitnum[N])
		return bitnum[N];

	int rv = bitnum[ (( ( N^(N-1LL) )>>1LL )+1LL) ];
	return rv;
}

void display_output(long long rv)
{
	printf("%04d\n", rv);
}

// return a+b
inline int AddTwoIntegers( int a, int b )
{
    int result;

	/*
    __asm
    {
        mov eax, a  // inlined assembler can deal with simple local variable references
        add eax, b
        mov result, eax
    }
	*/
	result = a+b;
    return result;
}

vector <long long> primes;
inline vector<long long>&   gimmefactors(long long N, vector<long long>&factors)
{
	unsigned long numprimes = primes.size();
	long long lim = (long long)((long double)sqrt((long double)N)) + 1;
	for(unsigned long i = 0; i < numprimes && primes[i] < lim; i++)
	{
		if(N%primes[i] == 0)
			factors.push_back(primes[i]);
	}
	return factors;
}

inline vector<int> &rdigits(unsigned long long N, vector<int> &rd)
{
	unsigned long long tmp = N;
	while(tmp)
	{
		rd.push_back(tmp%10);
	}
	if(0 == N)
		rd.push_back(0);
	return rd;
}

#define intToVector digits
inline vector<int> &digits(unsigned long long N, vector<int> &d)
{
	rdigits(N, d);
	reverse(d.begin(), d.end());
	return d;
}


inline unsigned int onbits(unsigned long long N)
{
	unsigned long long tmp = N; 
	int rv = 0;
	while(tmp)
		rv++,(tmp&=(tmp-1));
	return rv;
}

inline long long gcd(long long a, long long b)
{
	long long rv = a;
	while(b!=0 && a!=0)	// until one was able to divide another...or if any was 0 to begin with :)
	{	
		rv = a;
		a %= b;		// a%=b
		b %= rv;	// b%=a
	}
	if(b)
		rv = b;
	return rv;
}

inline long long lcm(long long a, long long b)
{ // assumption...a!=0 and b!=0
	return (a/gcd(a,b))*b;
}

inline long long nCr(long long n, long long r)
{
   long long ncr = n;
   long long k = 1;
   long long n_r = n-r;

   // Handle special cases
   if (n_r < 0) { return 0;}	// Invalid value
   if (n_r < r) { r = n_r;}		// nCr = nC(n-r)
   if (r == 0) { return 1;}		// nC0 = 1

   // To avoid integer overflow, divide as early as possible
   //          n!
   // nCr =  _______
   //         r! (n-r)!
   // for expanding, let us make the assumption that n-r >= r
   // so, NUMERATOR   =  n*(n-1)*(n-2)...*(n-(r+1)) // basically we have ignored the terms that r gonna get cancelled
   //     DENOMINATOR =  1*2*...r
   while (++k <= r) // can do this coz, numerator as well as denominator will have r terms//coz (n-r) terms cancelled out
   {				// we loop only r-1 times coz the operation (* or /) is performed only r-1 times
     ncr *= --n;	// although the number of terms is r
     ncr /= k;
   }

   return ncr;
} 

inline long long nPr(long long n, long long r)
{
   long long npr = n;
   long long k = 1;
   long long n_r = n-r;

   // Handle special cases
   if (n_r < 0) { return 0;}	// Invalid value
   if (n_r < r) { r = n_r;}		// nCr = nC(n-r)
   if (r == 0) { return 1;}		// nP0 = (0!)*nC0 == 1*1 == 1
   // nPr = r! * nCr
   while (++k <= r) // can do this coz, numerator as well as denominator will have r terms//coz (n-r) terms cancelled out
   {				// we loop only r-1 times coz the operation (* or /) is performed only r-1 times
     npr *= --n;	// although the number of terms is r
     // npr /= k; ////////thus we cancel out the r! part
   }

   return npr;
}

int process_testcase(int n)
{
	int rv = 0;
	for(int i = 0; i < n; i++)
	{
		for(int j = i+1; j < n; j++)
			rv += ( ((A[i]-A[j])*(B[i]-B[j])) < 0)?1:0;
	}
	return rv;
}

int main(int argc, const char *argv[])
{
	int tc = 0;
	ifstream is;
	if(argc == 1)
		//is.open("C:\\Users\\viv.NTDEV\\ipfile.in");
		is.open("C:\\viv\\gcj\\gcj\\Debug\\ipfile.in");
		//C:\viv\gcj\gcj\Debug
	else
		is.open(argv[1]);

	initbitnum();
	// find total number of testcases
	string s;
	getline(is,s); 
	istringstream iss(s);
	iss >> tc;
	//printf("num tc == %d\n", tc);

	// for every testcase
	for(int i = 1; i <= tc; i++)
	{
		printf("Case #%d: ",i);
		// find number of lines for this testcase
		string ss;
		int n;
		int m;
		getline(is,ss); 
		istringstream iss(ss);
		iss >> n;
		A.clear();
		B.clear();
		for(int i= 0; i < n; i++)
		{
		getline(is,ss); 
		istringstream iss(ss);
		int a,b;
		iss >> a >> b;
		A.push_back(a);
		B.push_back(b);
		}
/*
		for(int i= 0; i < n; i++)
		{
			string s;
			getline(is,s); 
			odir.push_back(s);
		}

		for(int i= 0; i < m; i++)
		{
			string s;
			getline(is,s); 
			ndir.push_back(s);
		}
		*/
		cout << process_testcase(n) << endl;
	}
	is.close();
	return 0;
}
