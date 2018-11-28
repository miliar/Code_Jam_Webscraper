#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

#define FOR(i,a,b) for (int i = (int)a; i < (int)b; ++i)
#define REP(i,a) FOR(i,0,a)
#define ALL(a) a.begin(),a.end()
#define SIZE(a) (int)((a).size())
#define PB push_back
#define FILL(a) memset(&a,0,sizeof(a))
typedef long long LL;

using namespace std;

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	REP(it,tc){
		int k,n;
		scanf("%d%d",&k,&n);
		int ind[100];
		REP(i,n) scanf("%d",&ind[i]);
		int next[5000];
		REP(i,k)
			next[i]=i+1;
		next[k-1]=0;
		int res[5000],cur=0;
		int last=k-1;
		REP(i,k){
			int sch=(i%(k-i));
			while (sch){
				last=cur;
				cur=next[cur];
				--sch;
			}
			res[cur]=i+1;
			next[last]=next[cur];
			cur=next[cur];
		}
		printf("Case #%d:",it+1);
		REP(i,n) printf(" %d",res[ind[i]-1]);
		puts("");
	}
}