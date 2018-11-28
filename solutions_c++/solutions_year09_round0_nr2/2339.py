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
		if (num < 0){
			num = -num;
			putChar('-');
		}
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

#define ri io.readInt<int>

int m[101][101];
int d[101][101];

int dx[] = {0,-1,1,0};
int dy[] = {-1,0,0,1};

int ok(int x, int y, int W, int H) {
	if (x <0 || y < 0 || x >= W || y >= H) return 0;
	return 1;
}

int gh(int x, int y, int W, int H) {
	if (!ok(x, y, W, H)) return 1010101;
	return m[x][y];
}

int que[101*101][2];
int qs,qe;

int main(){
	int T;
	int TT = ri();
	int i,j,k;
	//_asm int 3;
	FUP(T,1,TT){
		int H = ri();
		int W = ri();
		FUP(j,0,H-1) {
			FUP(i,0,W-1) {
				m[i][j] = ri();
			}
		}
		qs=qe=0;
		cleara(d, 0);
		FUP(i,0,W-1) {
			FUP(j,0,H-1) {
				FUP(k,0,3) {
					if (gh(i+dx[k], j+dy[k], W, H) < m[i][j])
						break;
				}
				if (k == 4) {
					que[qe][0] = i;
					que[qe][1] = j;
					d[i][j] = ++qe;
				}
			}
		}
		while (qs != qe) {
			int x = que[qs][0];
			int y = que[qs++][1];
			int d1, d2;
			FUP(d1, 0, 3) {
				int nx = x+dx[d1];
				int ny = y+dy[d1];
				if (!ok(nx, ny, W, H))
					continue;
				if (d[nx][ny] > 0)
					continue;
				int b = -1;
				int mn = 1010100;
				FUP(d2, 0, 3) {
					int nnx = nx+dx[d2];
					int nny = ny+dy[d2];
					if (ok(nnx, nny, W, H) && gh(nnx, nny, W, H) < mn) {
						mn = gh(nnx, nny, W, H);
						b = d[nnx][nny];
					}
				}
				if (b > 0) {
					d[nx][ny] = b;
					que[qe][0] = nx;
					que[qe++][1] = ny;
				}
			}
		}
		map<int, char> rr;
		char last = 'a';
		printf("Case #%d:\n", T);
		FUP(j,0,H-1) {
			FUP(i,0,W-1) {
				if (rr.count(d[i][j]) == 0) {
					rr[d[i][j]] = last++;
				}
				printf("%c ", rr[d[i][j]]);
			}
			printf("\n");
		}
	}

	return 0;
}

