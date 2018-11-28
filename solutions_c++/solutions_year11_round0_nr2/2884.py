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
char c[26][26];
bool c2[26][26];
char s[4];
int C,D,N;
list<int> lst;
int met[26];
char ST[105];
int CASE=1;
int main(){
	ifstream f("input.txt");
	ofstream f2("output.txt");
	f>>t;
	forn(xx,t){
		memset(c,0,sizeof(c));
		memset(c2,0,sizeof(c2));
		f>>C;
		
		forn(i,C){
			f>>s;
			c[s[0]-'A'][s[1]-'A']=s[2]-'A';
			c[s[1]-'A'][s[0]-'A']=s[2]-'A';
		}
		f>>D;
		forn(i,D){
			f>>s;
			c2[s[0]-'A'][s[1]-'A']=true;
			c2[s[1]-'A'][s[0]-'A']=true;
		}
		f>>N;
		lst.clear();
		memset(met,0,sizeof(met));
		f>>ST;
		forn(i,N){
			if (lst.sz){
				int elem=ST[i]-'A';
				bool BB=false;
				while (c[*lst.rbegin()][elem]){
					elem=c[*lst.rbegin()][elem];
					met[*lst.rbegin()]--;
					lst.pop_back();
					BB=true;
					if (lst.sz==0) break;
				}
				if (BB) {
					met[elem]++;
					lst.pb(elem);
					continue;
				}
				forn(i,26){
					if (met[i]){
						if (c2[i][elem]){
							memset(met,0,sizeof(met));
							lst.clear();
							BB=true;
							break;
						}
					}
				}
				if (!BB){
					lst.pb(elem);
					met[elem]++;
				}
			} else{
				int elem=ST[i]-'A';
				lst.pb(elem);
				met[elem]++;
			}
		}
		f2<<"Case #"<<CASE++<<": [";
		list<int>::iterator it1=lst.begin();
		if (lst.begin()!=lst.end()){
			f2<<(char)(*lst.begin()+'A');
			it1++;
		}
		while(it1!=lst.end()){
			f2<<", "<<(char)(*it1+'A');
			it1++;
		}
		f2<<']'<<endl;
	}
	f2.close();
	f.close();
	return 0;
}