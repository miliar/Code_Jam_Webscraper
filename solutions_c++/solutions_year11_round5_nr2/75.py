#pragma comment(linker, "/STACK:65777216")

#include <algorithm>
#include <iostream>
#include <string>
#include<sstream>
#include<string.h>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include<stack>
#include <set>
#include <map>
#include<ctime>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef unsigned long long ull;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back

int a[11111];
int b[11111];
int c[11111];
int n;

bool can(int x){
	memcpy(c,a,sizeof a);

	CL(b,0);
	REP(i,10001)if(c[i]){
		int need = c[i] - b[i];
		need = max(need, 0);

		REP(j,x){
			c[i+j] -= need;
			b[i+j] = min(b[i+j], c[i+j]);
			if(c[i+j]<0) return 0;
		}
		b[i+x] += need;
		b[i+x] = min(b[i+x],c[i+x]);


		int poss = b[i];
		b[i+1] +=poss;
		b[i+1] = min(b[i+1],c[i+1]);
	}
	return 1;
}

int main(){ 
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tc;
	cin>>tc;
	REP(TC,tc){
		cin>>n;
		CL(a,0);
		REP(i,n){
			int x;
			cin>>x;
			a[x]++;
		}

		int best = 0;
		int beg = 1;
		int end = n;

		while(beg<=end){
			int s = (beg+end)/2;
			if(can(s))  best = s, beg = s +1;
			else end = s - 1;
		}


		printf("Case #%d: %d\n",TC+1,best);

	}
#ifdef LocalHost
	//cout<<endl<<endl<<"TIME: "<<clock()<<endl;
#endif
	return 0;
}
