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
int X, S, R, N;
ld T = 0;
ld s2, r2;
struct pt{
	int s, e, a;
} mass[2005];
struct pt2{
	int l, a;
	bool operator <(const pt2 &w)const{
		return a<w.a;
	}	
} A[2005];
int xx;
int main(){
	ifstream f("input.txt");
	ofstream f2("output.txt");
	f2.setf(ios_base::fixed);
	f2.precision(9);
	f>>xx;
	for1(CASE,xx){
		f>>X>>S>>R>>T>>N;
		s2=S;r2=R;
		forn(i,N)
			f>>mass[i].s>>mass[i].e>>mass[i].a;
		int kol=N;
		if (mass[0].s!=0){
			kol++;
			mass[N].s=0;
			mass[N].e=mass[0].s;
			mass[N].a=0;
		}
		forab(i,1,N){
			if (mass[i].s!=mass[i-1].e){
				mass[kol].s=mass[i-1].e;
				mass[kol].e=mass[i].s;
				mass[kol++].a=0;
			}
		}
		if (mass[N-1].e!=X){
			mass[kol].s=mass[N-1].e;
			mass[kol].e=X;
			mass[kol++].a=0;
		}
		forn(i,kol){
			A[i].l=mass[i].e-mass[i].s;
			A[i].a = mass[i].a;
		}
		sort(A,A+kol);
		ld sum=0;
		forn(i,kol){
			if (T>0){
				ld tmp = A[i].l/(r2+A[i].a);
				if (tmp>T){
					tmp = (A[i].l-(r2+A[i].a)*T)/(s2+A[i].a)+T;
					T=-1.0f;
				} else T-=tmp;
				sum+=tmp;
			} else sum+=A[i].l/(s2+A[i].a);
		}
		f2<<"Case #"<<CASE<<": "<<sum<<endl;
	}
	f.close();
	f2.close();
	return 0;
}