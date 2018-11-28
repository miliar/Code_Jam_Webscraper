#include <string>
#include <vector>
#include <map>
#include <list>
#include <map>
#include <set>
#include <math.h> 
#include <fstream>
#include <iostream>
#include <algorithm>
#include <sstream>

#define pb(a) push_back(a) 
#define sz size()

typedef long long ll;
typedef long double ld;

inline void swap(int &a, int &b){int tmp=a;a=b;b=tmp;}
inline void swap(ll &a, ll &b){ll tmp=a;a=b;b=tmp;}
inline void swap(ld &a, ld &b){ld tmp=a;a=b;b=tmp;}
inline ld ABS(const ld &val) {return val<0?-val:val;}

inline ll MAX(const ll &a, const ll &b){return a>b?a:b;}
inline int MAX(const int &a, const int &b){return a>b?a:b;}
inline ll MIN(const ll &a, const ll &b){return a<b?a:b;}
inline int MIN(const int &a, const int &b){return a<b?a:b;}
inline ld MAX(const ld &a, const ld &b){return a>b?a:b;}
inline ld MIN(const ld &a, const ld &b){return a<b?a:b;}

#define forn(i,n) for(int i=0;i!=n;i++)
#define for1(i,n) for(int i=1;i<=n;i++)
#define forab(i,a,b) for(int i=a;i!=b;i++)
#define for1ab(i,a,b) for(int i=a+1;i<=b;i++)
#define ford(i,n) for(int i=n-1;i!=-1;i--)
#define ford1(i,n) for(int i=n;i!=0;i--)


const int INTinf=2147483647;
const int nINTinf=0-2147483648;
#define LLinf 9223372036854775807


using namespace std;
int XXX;
int A[10][10];
int B[10][10];
int size;
ld work(int x, int y){
	ld answX = 0;
	ld answY = 0;
	ld center = (size-1)/2.0;
	swap(B[x][y],A[x][y]);
	swap(B[x+size-1][y],A[x+size-1][y]);
	swap(B[x][y+size-1],A[x][y+size-1]);
	swap(B[x+size-1][y+size-1],A[x+size-1][y+size-1]);
	forn(j,size){
		forn(i,size){
			answX+=A[x+i][y+j]*(center-i);
			answY+=A[x+i][y+j]*(center-j);
		}
	}
	swap(B[x][y],A[x][y]);
	swap(B[x+size-1][y],A[x+size-1][y]);
	swap(B[x][y+size-1],A[x][y+size-1]);
	swap(B[x+size-1][y+size-1],A[x+size-1][y+size-1]);

	return ABS(answX)+ABS(answY);
}
int n,m,d;
char c;
int main(){
	ifstream f("input.txt");
	ofstream f2("output.txt");
	f>>XXX;
	for1(CASE, XXX){
		f>>n>>m>>d;
		forn(i,n){
			forn(j,m){
				f>>c;
				A[i][j]=c-'0'+d;
			}
		}
		size = MIN(n,m);
		bool ok=false;
		while (size!=2){
			int ton = n-size+1;
			int tom = m-size+1;
			forn(i,ton){
				forn(j,tom){
					ld tmp = work(i, j);
					if (tmp<0.00001) {
						ok=true;
						f2<<"Case #"<<CASE<<": "<<size<<endl;
						break;
					}
				}
				if (ok) break;
			}
			if (ok) break;
			size--;
		}
		if (!ok)
			f2<<"Case #"<<CASE<<": IMPOSSIBLE"<<endl;
	}

	f.close();
	f2.close();
	return 0;
}