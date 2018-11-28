#include<stdio.h>
FILE *in=fopen("input.txt","r");
FILE *out=fopen("output.txt","w");
int ta,a,b,c,i,v[2000001],cc,r[10],t,j;
long long res;
int main(){
	fscanf(in,"%d",&t);
	a=1;
	for(i=0;i<7;i++){r[i]=a;v[a]=1;a*=10;}
	while(t>c){
		c++;
		fprintf(out,"Case #%d: ",c);
		fscanf(in,"%d%d",&a,&b);
		ta=a-1,cc=0;
		res=0;
		while(ta>0){ta/=10;cc++;}
		cc--;
		for(i=a;i<b;i++){
			if(v[i])cc++;
			ta=i;
			for(j=0;j<cc;j++){
				ta=ta/10+(ta%10)*r[cc];
				if(i==ta)break;
				if(i<ta&&ta<=b)res++;}}
		fprintf(out,"%lld\n",res);
	}
}