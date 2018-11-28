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

char str[100];
int mnx,mny,mxx,mxy;
int tmxx[7000];
int tmxy[7000];
int tmnx[7000];
int tmny[7000];
bool chg[7000][7000];
int x,y,d=0;
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};
void go(char c){
	if (c=='L')
		d--;
	else if (c=='R')
		d++;
	else if (c=='F'){
		if (d==1)
			chg[x][y]=1;
		else if (d==3)
			chg[x][y-1]=1;

		x+=dx[d];
		y+=dy[d];

		minn(mnx, x);
		minn(mny, y);
		maxn(mxx, x);
		maxn(mxy, y);

		minn(tmnx[x], y);
		minn(tmny[y], x);
		maxn(tmxx[x], y);
		maxn(tmxy[y], x);
	}

	d+=4;
	d%=4;
}
int main(){
	int t = io.readInt<int>(), tt, L,i,T,ret;
	vector<int> p;
	FUP(tt,1,t){
		L = io.readInt<int>();
		x=y=3500;
		ret=0;
		FUP(i,0,6999)
			tmxx[i] = tmxy[i] = 0;
		FUP(i,0,6999)
			tmnx[i] = tmny[i] = 7000-1;
		cleara(chg,0);
		mnx=mny=7000-1;
		mxx=mxy=-0;
		while (L--){
			io.readStringLow(str);
			T = io.readInt<int>();
			while (T--)
				for(i=0; str[i]; i++)
					go(str[i]);
		}
		assert(x==y && y==3500);
		FUP(x,mnx,mxx)FUP(y,mny,mxy){
			chg[x][y] ^= chg[x-1][y];
			if (!chg[x][y] &&(
				(max(tmnx[x],tmnx[x+1]) <= y && y < min(tmxx[x], tmxx[x+1])) ||
				(max(tmny[y],tmny[y+1]) <= x && x < min(tmxy[y], tmxy[y+1]))))
				ret++;
			}
		printf("Case #%d: %d\n", tt, ret);
	}
	return 0;
}
 