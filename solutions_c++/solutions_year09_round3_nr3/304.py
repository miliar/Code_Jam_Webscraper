#include <stdio.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define debug 0
#define dprintf debug&&printf

void test() {
	int P,Q;
	vector<int> rel;	
	scanf("%d %d",&P,&Q);
	for(int i=0;i<Q;i++){
		int tal;
		scanf("%d",&tal);
		rel.push_back(tal-1);
	}

	int bestAns = 1<<30;
	do{
		int slappt[12345];	
		for(int i=0;i<P;i++){
			slappt[i]=0;
		}
		int ans = 0;
		for(int i=0;i<Q;i++){
			int slapp = rel[i];
			int addlo=0;
			for(int j=slapp-1;j>=0 && !slappt[j];j--){
				addlo++;
			}
			int addhi=0;
			for(int j=slapp+1;j<P && !slappt[j];j++){
				addhi++;
			}
			dprintf("%d %d %d\n",addlo, addhi, addlo+addhi);
			ans += addhi + addlo;
			slappt[slapp] = 1;
		}
		if(ans<bestAns) {
			bestAns = ans;
		}
	}while(next_permutation(rel.begin(), rel.end()));
	printf("%d\n", bestAns);
}

int main(){
	int N;
	scanf("%d\n", &N);
	for(int fall=0;fall<N;fall++){	
		printf("Case #%d: ", fall+1);
		test();
	}
	return 0;
}
