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

LL price[1000][1000];
VI graph[1000];
vector<PI> tmp;
int degree[10000];
int color[10000],cnt;

int main(){
	int t;
	cin>>t;
	int cas=0;
	while(t--){
		cas++;
		cout<<"Case #"<<cas<<": "; 
		int n,k;
		cin>>n>>k;
		REP(i,n)graph[i].clear();
		REP(i,n){
			REP(j,k)cin>>price[i][j];
		}
		memset(degree,0,sizeof(degree));
		memset(color,-1,sizeof(color));
		cnt=0;
		tmp.clear();
		REP(i,n){
			FOR(j,i+1,n){
				bool poss=0;
			
				FOR(l,1,k){
					if(price[i][l]==price[j][l])poss=1;
					if(price[i][l-1]==price[j][l-1])poss=1;
					if((price[i][l]-price[j][l])*(price[i][l-1]-price[j][l-1])<0)poss=1;
				}
				if(poss){
					graph[i].PB(j);
					graph[j].PB(i);
					degree[i]++;
					degree[j]++;
				}
			}
		}
		REP(i,n){
			tmp.PB(MP(degree[i],i));
		}
		sort(tmp.begin(),tmp.end());
		reverse(tmp.begin(),tmp.end());
		EACH(it,tmp){
			int ver = it->second;
			int pr[cnt+5];memset(pr,0,sizeof(pr));
			EACH(it1,graph[ver]){
				if(color[*it1]!=-1)pr[color[*it1]]=1;
			}
			int c=-1;
			REP(i,cnt)if(!pr[i]){
				c=i;
				break;
			}
			if(c==-1){
				color[ver]=cnt++;
			}
			else color[ver]=c;
		}
		cout<<cnt<<endl;
	}
}
