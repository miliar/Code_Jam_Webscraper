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

using namespace std;
int t;
list<int> b;
list<int> o;
bool mass[1000];
int time1;
int time2;
int n;
char c;
int val;
int pos1,pos2;

int Case=1;
int main(){
	ifstream f("input.txt");
	ofstream f2("output.txt");
	f>>t;
	forn(xx,t){
		b.clear();
		o.clear();
		f>>n;
		time1=0;
		time2=0;
		pos1=1;
		pos2=1;
		int nom=1;
		forn(i,n){
			f>>c;
			mass[i]=(c=='B');
			f>>val;
			if (mass[i]){
				b.pb(val);
			} else o.pb(val);
		}
		list<int>::iterator io=o.begin();
		list<int>::iterator ib=b.begin();
		forn(xx,n){
			if (!mass[xx]){
				int tmpT=ABS(pos1-*io)+1;
				pos1=*io;
				io++;
				time1+=tmpT;
				if (time1<=time2) time1=time2+1;
			} else {
				int tmpT=ABS(pos2-*ib)+1;
				pos2=*ib;
				ib++;
				time2+=tmpT;
				if (time2<=time1) time2=time1+1;
			}
		}
		f2<<"Case #"<<Case++<<": "<<MAX(time1,time2)<<endl;
	}
	f.close();
	f2.close();
	return 0;
}