#include<stdio.h>
#define max 10000
FILE *in=fopen("input.txt","r");
FILE *out=fopen("output.txt","w");
int n,l,h;
int f[max+5];
int res;
void input(){
//	fscanf(in,"%d%I64d%I64d",&n,&l,&h);
//	for(int i=0;i<n;i++){
//		fscanf(in,"%I64d",&
//	}
	fscanf(in,"%d%d%d",&n,&l,&h);
	for(int i=0;i<n;i++){
		fscanf(in,"%d",&f[i]);
	}
}
void process(){
	res=-1;
	for(int i=l;i<=h;i++){
		int w=0;
		for(int j=0;j<n;j++){
			if(f[j]%i==0 || i%f[j]==0) continue;
			w=1;
			break;
		}
		if(w==0){
			res=i;
			break;
		}
	}
}
void output(int tc){
	if(res==-1) fprintf(out,"Case #%d: NO\n",tc);
	else fprintf(out,"Case #%d: %d\n",tc,res);
}
int main(){
	int t;
	fscanf(in,"%d",&t);
	for(int i=0;i<t;i++){
		input();
		process();
		output(i+1);
	}
	fclose(in);
	fclose(out);
	return 0;
}
