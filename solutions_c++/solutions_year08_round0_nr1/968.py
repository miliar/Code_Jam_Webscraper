
#include<algorithm>
#include<bitset>
#include<iostream>
#include<string>
#include<cstdio>
#include<sstream>
#include<vector>
#include<stack>
#include<deque>
#include<map>
#include<iterator>
#include<cmath>
#include<complex>
#include<queue>
#include <ext/hash_map>

#define FOREACH(it ,c ) for( typeof((c).begin()) it= (c).begin();it!=(c).end();++it) 
#define debug(x) cerr<< #x << " = " << x << "\n";
#define debugv(x) cerr<< #x << " = " ; FOREACH(it,(x)) cerr << *it << "," ; cerr<< "\n" ;
#define MP make_pair
#define PB push_back
#define siz(w) (int)w.size()
#define fup(i,st,ko) for(int i=st;i<=ko;i++)
#define fdo(i,st,ko) for(int i=st;i>=ko;i--)
#define REP(i,w) for(int i=0;i<siz(w);i++)
#define inf 100000000
typedef long long ll;
using namespace std;

map<string,int> names;
int best[1005][105];
int t[1005];
string jakis;
int main(){
int cas;cin>>cas;
getline(cin,jakis);
fup(i,1,cas){
	int przypadek= i;
	int ile; cin>>ile;
	getline(cin,jakis);
	names.clear();
	fup(i,1,ile){
		string s; 
		getline(cin,s);
		names[s]= i;
	}
	int M;
	cin>>M;
	getline(cin,jakis);
	fup(i,1,M){
		string s; 
		getline(cin,s);
		t[i]= names[s];
	}
	fup(i,1,M){
		fup(j,1,ile){
			best[i][j]=inf;
		}
	}

	fup(i,1,M){
		fup(j,1,ile){
			if(j==t[i])continue;
			fup(k,1,ile){
				best[i][j]=min(best[i][j],best[i-1][k]+ (j!=k));
			}
		}
	}	
	int bb= inf;
	fup(i,1,ile){
		bb=min(bb,best[M][i]);
	}

	cout<<"Case #"<<przypadek<<": "<<bb<<endl;
}

return 0;
}
