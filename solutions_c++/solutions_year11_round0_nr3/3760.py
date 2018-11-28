#include<stdio.h>
#include<memory.h>
int main()
{
	int tc,n,i,l,c,j,bin[40],temp,min,sum,bm;
	FILE *in=fopen("input.txt","r"),*out=fopen("output.txt","w");
	fscanf(in,"%d",&tc);
	for(l=0;l<tc;l++){
		memset(bin,0,sizeof(bin));
		fscanf(in,"%d",&n);
		min=1000001;
		sum=0;
		bm=0;
		for(i=0;i<n;i++){
			fscanf(in,"%d",&c);
			if(min>c){min=c;}
			sum+=c;
			temp=c;
			for(j=0;temp>0;j++){
				bin[j]+=temp&1;
				temp=temp>>1;
			}
			if(bm<j){bm=j;}
		}
		for(i=0;i<bm;i++){
			if(bin[i]%2){
				break;
			}
		}
		if(i<bm){
			fprintf(out,"Case #%d: NO\n",l+1);
		}else{
			fprintf(out,"Case #%d: %d\n",l+1,sum-min);
		}
	}
}