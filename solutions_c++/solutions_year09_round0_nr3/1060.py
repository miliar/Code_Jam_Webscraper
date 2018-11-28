#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()
#define sz(a) int((a).size()) 
#define pb push_back 
typedef long long LL;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 

class INPUT {
  static const int BUFSIZE = 1<<16;
  static char buffer[];
  char *bufpos;
  char *bufend;
  void grabBuffer();
 public:
  INPUT() { grabBuffer(); }
  bool eof() { return bufend==buffer; }
  char nextChar() { return *bufpos; }
  inline char readChar();
  inline void skipWS();
  unsigned readUnsigned();
  int readInt();
};

char INPUT::buffer[INPUT::BUFSIZE];

void INPUT::grabBuffer() {
  bufpos = buffer;
  bufend = buffer + fread( buffer, 1,BUFSIZE,stdin);
}

char INPUT::readChar() {
  char res = *bufpos++;
  if(bufpos==bufend) grabBuffer();
  return res;
}

inline bool myisspace(char c) { return c<=' '; }

void INPUT::skipWS() {
  while(!eof() && myisspace(nextChar())) readChar();
}

unsigned INPUT::readUnsigned() {
  skipWS();
  unsigned res = 0;
  while(!eof() && isdigit(nextChar())) {
    res = 10u * res + (readChar()-'0');
  }
  return res;
}

int INPUT::readInt() {
  skipWS();
  bool neg = false;
  if(!eof() && nextChar()=='-') { neg=true; readChar(); }
  int res = static_cast<int>(readUnsigned());
  if(neg) res = -res;
  return res;
}


class OUTPUT {
  static const int BUFSIZE = 1<<16;
  static char buffer[];
  char *bufpos;
  char *BUFLIMIT;
  void flushBuffer();
 public:
  OUTPUT():bufpos(buffer),BUFLIMIT(buffer+BUFSIZE-100) {}
  ~OUTPUT() { flushBuffer(); }
  inline void operator()(char c);
  inline void operator()(unsigned x);
  inline void operator()(int x);
  inline void operator()(const char*s);
  void operator()(const string&s) { operator()(s.c_str()); }
  template<class A,class B>
  void operator()(const A& a,const B& b) {
    operator()(a); operator()(b);
  }
  template<class A,class B,class C>
  void operator()(const A& a,const B& b,const C&c) {
    operator()(a); operator()(b); operator()(c);
  }
  template<class A,class B,class C,class D>
  void operator()(const A& a,const B& b,const C&c,const D&d) {
    operator()(a); operator()(b); operator()(c); operator()(d);
  }
  template<class A,class B,class C,class D,class E>
  void operator()(const A& a,const B& b,const C&c,const D&d,const E&e) {
    operator()(a); operator()(b); operator()(c); operator()(d); operator()(e);
  }
  template<class A,class B,class C,class D,class E,class F>
  void operator()(const A& a,const B& b,const C&c,const D&d,const E&e,const F&f) {
    operator()(a); operator()(b); operator()(c); operator()(d); operator()(e); operator()(f);
  }
};

char OUTPUT::buffer[OUTPUT::BUFSIZE];

void OUTPUT::flushBuffer() {
  char *p = buffer;
  while(p < bufpos) {
    p += fwrite( p,1, bufpos-p,stdout);
  }
  bufpos = buffer;
}

void OUTPUT::operator()(char c) {
  *bufpos = c;
  ++bufpos;
  if(bufpos >= BUFLIMIT) flushBuffer();
}

void OUTPUT::operator()(unsigned x) {
  char *old = bufpos;
  do {
    *bufpos = char('0' + x % 10u);
    x /= 10u;
    ++bufpos;
  } while(x);
  reverse(old, bufpos);
  if(bufpos >= BUFLIMIT) flushBuffer();
}

void OUTPUT::operator()(int x) {
  if(x<0) { operator()('-'); x = -x; }
  operator()(static_cast<unsigned>(x));
}

void OUTPUT::operator()(const char*s) {
  while(*s) operator()(*s++);
}

INPUT input;
OUTPUT output;





string s="welcome to code jam";
int dp[20][501];
char str[501];
int main()
{
	int runs;
	for(int i=0;i<501;i++) dp[0][i] =1;
	for(int i=1;i<20;i++) dp[i][0] = 0;
	runs = input.readUnsigned();	
	int temp = runs;
	while(runs--)
	{
		int len =0;
		char ch;
		input.skipWS();
		while( (ch = input.readChar()) != '\n')
			str[len++] = ch;
		str[len] = 0;
		
		for(int j=1;j<20;j++)
		{
			for(int i=1;i<=len;i++)
			{
				if(str[i-1] == s[j-1])
				{
					dp[j][i] = dp[j-1][i]+dp[j][i-1];
					dp[j][i] = dp[j][i] %10000;
				}
				else
				{
					dp[j][i] = dp[j][i-1];
				}
			}
		}
		printf("Case #%d: %04d\n",temp-runs,dp[19][len]);
	}
}





