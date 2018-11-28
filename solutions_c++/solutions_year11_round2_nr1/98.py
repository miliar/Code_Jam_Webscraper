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

inline void swap(int &a,int &b){int tmp;tmp=a;a=b;b=tmp;} 

#define pb(a) push_back(a) 
#define sz size()

#define ll long long
#define ld long double

inline int MIN(const int &q, const int &b){return q<b?q:b;}
inline ll MIN(const ll &q, const ll &b){return q<b?q:b;}
inline ld MIN(const ld &q, const ld &b){return q<b?q:b;}
inline int MAX(const int &q, const int &b){return q>b?q:b;}
inline ll MAX(const ll &q, const ll &b){return q>b?q:b;}
inline ld MAX(const ld &q, const ld &b){return q>b?q:b;}
inline ld ABS(const ld &q){return q<0?-q:q;}
inline ll ABS(const ll &q){return q<0?-q:q;}
inline int ABS(const int &q){return q<0?-q:q;}

inline void swap(ll &a, ll &b){ll tmp=a;a=b;b=tmp;}
inline void swap(ld &a, ld &b){ld tmp=a;a=b;b=tmp;}

#define forn(i,n) for(int i=0;i!=n;i++)
#define for1(i,n) for(int i=1;i<=n;i++)
#define forab(i,a,b) for(int i=a;i!=b;i++)
#define for1ab(i,a,b) for(int i=a+1;i<=b;i++)
#define ford(i,n) for(int i=n-1;i!=-1;i--)
#define ford1(i,n) for(int i=n;i!=0;i--)

#define tochn 1e-7
#define INTinf 2147483647
#define LLinf 9223372036854775807
int t;
int n;
using namespace std;

char m[105][105];
int wins[105], games[105];
ld pwin[105], powin[105], poowin[105];
ld k1=0.25;
ld k2=0.5;
ld k3=0.25;
int main(){
	ifstream f("input.txt");
	ofstream f2("output.txt");
	f2.setf(ios_base::fixed);
	f2.precision(8);
	f>>t;
	forn(xx,t){
		f>>n;
		forn(i,n){
			f>>m[i];
		}
		memset(wins,0,sizeof(wins));
		memset(games,0,sizeof(games));
		forn(i,n){
			forn(j,n){
				if (m[i][j]!='.') {
					games[i]++;
					if (m[i][j]=='1') wins[i]++;
				}
			}
			pwin[i]=((ld)wins[i])/games[i];
		}

		forn(i,n){
			int kol=0;
			ld sum=0;
			forn(j,n){
				if (m[i][j]!='.'){
					kol++;
					int tmp1 = games[j]-1;
					int tmp2=wins[j];
					if (m[i][j]=='0') tmp2--;
					sum+=((ld)tmp2)/tmp1;
				}
			}
			powin[i]=sum/(ld)kol;
		}

		f2<<"Case #"<<xx+1<<':'<<endl;
		forn(i,n){
			int kol=0;
			ld sum=0;
			forn(j,n){
				if (m[i][j]!='.'){
					kol++;
					sum+=powin[j];
				}
			}
			poowin[i]=sum/(ld)kol;
			f2<<k1*pwin[i]+k2*powin[i]+k3*poowin[i]<<endl;
		}
	}
	f2.close();
	f.close();
	return 0;
}