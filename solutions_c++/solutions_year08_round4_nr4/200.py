#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<queue>
using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define SIZE 1005

char s[SIZE];

int calc(string & s) {
	int r=0;
	int i,j;
	for(i=0;i<(int)s.size();i++) {
		for(j=i;j<(int)s.size();j++) {
			if(s[i] != s[j]) break;
		}
		i = j - 1;
		r++;
	}
	return r;
}

int main() {
	int T,K;
	int i,j;
	vector<int>v;
	int res,cur,kase=1;
	string str;
	int L;
	scanf("%d",&T);
	while(T--) {
		scanf(" %d",&K);
		scanf(" %s",s);
		res = 1000000;
		L = strlen(s);

		v.clear();
		rep(i,K) v.push_back(i);

		do {
			cur = 0;
			str = "";
			for(i=0;i<L;i+=K) {
				rep(j,K) {
					str += s[i + v[j]];
				}
			}
			cur = calc(str);

			res = min(res,cur);

		}while(next_permutation(v.begin(),v.end()));

		printf("Case #%d: %d\n",kase++,res);
	}
	return 0;
}