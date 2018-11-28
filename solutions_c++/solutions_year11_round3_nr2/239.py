#include<stdio.h>
#include<algorithm>

using namespace std;

__int64 dist[1000001];
__int64 res[1000001];
int L, N, C;
__int64 time;

int main(void){
	int t,T;
	int i,j;
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
	for(t=1;t<=T;t++){
		fprintf(fout,"Case #%d: ",t);
		fscanf(fin,"%d%I64d%d%d",&L,&time,&N,&C);
		for(i=0;i<C;i++){
			fscanf(fin,"%d",&dist[i]);
		}

		int c = 0;
		__int64 sum = 0;
		int cc = 0;
		for(i=0;i<N;i++){
			sum += dist[c] * 2;

			if( sum >= time ){
				res[cc++] = (sum - time) / (__int64)2;
				sum = time;
				break;
			}
			c++;
			if( c >= C ){
				c = 0;
			}
		}
		for(j=i+1;j<N;j++){
			c++;
			if( c >= C ){
				c = 0;
			}
			res[cc++] = dist[c];
		}

		sort(res, res+cc);

		for(j=cc-1;j>=0;j--){
			if( (cc-1) - j + 1 <= L ){
				sum += res[j];
			} else{
				sum += res[j] * (__int64)2;
			}
		}

		fprintf(fout,"%I64d\n",sum);
	}

	fcloseall();
}