#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#include<stack>
#include<queue>
#include<list>
#include<cmath>
#include<cstdlib>
#include<cassert>


using namespace std;


typedef vector<int> vi;
typedef vector< vector<int> > vii;
typedef vector<string> vs;

#define fo(i, j) for(i= 0; i < j ; i++)
#define clr(x, n) memset(x, n, sizeof(x))

void main(void){ // main start

	FILE *p, *fp;

	
	p=fopen("A-large.in","r");
	fp=fopen("A-large.out","w");
	
	int T=0, i=0;

	fscanf(p, "%d", &T);

	assert(T <=10000 && 1<=T);

	int N, K;
	
	double value;

	
	while( i<T){ 
			
		fscanf(p, "%d %d\n", &N, &K);

		assert(1<=N && N<=30 && 0<=K && K<=100000000);
		
		value = pow((double)2,(double)N);
		
		if((K - (int)value + 1)%((int)value) == 0){
			fprintf(fp, "Case #%d: ON\n", i+1);
		}

		else
			fprintf(fp, "Case #%d: OFF\n", i+1);
			
	
		i++;
	}
	


} // main end