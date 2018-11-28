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
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	REP(it,tc){
		int k;
		scanf("%d\n",&k);
		string s;
		getline(cin,s);
		string st=s;
		vector<int> a;
		REP(i,k) a.PB(i);
		bool fl=true;
		int best=10000;
		int q=s.length();
		while (fl){
			REP(i,q/k){
				REP(j,k){
					st[k*i+j]=s[k*i+a[j]];
				}
			}
			int count=1;
			FOR(i,1,q) if (st[i]!=st[i-1]) count++;
			best=min(best,count);
			fl=next_permutation(ALL(a));
		}
		printf("Case #%d: %d\n",it+1,best);
	}
}