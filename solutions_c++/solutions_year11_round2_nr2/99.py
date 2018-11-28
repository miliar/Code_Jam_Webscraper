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

using namespace std;
ll t;
ll n;
ll r;
ll mass[1000005];
ll mass2[1000005];
ll mass3[1000005];
ld two=2;
ld answ=0;
int main(){
	ofstream f2("output.txt");
	f2.setf(ios_base::fixed);
	f2.precision(8);
	ifstream f("input.txt");
	f>>t;
	for1(xx,t){
		f>>n>>r;
		answ=0;
		forn(i,n){
			f>>mass[i]>>mass2[i];
		}
		mass3[0]=0;
		forn(i,n){
			mass3[i+1]=mass3[i]+mass2[i];
		}
		forn(i,n){
			for(int j=i;j!=n;j++){
				ll sum=mass3[j+1]-mass3[i];
				ll rast=mass[j]-mass[i];
				ll tmprast = (sum-1)*r;
				answ=MAX(answ,(tmprast-rast)/two);
			}
		}
		f2<<"Case #"<<xx<<": "<<answ<<endl;
	}
	f.close();
	f2.close();
	return 0;
}