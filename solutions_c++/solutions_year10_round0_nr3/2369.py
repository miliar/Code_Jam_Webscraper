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
#include<cstdio>


using namespace std;


typedef vector<int> vi;
typedef vector< vector<int> > vii;
typedef long long LL;
typedef vector<string> vs;

#define fo(i, j) for(i= 0; i < j ; i++)
#define clr(x, n) memset(x, n, sizeof(x))

void main(void){ // main start

	FILE *p, *fp;

	
	p=fopen("C-small-attempt2.in","r");
	fp=fopen("C-small-attempt2.out","w");

	int T, i=0;
	

	fscanf_s(p, "%d",&T);
	assert(1<=T && T <= 50);

	while(i < T){
			
		int R, K, N, j=1, k=0;
		int money=0;
		int tmp;
		int group[11];
		queue<int> Q;

		fscanf_s(p,"%d %d %d", &R, &K, &N);

		assert(1<=N && N <= 10 && 1<=K && K <=100 & 1<=R && R<=1000);
		
		
		while(j < N + 1 ){
			
			fscanf_s(p,"%d",&group[j]);
			assert(1<=group[j] && group[j] <=10);
			Q.push(group[j]);
			j++;
		}

		while(k	< R){
			
			tmp=K;

			int tem;
			int count=1;
			
			while(tmp - Q.front() >= 0 && count <= N ){
				
				tmp-=Q.front();
				tem=Q.front();
				Q.pop();
				Q.push(tem);
				money+=tem;
			count++;
			}
			k++;
		}
		cout << money << endl;
		fprintf(fp,"Case #%d: %d\n",i+1,money);
		i++;
	}
	
} // main end