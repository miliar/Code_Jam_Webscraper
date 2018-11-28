#include<stdio.h>

int main(){
	int t;

	FILE *in;
	FILE *out;

	in=fopen("input.txt","r");
	out=fopen("output.txt","w");

	fscanf(in,"%d",&t);

	for(int cnum=1;cnum<=t;cnum++){
		int n;

		fscanf(in,"%d",&n);

		int xor=0;
		int res=0;
		int min=10000000;

		for(int i=0;i<n;i++){
			int x;
			fscanf(in,"%d",&x);
			xor^=x;
			res+=x;
			if(min>x) min=x;
		}
		
		if(xor==0)fprintf(out,"Case #%d: %d\n",cnum,res-min);
		else fprintf(out,"Case #%d: NO\n",cnum);
	}


	return 0;
}