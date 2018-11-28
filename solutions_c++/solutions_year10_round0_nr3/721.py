#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;
int P[1005], A[1005];
long long S[1005];
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		memset(S,-1,sizeof(S));
		int R,K,N;
		scanf("%d%d%d",&R,&K,&N);
		queue<int> Q;
		for(int i=0;i<N;++i) {
			scanf("%d",&A[i]);
			Q.push(i);
		}
		long long nppl = 0;
		bool flag = 0;
		S[0] = P[0] = 0;
		for(int ri=1;ri<=R;++ri) {
			int sum = 0;
			for(int i=0;i<N;++i) {
				int st = Q.front();
				if(sum+A[st] > K) break;
				sum += A[st];
				Q.pop();
				Q.push(st);
			}
			nppl += sum;
			int cs = Q.front();
			if(!flag) {
				if(S[cs] != -1) {
					int turns = ri-P[cs];
					long long ppl = nppl-S[cs];
					int grps = (R-ri)/(ri-P[cs]);
					nppl += ppl*grps;
					ri += grps*turns;
					flag = 1;
				}
				P[cs] = ri;
				S[cs] = nppl;
			}
		}
		printf("Case #%d: ",cn);
		cout << nppl << endl;
	}
}
