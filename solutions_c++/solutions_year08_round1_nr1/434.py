#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <stdio.h>

using namespace std;

#define LL long long

int N;
int angka[1000];
int angka2[1000];
bool used[1000];
bool used2[1000];
priority_queue<int> pos1, pos2, neg1, neg2;




int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	LL INF=(LL)100000*100000+100000;
	int t,T;
	int i,j;
	scanf("%d", &T);
	for (t=1; t<=T; t++) {
		scanf("%d", &N);
		memset(used,0,sizeof(used));
		memset(used2,0,sizeof(used2));
		for (i=0; i<N; i++) {
			scanf("%d", &angka[i]);
		}
		for (i=0; i<N; i++) {
			scanf("%d", &angka2[i]);
		}
		int k=N;
		LL ans=0;
		while (k>0) {
			LL minres=INF;
			int id1,id2;
			for (i=0; i<N; i++) {
				if (used[i]) continue;
				for (j=0; j<N; j++) {
					if (used2[j]) continue;
					LL res=(LL)angka[i]*angka2[j];
					if (res<minres || res==minres && abs(angka[id1]+angka2[id2])<abs(angka[i]+angka2[j])) {
						minres=res;
						id1=i;
						id2=j;
					}
				}
			}
			if (minres>0) break;
			used[id1]=true;
			used2[id2]=true;
			k--;
			ans+=minres;
		}
		vector<int> gg;
		vector<int> gg2;
		for (i=0; i<N; i++) {
			if (!used[i]) gg.push_back(angka[i]);
			if (!used2[i]) gg2.push_back(angka2[i]);
		}
		sort(gg.begin(),gg.end());
		sort(gg2.begin(),gg2.end());
		for (i=0; i<gg.size(); i++) {
			ans+=(LL)gg[i]*gg2[gg.size()-1-i];
		}
		printf("Case #%d: %I64d\n",t,ans);
	}
	return 0;
}