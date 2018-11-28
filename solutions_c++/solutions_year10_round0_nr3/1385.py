//============================================================================
// Name        : codejam3.cpp
// Author      : Jani
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

#define MAXN 1000
#define BIGN 1000

struct rides {
	rides():
		num(0),
		fare(0)
		{}
	int num;
	int fare;
	int overlap;
};

int main() {

	int T;
	int G[MAXN];
	scanf("%d",&T);

	for (int i=0;i<T;++i){
		long long fare=0;
		int R,k,N;
		scanf("%d %d %d\n",&R,&k,&N);
		int k1=k;
		int sumGk=0;
		for (int j=0;j<N;++j){
			scanf("%d",&G[j]);
			k1-=G[j];
			if (k1<0){
				++sumGk;
				k1+=k;
			}
		}
//		cout << R << '/' << sumGk << ' ' << k << '/' << k1 << ' ' << N << endl;
		if (!sumGk){
			fare=(long long)(k-k1) * (long long)R;
		}else{
			vector<rides> smallrides(MAXN);
			vector<rides> bigrides(MAXN);
			int next=0;
			int k1;
			while(!smallrides[next].num){
				int j=next;
				k1=k;
				for (;j<N;++j){
					if (k1<G[j]){
						++smallrides[next].num;
						smallrides[next].fare+=k-k1;
						k1=k-G[j];
					} else {
						k1-=G[j];
					}
				}
				for (j=0;k1>=G[j];++j){
					k1-=G[j];
				}
				++smallrides[next].num;
				smallrides[next].fare+=k-k1;
				smallrides[next].overlap=j;
//				cout << "s " << next << ' ' << smallrides[next].num << "/"
//				<< smallrides[next].fare << "-" << smallrides[next].overlap << endl;
				next=smallrides[next].overlap;
			}
			int bignext=0;
			while(!bigrides[bignext].num){
				next=bignext;
				for (int j=0;j<BIGN;++j){
					bigrides[bignext].num+=smallrides[next].num;
					bigrides[bignext].fare+=smallrides[next].fare;
					next=smallrides[next].overlap;
				}
				bigrides[bignext].overlap=next;
//				cout << "b " << bignext << ' ' << bigrides[bignext].num << "/"
//				<< bigrides[bignext].fare << "-" << bigrides[bignext].overlap << endl;
				bignext=bigrides[bignext].overlap;
			}
			// let's roll
			next=0;
			int R1=R;
			while (bigrides[next].num<=R1){
				fare+=(long long)bigrides[next].fare;
				R1-=bigrides[next].num;
				next=bigrides[next].overlap;
			}
			while (smallrides[next].num<=R1){
				fare+=(long long)smallrides[next].fare;
				R1-=smallrides[next].num;
				next=smallrides[next].overlap;
			}
			while (R1 > 0){
				k1=k;
				for (;k1>=G[next];next=(next+1)%N){
					k1-=G[next];
				}
				--R1;
				fare+=(long long)(k-k1);
			}
		}
		printf("Case #%d: %ld\n",i+1,fare);
	}

	return 0;
}
