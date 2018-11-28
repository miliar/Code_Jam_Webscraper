#include <algorithm>
#include <bitset>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define PB push_back
#define iss istringstream
#define SZ(a) (int)a.size()
#define ALL(a) a.begin(),a.end()
#define CLEAR(a) memset(a,0,sizeof(a))
#define ll long long
#define ii pair<int,int>

ll combo[99][99];
const int MOD=1000;

int cases;
int n;

void dp(){
	REP(i,39) {
		combo[i][0]=1;
		FOR(j,1,i+1) {
			combo[i][j]=(combo[i-1][j-1]+combo[i-1][j])%MOD;
		}
	}
}

template<class T> T power(T x,int p) {
	if (p==0) {return 1;}
	if (p==1) {return x;}
	T ret=power(x,p/2);
	ret=(ret*ret)%MOD;
	if (p&1) {ret*=x;ret%=MOD;}
	return ret;
}

int main() {
	FILE * fin=fopen("C-small.in","r");
	FILE * fout=fopen("C-small.out","w");
	dp();
	fscanf(fin,"%d ",&cases);
	REP(h,cases) {
		fscanf(fin,"%d ",&n);
		ll ret=0;
		for(int i=0;i<=n;i+=2) {
			ll ans=combo[n][i];
			ans*=power(3,n-i);
			ans%=MOD;
			ans*=power(5,i/2);
			ans%=MOD;
			ret+=ans;
		}
		ret*=2;
		ret%=MOD;
		ret--;
		//printf("%lld\n",ret);
		ostringstream out;
		out << ret;
		string t=out.str();
		int s=t.size();
		
		fprintf(fout,"Case #%d: ",h+1);
		REP(j,3-s) {
			fprintf(fout,"0");
		}
		fprintf(fout,"%lld\n",ret);
	}

	return 0;
}
