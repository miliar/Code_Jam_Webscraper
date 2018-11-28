#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

#define sz			size()
#define lgt			length()
#define forn(i,n)	for(int i=0; i<n; i++)
#define forv(i,v)	forn(i,int(v.sz))
#define forl(i,s)	forn(i,int(s.lgt))
#define II(n)		forn(i,n)
#define JJ(n)		forn(j,n)
#define KK(n)		forn(k,n)
#define IV(v)		forv(i,v)
#define JV(v)		forv(j,v)
#define KV(v)		forv(k,v)
#define IL(s)		forl(i,s)
#define JL(s)		forl(j,s)
#define KL(s)		forl(k,s)
#define SSR(i,k)	substr(i,k);
#define ALL(X)		(X).begin(),(X).end()
#define RALL(X)		(X).rbegin(),(X).rend()
#define pb			push_back
#define SORT(a)		sort(ALL(a));
#define RSORT(a)	sort(RALL(a));
#define INS			insert
#define SIT			set<int>::iterator
#define MP			make_pair
#define dump(x)		cerr<<#x<<" = "<<(x)<<endl;
#define debug(x)	cerr<<#x<<" = "<<(x)<<" (L"<< __LINE__ <<")"<<" "<< __FILE__ <<endl;
#define inint(x)	scanf("%d",&(x));

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector< vector<int> > vvi;
typedef pair<int,int> pint;
typedef vector< pair<int,int> > vpi;
typedef priority_queue<int,vector<int>,greater<int> > pque;
typedef priority_queue<int> qque;

inline int toInt(string s){int v;istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
template<class T> inline T sqr(T x) {return x*x;}
vs form(string a,char s){vs v;string b;IL(a){if(a[i]==s){v.pb(b);b="";}else b+=a[i];}v.pb(b);return v;}

const double EPS=1e-10,PI=acos(-1.0);
const int INF=2100000000;

vector <string> combine,opposed;

int main(void){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	forn(cas,t){
		int c,d;
		string in,str;
		char res[256];
		int num=0;
		combine.clear();
		opposed.clear();
		cin>>c;
		forn(i,c){
			cin>>in;
			combine.pb(in);
		}
		cin>>d;
		forn(i,d){
			cin>>in;
			opposed.pb(in);
		}
		int strnum;
		cin>>strnum;
		cin>>str;
		forn(i,strnum){
			res[num]=str[i];num++;
			bool flag=true;
			while(flag){
				flag=false;
				forv(j,combine){
					if(combine[j][0]==res[num-1]&&combine[j][1]==res[num-2])
						{res[num-2]=combine[j][2];num--;flag=true;}
					if(combine[j][1]==res[num-1]&&combine[j][0]==res[num-2])
						{res[num-2]=combine[j][2];num--;flag=true;}
				}
			}
			forn(k,num-1){
				forv(j,opposed){
					if(opposed[j][0]==res[num-1]&&opposed[j][1]==res[k])
						{num=0;break;}
					if(opposed[j][1]==res[num-1]&&opposed[j][0]==res[k])
						{num=0;break;}
				}
			}
		}
		
		printf("Case #%d: [",cas+1);
		forn(i,num){
			printf("%c",res[i]);
			if(i!=num-1)printf(", ");
		}
		printf("]\n");
	}
	
	return 0;
}
