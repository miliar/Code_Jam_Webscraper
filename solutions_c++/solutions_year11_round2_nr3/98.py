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
int t;
int n,m;
int a[10],b[10];
int met[10];

vector<list<int> > vc2;
bool OK=false;
int KOL=0;
void rec(int pos){
	if (pos==n){
		int must=0;
		forn(i,KOL){
			must|=(1<<i);
		}
		forn(i,vc2.sz){
			int tmp=0;
			for(list<int>::iterator j=vc2[i].begin(); j!=vc2[i].end();j++){
				tmp|=(1<<(met[*j]-1));
			}
			if (tmp!=must) return;
		}
		OK=true;
		return;
	} else {
		for1(i,KOL){
			met[pos]=i;
			rec(pos+1);
			if (OK) return;
		}
	}
}
bool check(int kol){
	KOL=kol;
	rec(0);
	return OK;
}
list<int> group;
int main(){
	ifstream f("input.txt");
	ofstream f2("output.txt");
	f>>t;
	
	for1(xx,t){
		OK=false;
		vc2.clear();
		group.clear();
		memset(met,0,sizeof(met));
		f>>n>>m;
		forn(i,m) f>>a[i];
		
		forn(i,n)
			group.pb(i);
		vc2.pb(group);
		forn(i,m) {
			f>>b[i];
			a[i]--;b[i]--;
			if (a[i]>b[i]) swap(a[i],b[i]);
			bool find=false;
			forn(j,vc2.sz){
				for(list<int>::iterator l=vc2[j].begin();l!=vc2[j].end();l++){
					if (*l==a[i]){
						bool x=false;
						for(list<int>::iterator r=l;r!=vc2[j].end();r++){
							if (*r==b[i]){
								x=true;
								break;
							}
						}
						if (!x) break;
						group.clear();
						group.pb(a[i]);
						list<int>::iterator ind = l;
						ind++;
						while(*ind!=b[i]){
							group.pb(*ind);
							vc2[j].erase(ind);
							ind = l;
							ind++;
						}
						group.pb(b[i]);
						vc2.pb(group);
						find=true;
					}
					if (find) break;
				}
				if (find) break;
			}
		}
		

		memset(met,0,sizeof(met));
		int MX=10;
		forn(i,vc2.sz){
			MX=MIN(vc2[i].sz,MX);
		}
		while(!check(MX--));

		f2<<"Case #"<<xx<<": "<<MX+1<<endl;
		forn(i,n)
			f2<<met[i]<<' ';
		f2<<endl;
	}
	f.close();
	f2.close();
	return 0;
}