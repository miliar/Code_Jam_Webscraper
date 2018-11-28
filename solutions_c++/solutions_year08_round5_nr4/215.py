#include <string>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <stack>
#include <queue>
#include <algorithm>
#include <deque>
#include <utility>
#include <sstream>
#include <vector>
#include <map>
#include <ctime>
#include <set>
using namespace std;
#define sz size()
#define vi vector<int>
#define vs vector<string>
#define dsz size()-1
#define pb push_back
#define maxn(a,b) (a) = ((a) < (b) ? (b) : (a))
#define FUP(ii,ss,ff) for ((ii) = (ss);(ii) <= (ff);(ii)++)
#define FDOWN(ii,ss,ff) for ((ii) = (ss);(ii) >= (ff);(ii)--)
#define FALL(ii, vv) for ((ii) = 0;signed (ii) <= signed ((vv).dsz);(ii)++)
#define ITERATE(__it,__container) for(__it=__container.begin(); __it!=__container.end(); __it++)
#define EPS 1e-12
#define INF 2147483647
#define sgn(x) ((x)>0 ? 1 : (x)==0 ? 0 : -1)
#define sq(x) ((x)*(x))
#define sorta(a) sort(a.begin(), a.end())
#define cleara(a, b) memset(a, b, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define absd(a) ((a)<0?-(a):(a))
#define absm absd
#define mp make_pair
typedef unsigned int uint;
typedef long long ll;
#ifdef _TS
#define assert(x) if (!(x))_asm int 3;
#define dprintf printf
#define LL "I64"
#else
#include <cassert>
#define dprintf //
#define LL "ll"
#endif
 
#define READ_BUF_SIZE 100*1024
#define WRITE_BUF_SIZE 100*1024
 
class StdIO{
public:
	StdIO(){
		pos_read = 0;
		pos_write = 0;
		buf_read_len = 0;
		eof = false;
		memset(white_table, false, 256);
		int i;
		FUP(i,0,32)
			white_table[i] = true;
	}
	~StdIO(){
		flushWrite();
	}
	bool isEOF(){
		if (eof)
			return true;
		if (pos_read == buf_read_len)
			return eof = !_read();
		return false;
	}
	int getChar(){
		if(isEOF())
			return -1;
		return buf_read[pos_read++];
	}
	int getCharNonWhite(){
		int c;
		while ((c=getChar()) != -1 && white_table[c])
			;
		return c;
	}
	void ungetChar(){
		if (eof)
			return;
		if(!(pos_read--))
			pos_read = 0;
	}
	void flushWrite(){
		if (!pos_write)
			return;
		fwrite(buf_write, 1, pos_write, stdout);
		pos_write = 0;
	}
	template<typename T> T readInt(){
		T ret=0;
		trimWhite();
		int c=getChar();
		bool sg=false;
		if (c == -1)
			return 0;
		else if (c == '-'){
			sg = true;
			c = getChar();
		}
		do
			ret = (ret<<3) + (ret<<1) + c-'0';
		while ((c=getChar()) >= '0' && c <= '9');
		ungetChar();
		return sg?-ret:ret;
	}
	string readString(){
		string ret;
		trimWhite();
		int c;
		while ((c=getChar()) != -1 && !white_table[c])
			ret += (char)c;
		ungetChar();
		return ret;
	}
	char* readStringLow(){
		throw 0; // unimplemented
	}
	void readStringLow(char* str){
		trimWhite();
		int c;
		int pos = 0;
		while ((c=getChar()) != -1 && !white_table[c])
			str[pos++] = (char)c;
		str[pos] = 0;
		ungetChar();
	}
	void readStringLow(char* str, int len){
		int pos = 0;
		while (len--)
			str[pos++] = (char)getChar();
	}
	void trimWhite(){
		int c;
		while ((c=getChar())!=-1 && white_table[c])
			;
		ungetChar();
	}
	void setWhite(string chars, bool areWhite){
		for(int i = chars.size()-1; i >= 0; i--)
			white_table[chars[i]] = areWhite;
	}
	void putChar(char c){
		if (pos_write == WRITE_BUF_SIZE)
			flushWrite();
		buf_write[pos_write++] = c;
	}
	void writeString(string& str){
		writeString(str.c_str(), str.size());
	}
	void writeString(const char* str){
		writeString(str, strlen(str));
	}
	void writeString(const char* str, int len){
		int i;
		FUP(i,0,len-1)
			putChar(str[i]);
	}
	template<typename T> void writeInt(T num){
		string ret;
		if (num == 0)
			ret += '0';
		while (num != 0){
			ret += '0' + (num%10);
			num/=10;
		}
		reverse(ALL(ret));
		writeString(ret);
	}
private:
	int _read(){
		buf_read_len -= pos_read;
		if (buf_read_len)
			memcpy(buf_read, buf_read + pos_read, buf_read_len);
		pos_read = 0;
		return buf_read_len += fread(buf_read + buf_read_len, 1, READ_BUF_SIZE - buf_read_len, stdin);
	}
	bool eof;
	unsigned char buf_read[READ_BUF_SIZE];
	unsigned char buf_write[WRITE_BUF_SIZE];
	bool white_table[256];
	int pos_read;
	int pos_write;
	int buf_read_len;
};

StdIO io;

void minn(int& a, int b){
	if (a>b)a=b;
}

#define MOD 10007

int prime[100000];
vi prm;
void pri(){
	int i,j;
	for (i=2; i<100000; i++)if (!prime[i]){
		prm.pb(i);
		for (j=2*i; j < 100000; j+=i)
			prime[j]=1;
	}
}

int bf(int n, int p){
	int ret=0;
	while (n>=p){
		n/=p;
		ret+=n;
	}
	return ret;
}
int pw(int n, int p){
	int ret=1;
	while (p){
		if (p&1){
			ret *= n;
			ret %= MOD;
		}
		n*=n;
		n%=MOD;

		p/=2;
	}
	return ret;
}
int binom(int n, int k){
	int ret=1, i, p;
	if (k<0 || k>n)return 0;
	p = MOD;
	ret*=pw(p, bf(n, MOD) - bf(k, MOD) - bf(n-k, MOD));
	if (ret)FALL(i,prm){
		p = prm[i];
		ret*=pw(p, bf(n, p) - bf(k, p) - bf(n-k, p));
		ret%=MOD;
		if (p >= n)break;
	}
	return ret;
}

int x[100];
int y[100];
vector<pair<int, int> > xs, ys;
int main(){
	int t = io.readInt<int>(), tt, ret, W, H, R, n, i, j, m, sret, sg;
	pri();
	FUP(tt,1,t){
		W = io.readInt<int>();
		H = io.readInt<int>();
		R = io.readInt<int>();
		FUP(i,0,R-1){
			x[i] = io.readInt<int>()-1;
			y[i] = io.readInt<int>()-1;
		}
		W--;
		H--;
		n = (W+H)/3;
		m = (1<<R)-1;
		ret = 0;
		if(W==0&&H==0)ret=1;
		FUP(i,0,m){
			xs.clear();
			ys.clear();
			sg=1;
			xs.pb(mp(0,0));
			ys.pb(mp(0,0));
			xs.pb(mp(W,H));
			ys.pb(mp(H,W));
			FUP(j,0,R-1)if (i&(1<<j)){
				xs.pb(mp(x[j], y[j]));
				ys.pb(mp(y[j], x[j]));
				sg = -sg;
			}
			sorta(xs);
			sorta(ys);
			FALL(j,ys)
				swap(ys[j].first, ys[j].second);
			if (xs!=ys)continue;
			sret=1;
			FALL(j, xs)if (j){
				if (xs[j].second <= xs[j-1].second)goto fal;

				n = (xs[j].first - xs[j-1].first) + (xs[j].second - xs[j-1].second);
				if (n%3)goto fal;
				n/=3;
				sret *= binom(n, (xs[j].first - xs[j-1].first)-n);
				sret %= MOD;
			}
			ret += MOD + sret*sg;
			ret%=MOD;
fal:;
		}
		printf("Case #%d: %d\n", tt, ret);
	}
	return 0;
}
 