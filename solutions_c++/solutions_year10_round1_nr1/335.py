#include <cstdio>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <math.h>
#include <limits.h>
#include <float.h>
#include <algorithm>
#include <iostream>

using namespace std;

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
typedef __int64 LL;
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define FORR(a,s,b) for(int a=s;a<=b;a++)
#define CLR(a,b) memset(a,b,sizeof(a))
#define VI vector<int>
#define VS vector<string>


bool RBcmp(const char &a,const char &b) {
	if(a=='.' && b!='.') return true;
	return false;
}

int n,k;

int main()
{
	int t;
	cin >> t;

	FORR(cn,1,t) {
		cout << "Case #"<<cn<<": ";

		char board[64][64];
		CLR(board,0);

		cin >> n>>k;

		int mask=0;

		FOR(i,n) {
			cin >> board[i];
			sort(board[i],board[i]+n,RBcmp);
		}

		FOR(i,n) {
			int p=board[i][0],k=1;
			FORR(j,1,n) {
				if(p==board[i][j]) k++;
				else {
					if(k>=::k) {if(p=='B') mask|=1;if(p=='R') mask|=2;}
					k=1; p=board[i][j];
				}
			}
		}

		FOR(i,n) {
			int p=board[0][i],k=1;
			FORR(j,1,n) {
				if(p==board[j][i]) k++;
				else {
					if(k>=::k) {if(p=='B') mask|=1;if(p=='R') mask|=2;}
					k=1; p=board[j][i];
				}
			}
		}

		FOR(z,2*n-1) {
			int i,j;
			if(z<n) { i=z; j=0; }
			else { i=0; j=1+z-n; }

			int p=board[i][j],k=1;
            for(;;) {
				++i; ++j;
				if(p==board[i][j]) k++;
				else {
					if(k>=::k) {if(p=='B') mask|=1;if(p=='R') mask|=2;}
					k=1; p=board[i][j];
                    if(!p) break;
				}
			}
		}

		FOR(z,2*n-1) {
			int i,j;
			if(z<n) { i=z; j=n-1; }
			else { i=0; j=z-n; }

			int p=board[i][j],k=1;
            for(;;) {
				++i; --j;
                if(i>=n || j<0) {
					if(k>=::k) {if(p=='B') mask|=1;if(p=='R') mask|=2;}
                    break;
                }
				if(p==board[i][j]) k++;
				else {
					if(k>=::k) {if(p=='B') mask|=1;if(p=='R') mask|=2;}
					k=1; p=board[i][j];
                    if(!p) break;
				}
			}
		}

		char *s;
		switch(mask) {
		case 0: s="Neither"; break;
		case 1: s="Blue"; break;
		case 2: s="Red"; break;
		case 3: s="Both"; break;
		}

		cout << s << "\n";
	}

	return 0;
}
