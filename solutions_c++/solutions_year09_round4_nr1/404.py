#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<sstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;

#define LET(x,a) 	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	IFOR(it,v.begin(),v.end())
#define FOR(i,a,b)  	for(int i=(int)(a) ; i < (int)(b);++i)
#define REP(i,n) 	FOR(i,0,n)
#define PB		push_back
#define MP 		make_pair
#define EPS		1e-9
#define INF 2000000000

typedef vector<int>	VI;
typedef long long	LL;
typedef pair<int,int>	PI;

vector<VI> v;

int main(){
	int t;cin>>t;
	FOR(cas,1,t+1){
		cout<<"Case #"<<cas<<": ";
		int n;cin>>n;
		v.clear();
		REP(i,n){
			char ch;
			VI tmp;
			tmp.resize(n);
			REP(j,n){
				scanf(" %c",&ch);
				tmp[j]=(int)(ch-'0');	
			}
			v.PB(tmp);
		}
		int ans=0;
		REP(i,n){
			int index=-1;
			FOR(j,i,n){
				bool poss=1;
				FOR(k,i+1,n)if(v[j][k]){
					poss=0;
					break;
				}
				if(poss){
					index=j;
					break;
				}
			}
			for(int j=index;j>i;j--){
				swap(v[j],v[j-1]);
			}
			ans+=(index-i);
		}
		cout<<ans<<endl;
	}
	return 0;
}
