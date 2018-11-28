#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<sstream>
using namespace std;

#define FOR(i,a,b) for(int i = (a); i < int(b); ++ i)
#define REP(i,n) FOR(i,0,n)
#define sz size()
#define pb push_back
#define cs c_str()
#define V(x) vector< x >

typedef V(int) VI;
typedef V(VI) VVI;
typedef V(string) VS;

int toInt(string s){ int r=0; istringstream sin(s); sin>>r; return r; }

int go(int A2, int A3, int B0, int B1, int T) {
	A3 += T;
	A2 += A3/60;
	A2 %= 24;
	A3 %= 60;
	
	int diff = B0 * 60 + B1 - (A2 * 60 + A3);
	if (diff >= 0) return diff;
	return -1;
}
	
void ip (int arr[4]) {
	string st;
	getline(cin,st);
	arr[0] = (st[0]-'0') * 10 + (st[1]-'0');
	arr[1] = (st[3]-'0') * 10 + (st[4]-'0');
	arr[2] = (st[6]-'0') * 10 + (st[7]-'0');
	arr[3] = (st[9]-'0') * 10 + (st[10]-'0');
	return ;
}

int main() {
	int num;
	string t;
	getline(cin,t);
	num = toInt(t);
	REP(z,num) {
		int T, a, b;
		int A[150][4], B[150][4];
		
		getline(cin,t);
		T = toInt(t);
		getline(cin,t);
		istringstream sin(t);
		sin >> a >> b;
		
		REP(i,a) ip(A[i]);
		REP(i,b) ip(B[i]);
		
		VI trA(a,-1),trB(b,-1);
		
		REP(i,a) {
			int flag= -1, diff= 100000000;
			REP(j,b) {
				if(trB[j] != -1) continue;
				int k= go(A[i][2],A[i][3],B[j][0],B[j][1],T);
				if(k < 0) continue;
				if( k <= diff ) flag= j, diff= k;
			}
			if(flag >= 0 ) trB[flag] = i;
		}
		REP(i,b) {
			int flag= -1, diff= 100000000;
			REP(j,a) {
				if(trA[j] != -1) continue;
				int k= go(B[i][2],B[i][3],A[j][0],A[j][1],T);
				if(k < 0) continue;
				if( k <= diff ) flag= j, diff= k;
			}
			if(flag >= 0 )trA[flag] = i;
		}
		int sumA =0, sumB =0;
		REP(i,a) if(trA[i] == -1) sumA++;
		REP(i,b) if(trB[i] == -1) sumB++;
		cout << "Case #"<< z+1 <<": " << sumA <<" "<< sumB <<endl;
	}
	return 0;
}
