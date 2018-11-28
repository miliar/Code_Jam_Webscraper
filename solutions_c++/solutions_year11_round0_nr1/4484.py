#include <cstdio>
#include <vector>
#include <set>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	int t,n,a,lo,lb,o,b,time;
	char c;
	scanf("%d",&t);
	for (int i=1; i<=t; i++) {
		scanf("%d",&n);
		vector<int> O,B;
		vector<bool> order;
		lo=1; lb=1;
		for (int j=0; j<n; j++) {
			scanf(" %c %d",&c,&a);
			if (c=='O') {
				O.push_back(abs(a-lo));
				lo=a;
				order.push_back(0);
			} else {
				B.push_back(abs(a-lb));
				lb=a;
				order.push_back(1);
			}
		}
		o=0; b=0;
		time=0;
		for (int j=0; j<order.size(); j++) {
			 if (order[j]) {
				 B[b]-=time;
				 if (B[b]<0) B[b]=0;
				 time+=B[b]+1;
				 b++;
				 if (b<B.size()) B[b]+=time;
			 } else {
				 O[o]-=time;
				 if (O[o]<0) O[o]=0;
				 time+=O[o]+1;
				 o++;
				 if (o<O.size()) O[o]+=time;
			 }
		}
		printf("Case #%d: %d\n",i,time);
	}

}