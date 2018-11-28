#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
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
#include <ctime>

#define REP(i,n) for(int i=0; i < (int)n; i++)
#define REPD(i,n) for(int i=n-1; i >= 0; i--)
#define FOR(i,a,b) for(int i= (int)a; i <= (int)b; i++)
#define FORD(i,a,b) for(int i= (int)a; i >= (int)b; i++)
#define SIZE(x) ((int)(x.size()))
#define PB push_back
#define MP make_pair

using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vii;
typedef vector<string> vs;
typedef vector< vs > vss;
typedef pair<int, int> pii;
typedef long long ll;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	//freopen("inputA.txt","r",stdin);
	//freopen("outputA.txt","w",stdout);	

	int numcases;
	scanf("%d",&numcases);
	REP(i,numcases) {
		int n,m; scanf("%d %d",&n,&m);
		char nl; scanf("%c",&nl);
		vss dir(101);
		REP(j,n) {
			char t='/'; string k="";
			int c=-1;
			scanf("%c",&t);
			while(t!='\n') {
		   	if(t=='/') {
					c++;
					if(k!="") {
						int indx=0;
						if(c >0) indx=c-1;
						dir[indx].PB(k);
					}
					k+='/';
				}
				else {
					k+=t;
				}
				scanf("%c",&t);
			}
			if(k!="") { 
				dir[c].PB(k); }
		}
		int res=0;
		REP(j,m) {
			int c=-1;
			char t='/'; string k=""; scanf("%c",&t);
			while(t!='\n') {
				if(t=='/') { 
					c++;
					if(k!="") {
						int indx=0;
						if(c>0) indx=c-1;
						vs curr=dir[indx];
						int b=1;
						REP(d,SIZE(curr)) {
							if(curr[d]==k) b=0; 
						}
						if(b==1) { 
							res++; }
						dir[indx].PB(k);
					}
					k+='/';
				}
				else {
					k+=t;
				}
				scanf("%c",&t);
		  }
			if(k!="") {
				vs curr=dir[c];
				int b=1;
				REP(d,SIZE(curr)) {
					if(curr[d]==k) b=0;
				}
				if(b==1) { 
					res++; }
				dir[c].PB(k);
			}
    }
		printf("Case #%d: ",i+1);
		printf("%d\n",res);
	}
}
