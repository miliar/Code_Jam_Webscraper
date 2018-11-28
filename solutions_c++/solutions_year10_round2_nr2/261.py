#include <iostream>
#include <set>
#include <string>
#include <cstring>
using namespace std;

int main(){
//	FILE *fin = stdin;
//	FILE *fout = stdout;
 	FILE *fin = fopen("B-large.in","r");
 	FILE *fout = fopen("RoundBB.out","w");

	int t,tt,m,n,i,j;
	fscanf(fin,"%d",&t);
	tt = 0;
	while(t--){
		tt++;
		int ans;
		int N,K,B,T;
		int xa[55],va[55];
		double ta[55];
		fscanf(fin,"%d %d %d %d",&N,&K,&B,&T);
		for(i = 0; i < N; i++)
			fscanf(fin,"%d",xa+i);
		for(i = 0; i < N; i++)
			fscanf(fin,"%d",va+i);

		for(i = 0; i < N; i++)
			ta[i] = (double(B-xa[i]))/double(va[i]);

		ans = 0;
		int count = 0;
		int count2 = 0;

		for(i = N-1; i>=0; i--){
			if(ta[i] > T)count ++;
			else{
				count2++;
				ans+=count;
			}
			if(count2 >= K)break;
		}

		if(count2 < K)
			fprintf(fout,"Case #%d: IMPOSSIBLE\n",tt,ans);
		else
			fprintf(fout,"Case #%d: %d\n",tt,ans);

	}


	return 0;
}