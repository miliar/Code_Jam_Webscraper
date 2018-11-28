#include <stdio.h>
#include <vector>
#include <iostream>
using namespace std;

#define x first
#define y second
#define all(x) (x).begin() , (x).end()
typedef pair<int,int> par;

int main() {
	int n;
	scanf("%d",&n);
	for (int i=1;i<=n;i++) {
		int t,na,nb;
		scanf("%d",&t);
		scanf("%d %d",&na,&nb);
		int A[24*60+200]={};
		int B[24*60+200]={};
		vector< par > ta,tb;
		for (int k=0;k<na;k++) {
			int a,b,c,d;
			scanf("%d:%d %d:%d\n",&a,&b,&c,&d);
			ta.push_back(par(a*60+b,c*60+d));
		}
		for (int k=0;k<nb;k++) {
			int a,b,c,d;
			scanf("%d:%d %d:%d\n",&a,&b,&c,&d);
			tb.push_back(par(a*60+b,c*60+d));
		}
		sort(all(ta));
		sort(all(tb));
		int TrainA=0,TrainB=0;
		while (na+nb) {
			if (na && nb) {
				if (ta[0].x<=tb[0].x) {
					int k=ta[0].x;
					while (k>=0 && A[k]==0)
						k--;
					if (k>=0) A[k]--;
					else      TrainA++;
					B[ta[0].y+t]++;
					na--;
					ta.erase(ta.begin());
				}
				else {
					int k=tb[0].x;
					while (k>=0 && B[k]==0)
						k--;
					if (k>=0) B[k]--;
					else      TrainB++;
					A[tb[0].y+t]++;
					nb--;
					tb.erase(tb.begin());
				}
			}
			if (na) {
				int k=ta[0].x;
				while (k>=0 && A[k]==0)
					k--;
				if (k>=0) A[k]--;
				else      TrainA++;
				B[ta[0].y+t]++;
				na--;
				ta.erase(ta.begin());
			}
			if (nb) {
				int k=tb[0].x;
				while (k>=0 && B[k]==0)
					k--;
				if (k>=0) B[k]--;
				else      TrainB++;
				A[tb[0].y+t]++;
				nb--;
				tb.erase(tb.begin());
			}
		}
		printf("Case #%d: %d %d\n",i,TrainA,TrainB);
	}
	return 0;
}

