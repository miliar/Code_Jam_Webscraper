#include <unistd.h>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cassert>
#include <cstring>
using namespace std;
typedef long long LL;
typedef unsigned uint;
typedef unsigned long long ULL;
#define FOR(x, b, e) for (int x = (b); x <= (e); ++x)
#define FORD(x, b, e) for (int x = (b); x >= (e); --x)
#define REP(x, n) for (int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int) (x).size())
#define EACH(i, c) for (VAR(i, (c).begin()); i != (c).end(); ++i)
#define REACH(i, c) for (VAR(i,(c).rbegin()); i != (c).rend(); ++i)
#define CLR(x, v) memset(x, v, sizeof(v))
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
const int INF = 1000000001;
const double EPS = 10e-9;

typedef pair<int,int> PII;

typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<uint> VU;
typedef vector<ULL> VULL;
typedef vector<double> VD;
typedef vector<string> VS;
typedef vector<bool> VB;
typedef vector<PII> VPII;

typedef vector<VI> VVI;
typedef vector<VLL> VVLL;
typedef vector<VU> VVU;
typedef vector<VULL> VVULL;
typedef vector<VD> VVD;
typedef vector<VS> VVS;
typedef vector<VB> VVB;
typedef vector<VPII> VVPII;

const int INPUT_SIZE = 1 << 16;
char INPUT[INPUT_SIZE];
class Input
{
	char * curr;
	char * last;
	char buf[128];
	void grab()
	{
		curr = INPUT;
		last = INPUT + read(0, INPUT, INPUT_SIZE);
	}
	bool eof()
	{
		return curr == last;
	}
public:
	Input() : curr(0), last(0)
	{
		grab();
	}
	char next()
	{
		return *curr;
	}
	char getChar()
	{
		char res = *curr++;
		if (curr == last) {
			grab();
		}
		return res;
	}
	void skipWs()
	{
		while (!eof() && isSpace(next())) {
			getChar();
		}
	}
	static bool isSpace(unsigned char x)
	{
		return x <= ' ';
	}
	uint getUint()
	{
		skipWs();
		char * e = buf, * p = buf;
		uint res = 0;
		while (!eof() && next() >= '0' && next() <= '9') {
			*e++ = getChar() - '0';
		}
		while (p < e) {
			res *= 10u;
			res += *p++;
		}
		return res;
	}
	ULL getULL()
	{
		skipWs();
		char * e = buf, * p = buf;
		ULL res = 0;
		while (!eof() && next() >= '0' && next() <= '9') {
			*e++ = getChar() - '0';
		}
		while (p < e) {
			res *= 10u;
			res += *p++;
		}
		return res;
	}
	int getInt()
	{
		skipWs();
		bool neg = false;
		if (!eof() && next() == '-') {
			neg = true;
			getChar();
		}
		int res = getUint();
		return neg ? -res : res;
	}
	LL getLL()
	{
		skipWs();
		bool neg = false;
		if (!eof() && next() == '-') {
			neg = true;
			getChar();
		}
		LL res = getULL();
		return neg ? -res : res;
	}
	void getStr(char * s)
	{
		skipWs();
		while (!eof() && !isSpace(next())) {
			*s++ = getChar();
		}
		*s = 0;
	}
	void getStr(char * s, char delim)
	{
		while (!eof() && next() != delim) {
			*s++ = getChar();
		}
		getChar(); // skip delimeter
		*s = 0;
	}
	double getDouble()
	{
		skipWs();
		getStr(buf);
		double res;
		sscanf(buf, "%lf", &res);
		return res;
	}
	Input & operator , (char & x)
	{
		x = getChar();
		return *this;
	}
	Input & operator , (int & x)
	{
		x = getInt();
		return *this;
	}
	Input & operator , (uint & x)
	{
		x = getUint();
		return *this;
	}
	Input & operator , (char * s)
	{
		getStr(s);
		return *this;
	}
	Input & operator , (ULL & x)
	{
		x = getULL();
		return *this;
	}
	Input & operator , (LL & x)
	{
		x = getLL();
		return *this;
	}
	Input & operator , (double & x)
	{
		x = getDouble();
		return *this;
	}
};

const int OUTPUT_SIZE = 1 << 16;
char OUTPUT[OUTPUT_SIZE];
class Output
{
	char * curr;
	char buf[128];
public:
	Output() : curr(OUTPUT)
	{
	}
	Output(const Output &);
	Output & operator = (const Output &);
	~Output()
	{
		flush();
	}
	void flush()
	{
		if (curr != OUTPUT) {
			write(1, OUTPUT, curr - OUTPUT);
			curr = OUTPUT;
		}
	}
	void put(char x)
	{
		*curr++ = x;
		if (curr == OUTPUT + OUTPUT_SIZE) {
			flush();
		}
	}
	Output & operator , (char x)
	{
		put(x);
		return *this;
	}
	Output & operator , (uint x)
	{
		char * p = buf;
		do {
			*p++ = x % 10u + '0';
		} while (x /= 10u);
		
		while (p > buf) {
			put(*--p);
		}
		
		return *this;
	}
	Output & operator , (ULL x)
	{
		char * p = buf;
		do {
			*p++ = x % 10u + '0';
		} while (x /= 10u);
		
		while (p > buf) {
			put(*--p);
		}
		
		return *this;
	}
	Output & operator , (int x)
	{
		if (x < 0) {
			put('-');
			x = -x;
		}
		return operator , ((uint) x);
	}
	Output & operator , (LL x)
	{
		if (x < 0) {
			put('-');
			x = -x;
		}
		return operator , ((ULL) x);
	}
	Output & operator , (const char * s)
	{
		while (*s) {
			put(*s++);
		}
		return *this;
	}
	Output & operator , (double x)
	{
		sprintf(buf, "%lf", x);
		return operator , (buf);
	}
};

#define DEB_COND 1
#define db(x) { if (DEB_COND) { cerr << __LINE__ << " " << #x << " " << x << endl; } }
#define dbv(x) { if (DEB_COND) { cerr << __LINE__ << " " << #x << ": "; EACH (__i, x) cerr << *__i << " "; cerr << endl; } }


LL freqs[10001];

static bool testFreq(LL a, LL b)
{
	return a > b ? a % b == 0 : b % a == 0;
}

int main()
{
	Input input;
	Output output;
	int t;
	input, t;
	REP (tt, t) {
		
		int n;
		LL l, h;
		input, n, l, h;
		
		REP (nn, n) {
			input, freqs[nn];
		}
		
		LL ans = -1;
		
		FOR (x, (int)l, (int)h) {
			bool ok = 1;
			REP (nn, n) {
				if (!testFreq(x, freqs[nn])) {
					ok = 0;
					break;
				}
			}
			if (ok) {
				ans = x;
				break;
			}
		}
		
		output, "Case #", tt + 1, ": ";
		(ans == -1 ? (output, "NO") : (output, ans)), '\n';
	}
	
}
