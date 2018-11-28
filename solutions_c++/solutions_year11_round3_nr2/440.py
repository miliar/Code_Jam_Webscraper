#include <iostream>
#include <cstdio>

using namespace std;

int findDistance(int tBld, int N, int C, int * dists, int L1, int L2);

int main(){
	int nCases, iCases;
	cin >> nCases;
	
	for (iCases=1; iCases<=nCases; iCases++){
		fprintf(stderr, "%d\n", iCases);
		int L, tBld, N, C;
		scanf("%d %d %d %d", &L, &tBld, &N, &C);
		
		int dists[C];
		
		int i, j;
		for (i=0; i<C; i++){
			scanf("%d", dists+i);
		}
		
		int t, min=1000000000LL;
		if (L==0){
			t=findDistance (tBld, N, C, dists, -1, -1);
			if (t<min)
				min=t;
		} 
		else if (L==1){
			for (j=0; j<N; j++){
				t=findDistance (tBld, N, C, dists, j, -1);
				if (t<min)
					min=t;
			}
		}
		else{				
			for (i=0; i<N; i++){
				for (j=i+1; j<N; j++){
					t=findDistance (tBld, N, C, dists, i, j);
					if (t<min)
						min=t;
				}
			}
		}
		
		printf("Case #%d: ", iCases);
		printf("%d\n", min);
	}
	
	return 0;
}

int findDistance(int tBld, int N, int C, int * dists, int L1, int L2){
	int i;
	
	double t=0, t2;
	for (i=0; i<N; i++){
		if (i==L1 or i==L2){
			t2 = tBld-t;
			if (t2<=0)
				t += dists[i%C];
			else if (t2>dists[i%C]*2){
				t += dists[i%C]*2;
			}
			else {
				t += t2 + (dists[i%C]-t2/2);
			}
		}
		else
			t += dists[i%C]*2;
	}
	return int(t+0.5);
}
