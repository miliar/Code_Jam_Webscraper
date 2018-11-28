#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <string>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PI;

#define PB push_back
#define MP(a,b) make_pair(a,b)
#define FT first
#define SD second
#define INF 2000000000

int n,s,p;
int sumy[200];

int main() {
	int t;scanf("%d",&t);
	for(int d=1;d<=t;d++) {
		scanf("%d%d%d",&n,&s,&p);
		for(int i=0;i<n;i++) {
			scanf("%d",&sumy[i]);
		}
		int duze = 0, male = 0;
		int wyn;
		if(p == 0) {
			wyn = n;
		}
		else {
			for(int i=0;i<n;i++) {
				if(sumy[i] >= p*3-2) duze++;
				else if(sumy[i] >= (p == 1 ? 1 : p*3-4)) male++;
			}
			wyn = duze + min(male,s);
		}
		printf("Case #%d: %d\n", d, wyn);
	}


	return 0;
}