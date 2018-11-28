#include<cstdio>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include <list>
#include<queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iterator>

using namespace std;

int main() {
	int N,k,L;
	char S[1005],SS[1005];
	scanf("%d\n",&N);
	for(int ii=1;ii<=N;++ii) {
		int mm = 1005;
		scanf("%d\n%s\n",&k,S);
		L = strlen(S);
		int a[] = {0,1,2,3,4,5};
		do {
			for(int i=0;i<L/k;++i) for(int j=0;j<k;++j) SS[i*k+j] = S[i*k + a[j]]; 
			int mx = 0;
			for(int i=0;i < L;) {
				int j = i;
				while(j < L &&  SS[i] == SS[j]) j++;
				mx++;
				i = j;
			}
			mm = (mm > mx) ? mx:mm;
		//}while(next_permutation(a.begin(),a.end()));
		}while(next_permutation(a,a+k));
		printf("Case #%d: %d\n",ii,mm);
	}
	return 0;
}
