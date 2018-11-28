#include <stdio.h>
FILE *in=fopen("C-large.in","r");
FILE *out=fopen("output.txt","w");

int T;
int R,K,n;
int data[1001];
__int64 p[1001][2];
int check[1001];
__int64 check2[1001];
__int64 answer,s,sum;

int main(){
	int i,k,ind;
	fscanf(in,"%d",&T);
	for(k=0;k<T;k++){
		fscanf(in,"%d%d%d",&R,&K,&n);
		s=0;answer=0;
		for(i=0;i<n;i++){
			fscanf(in,"%d",&data[i]);
			s+=data[i];
		}
		for(i=0;i<n;i++){
			sum=0;
			for(ind=i;;ind=(ind+1)%n){
				sum+=data[ind];
				if(sum!=data[ind] && ind==i) break;
				if(sum>K) break;
			}
			p[i][0]=ind;
			p[i][1]=sum-data[ind];
		}
		int flag=0;
		for(i=0;i<n;i++) check[i]=-1,check2[i]=0;
		for(ind=0,i=0;R>0;i++,R--){
			if(check[ind]!=-1 && flag==0){
				answer+=((__int64)R/(i-check[ind]))*(answer-check2[ind]);
				R%=(i-check[ind]);
				flag=1;
				R++;
				continue;
			}
			check[ind]=i;
			check2[ind]=answer;
			answer+=p[ind][1];
			ind=p[ind][0];
		}
		fprintf(out,"Case #%d: %I64d\n",k+1,answer);
	}
	return 0;
}
