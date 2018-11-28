// esta3anna 3al sha2a belAllah ..
#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<limits.h>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>
using namespace std ;
#define rep(i,n,m) for(int i = (int)(n), _m = (int)(m); i < _m; ++ i)
#define	rrep(i,n,m) for(int i = (int)(n), _m = (int)(m); i >= _m; -- i)
#define all(v) (v.begin(), v.end())
#define rall(v) (v.rbegin(), v.rend())
#define sz size()
#define pb push_back
#define mp make_pair
#define mems(arr, v) memset(arr, v, sizeof arr)
#define setBit(mask, bit) ((mask) | (1LL << (bit)))
#define resetBit(mask, bit) ((mask) & (~(1LL << (bit))))
#define flipBit(mask, bit) ((mask) ^ (1LL << (bit)))
#define is0(mask, bit)(((mask) & (1LL << (bit))) == 0)
#define is1(mask, bit)(((mask) & (1LL << (bit))) != 0)
#define removeLastBit(mask) ((mask) & ((mask) - 1LL))
#define firstBitOn(mask) ((mask) & ~((mask) - 1LL))
#define grayCode(mask) ((mask) ^ ((mask) << 1LL))
#define repSubMasks(subMask, mask) for(ll subMask = (ll)(mask), _mask = subMask; subMask; subMask = _mask & (subMask - 1))
int countBits(int mask) {int res = 0; while(mask) mask &= (mask - 1), ++ res; return res;}
#define INT_MAX  2000000000
#define INT_MIN -INT_MAX
#define EPS 1e-9
#define debug(x) cout << #x << " : " << x << endl
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
#define Read() freopen("input.txt","r",stdin)
#define Write() freopen("output.txt","w",stdout)
int main() {
	Read();
	Write();
	int cases;
	char board[4][4];
	cin >> cases;
	rep(C, 1, cases + 1) {
		bool x, o, X = false;
		bool O = false;
		bool emptyPlace = false;
		rep(i, 0, 4)
			rep(j, 0, 4) {
				cin >> board[i][j];
				emptyPlace |= board[i][j] == '.';
		}
		rep(i, 0, 4) {
			x = true;
			o = true;
			rep(j, 0, 4) {
				x &= board[i][j] == 'X' || board[i][j] == 'T';
				o &= board[i][j] == 'O' || board[i][j] == 'T';
			}
			X |= x;
			O |= o;
			x = true;
			o = true;
			rep(j, 0, 4) {
				x &= board[j][i] == 'X' || board[j][i] == 'T';
				o &= board[j][i] == 'O' || board[j][i] == 'T';
			}
			X |= x;
			O |= o;
		}

		x = true;
		o = true;
		rep(i, 0, 4) {
			x &= board[i][i] == 'X' || board[i][i] == 'T';
			o &= board[i][i] == 'O' || board[i][i] == 'T';
		}
		X |= x;
		O |= o;

		x = true;
		o = true;
		rep(i, 0, 4) {
			x &= board[i][4 - i - 1] == 'X' || board[i][4 - i - 1] == 'T';
			o &= board[i][4 - i - 1] == 'O' || board[i][4 - i - 1] == 'T';
		}
		X |= x;
		O |= o;

		cout << "Case #" << C << ": ";
		if(X)
			puts("X won");
		else if(O)
			puts("O won");
		else if(emptyPlace == false)
			puts("Draw");
		else
			puts("Game has not completed");
	}
}