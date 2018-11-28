#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>

using namespace std;

typedef pair<int, int> PII;

typedef vector<int> VI;
typedef vector<vector<int> > VII;
typedef vector<PII> VPII;

typedef vector<double> VD;
typedef vector<string> VS;

typedef long long LL;

int min(int a, int b){
	return a < b ? a : b;
}

int main(){ 	
	int cases;
	scanf("%d\n", &cases);
	
	for(int caseNr = 1; caseNr <= cases; caseNr++){
		// go for it!	
		printf("Case #%d: ", caseNr);
		
		int R, C, D;
		scanf("%d %d %d\n", &R, &C, &D);
		//printf("%d %d %d\n", R, C, D);
		
		int arr[R][C];
		
		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++){
				char c;
				scanf("%c", &c);
				arr[i][j] = c - 48 + D;
			}
			scanf("\n");
		}
		
		int bestSZ = -1;
		
		for(int bs=3;bs<=min(R,C);bs++){
			//fprintf(stderr, "BS=%d\n", bs);
		
			for(int t=0;t<R-bs+1;t++){
				for(int l=0;l<C-bs+1;l++){
					// CHECK
					int ct = 2*t + (bs-1);
					int cl = 2*l + (bs-1);
					
					//fprintf(stderr,"t=%d l=%d ct=%d cl=%d (ct,cl)=%d\n", t,l,ct,cl,arr[ct][cl]-D);
					//fprintf(stderr,"t=%d l=%d ct=%d cl=%d \n", t,l,ct,cl);
					
					long long massX = 0;
					long long massY = 0;
					
					
					for(int j=t;j<t+bs;j++){
						for(int i=l;i<l+bs;i++){
							if(j==t && i==l)
								continue;
							if(j==t && i==l+bs-1)
								continue;
							if(j==t+bs-1 && i==l)
								continue;
							if(j==t+bs-1 && i==l+bs-1)
								continue;
							massY += arr[i][j] * (2*j - ct);
							massX += arr[i][j] * (2*i - cl);
						}
					}
					
					if(massX == 0 && massY == 0){
						//fprintf(stderr, "MASS=0 %d,%d\n", ct, cl);
						bestSZ = bs;
					}
				}
			}
		}
		
		if(bestSZ>0)
			printf("%d\n", bestSZ);
		else
			printf("IMPOSSIBLE\n");
		
		fflush(stdout);
	}
	
	return 0;
}
