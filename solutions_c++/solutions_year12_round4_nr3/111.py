#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<vector>
#define REP(i,m) for(int i=0;i<m;++i)
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define dump(x)  cerr << #x << " = " << (x) << endl
#define prl cerr<<"called:"<< __LINE__<<endl
using namespace std;
static const int INF =1e9+5; 
template<class T> void debug(T a,T b){ for(;a!=b;++a) cerr<<*a<<' ';cerr<<endl;}
typedef long long int lint;
typedef pair<int,int> pi;
int highest[2005];
int n;
int tall[2005];
lint div(lint a,int b){
	if(a>=0){
		if(a%b==0) return a/b-1;
		else return a/b;
	}else{
		return a/b-1;
	}
}
lint div2(lint a,int b){
	if(a>=0){
		if(a%b==0) return a/b;
		return a/b+1;
	}else{
		return a/b+1;
	}
}
int main(){
	int t;scanf("%d",&t);
	REP(setn,t){
		printf("Case #%d:",setn+1);
		scanf("%d",&n);
		REP(i,n-1) scanf("%d",&highest[i]),--highest[i];
		int fail=0;
		REP(i,n) REP(j,i) if(i<highest[j] && highest[j]<highest[i]) fail=1;
		if(fail){
			puts(" Impossible");
			continue;
		}

		REP(i,n) tall[i]=1000000000;
		bool flag=true;
		while(flag){
			flag=false;
			REP(i,n-1){
				int to=highest[i],dst=to-i;
				for(int j=i+1;j<to;++j){
					lint v=div((tall[to]-tall[i])*(lint)(j-i),dst)+tall[i];
					if(tall[j]>v){
						tall[j]=v;
						flag=true;
					}
				}
				for(int j=to+1;j<n;++j){
					lint v=tall[j]-div2((tall[j]-tall[to])*(j-i),(j-to));
					if(tall[i]>v){
						tall[i]=v;
						flag=true;
					}
				}
			}
		}
		REP(i,n) printf(" %d",tall[i]);
		putchar('\n');
	}


	return 0;
}



