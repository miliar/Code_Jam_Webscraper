#include<stdio.h>

#define ABS(a) ((a)<0?((a)*(-1)):(a))

int main()
{
	int tt,l,x,p[2],m,i,pt[2],d,t,ind;
	char c;
	FILE *in=fopen("input.txt","r"),*out=fopen("output.txt","w");
	fscanf(in,"%d",&tt);
	for(l=0;l<tt;l++){
		p[0]=1;p[1]=1;
		pt[0]=0;pt[1]=0;
		t=0;
		fscanf(in,"%d",&m);
		for(i=0;i<m;i++){
			fscanf(in," %c %d",&c,&x);
			if(c=='B'){
				ind=0;
			}else{
				ind=1;
			}
			d=ABS(x-p[ind]);
			d=(d>pt[ind])?(d-pt[ind]):0;
			++d;
			t+=d;
			p[ind]=x;
			pt[ind]=0;
			pt[1-ind]+=d;
		}
		fprintf(out,"Case #%d: %d\n",l+1,t);
	}
	return 0;
}