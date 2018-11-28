#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int t;scanf(" %d",&t);t;})
#define GC(x) scanf(" %c",&x)
#define sz size()
#define rz resize
#define inf (int)1e9
#define pb push_back
#define bs binary_search
#define lb lower_bound
#define ub upper_bound

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef double DD;
typedef long long LL;

int N,test[42],tp[42];

int main() {
	char c;
	int t,temp,cnt,yo=0;
	for(int _=GI;_--;) {
		N=GI;
		REP (i,N) {
			t=0;
			REP (j,N) {
				GC(c);
				if(c=='1') t=j+1;
			}
			test[i]=t;
		}
//		REP (i,N) tp[i]=test[i];
//		sort(tp,tp+N);
		cnt=0;
		REP (i,N) {
			if(test[i]>i+1) {
				FOR (j,i+1,N) if(test[j]<=i+1) {t=j; break;}
//				cout<<i<<" "<<t<<endl;
				cnt+=(t-i);
				temp=test[t];
				for (int k=t;k>=i+1;k--) test[k]=test[k-1];
				test[i]=temp;
//				REP (k,N) cout<<test[k]<<" ";
//				cout<<endl;
			}
		}
		cout<<"Case #"<<++yo<<": "<<cnt<<endl;
	}
	return 0;
}

