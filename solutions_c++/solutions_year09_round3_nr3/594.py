#include <iostream>
#include <fstream>

using namespace std;

int main() {
	
	//freopen("C.in","r",stdin);
	
	int t,T,P,Q,res,coins,i,j,k,cur;
	int pos[100];
	int pri[100];
	int el[100];
	
	scanf("%d",&T);
	
	for (t = 1; t <= T; ++t) {
		
		memset(pos,0,sizeof(pos));
		memset(pri,0,sizeof(pri));
		memset(el,0,sizeof(el));
		
		scanf("%d%d",&P,&Q);
		for (i = 0 ; i < Q; ++i) scanf("%d",&el[i]);
		for (i = 0 ; i < Q; ++i) pos[i] = i + 1;
		
		res = -1;
		
		do {
			coins = 0;
			memset(pri,0,sizeof(pri));
			for (i = 1; i <= Q; ++i) {

				for (j = 0;j < Q; ++j) 
					if (pos[j] == i) {
					cur = j;
					break;
				}
				
				pri[el[j] - 1] = 1;
				
				k = el[j] - 2;
				while ((pri[k] == 0) && (k >= 0)) {
					coins++;
					k--;
				}
				
				k = el[j];
				while ((pri[k] == 0) && (k < P)) {
					coins++;
					k++;
				}
				
			}
			if ((coins < res) || (res == -1)) res = coins;
		} while (next_permutation(pos,pos + Q));
		
		printf("Case #%d: %d\n",t,res);
	}
	
}