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
#define PB push_back
#define FILL(a) memset(&a,0,sizeof(a))
typedef long long LL;

using namespace std;

string eng[100];
int n,m;

int getnom(string s){
	REP(i,n)
		if (eng[i]==s) return i;
	return -1;
}

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	REP(it,tc){
		scanf("%d\n",&n);
		REP(i,n) getline(cin,eng[i]);
		scanf("%d\n",&m);
		int a[1000];
		REP(i,m){
			string s;
			getline(cin,s);
			a[i]=getnom(s);
		}
		int old[100],nw[100];
		FILL(old);
		REP(i,m){
			if (a[i]!=-1){
				REP(j,n){
					if (j!=a[i]) nw[j]=old[j];
					else{
						nw[j]=1<<20;
						REP(i2,n){
							if (i2!=a[i]) nw[j]=min(nw[j],old[i2]+1);
						}
					}
				}
				REP(j,n) old[j]=nw[j];
			}
		}
		int res=1<<20;
		REP(i,n) res=min(res,old[i]);
		printf("Case #%d: %d\n",it+1,res);
	}
}