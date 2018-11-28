#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main(){
	int d, p, q;
	int t[10];
	bool c[1000];
	int cs;
	int mcs;
	int wsk;
	scanf("%d", &d);
	for(int i=1; i<=d; i++){
		scanf("%d %d", &p, &q);
		for(int j=0; j<q; j++){
			scanf("%d", &t[j]);
		}
		mcs=p*q+100;
		sort(t, t+q);
		do{
			for(int j=1; j<=p; j++) c[j]=1;
			cs=0;
			for(int j=0; j<q; j++){
				wsk=t[j]-1;
				c[t[j]]=0;
				while(wsk!=0){
					if(c[wsk]==0) break;
					cs++;
					wsk--;
				}
				wsk=t[j]+1;
				while(wsk!=p+1){
					if(c[wsk]==0) break;
					cs++;
					wsk++;
				}
			}
			if(cs<mcs) mcs=cs;
		}while(next_permutation(t, t+q));
		printf("Case #%d: %d\n", i, mcs);
	}	
	return 0;
}

