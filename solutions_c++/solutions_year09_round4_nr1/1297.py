#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

#define REP(var, n) for(int var = 0; var < (n); ++var )
#define REPd(var, n) for(int var = (n)-1; var >= 0; --var )
#define PERM(st, en) while(next_permutation((st), (en))) 
#define LOOP(var, st, en) for(int var = (st); var < (en); ++var )

using namespace std;

int main(void)
{
    int T;
    cin >> T;



    REP(i,T){
	int N;
	int array[40];
	int array2[40];
	cin >> N;
	REP(j,N){
	    int last = 0;
	    int temp;
	    REP(k,N){
		scanf("%1d", &temp);
		if(temp == 1) last = k;
	    }
	    array[j] = last - j;
	    array2[j] = j;
	}

	int minc = 100000000;
	do{
	    int c = 0;
	    int last = 0;
	    REP(j,N){
		if(array[array2[j]] + (array2[j] - j) > 0){
		    break;
		}
		
		LOOP(k,j,N){
		    if( array2[j] > array2[k] )
			c++;
		}
		
		if( j == N-1){
		    if(minc > c) minc = c;
		}
	    }
	}PERM(array2, array2+N);

	printf("Case #%d: %d\n", i+1, minc);
    }
} 
