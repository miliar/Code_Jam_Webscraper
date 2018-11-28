#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define FOR(i,a,b) for (int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for (int i=(a),_b=(b); i>=_b; i--)
#define REP(i,n) for (int i=0,_n=(n); i<_n; i++)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)
#define FOREACHD(it,arr) for (__typeof((arr).rbegin()) it=(arr).rbegin(); it!=(arr).rend(); it++)

char s[1000];
int nTC, len;
long long cnt;

void rec(int idx, long long sum){
	if (idx==len){
		if (sum%2 == 0 || sum%3==0 || sum%5==0 || sum%7==0) cnt++;
		return;
	}

	long long num = 0;
	FOR(i,idx,len-1){
		num = num*10 + s[i]-'0';
		rec(i+1,sum+num);
		if (idx>0) rec(i+1,sum-num);
	}
}

int main(){
	sscanf(gets(s),"%d",&nTC);
	FOR(TC,1,nTC){
		len = strlen(gets(s));
		cnt = 0;
		rec(0,0);
		printf("Case #%d: %lld\n",TC,cnt);
	}
}
