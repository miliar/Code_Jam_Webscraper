#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

int main()
{
	FILE *fpin,*fpout;
	int T, A, B, i, n, m, count=0, d=0, x,j,k,r,p,temp=0;
	
	fpin=fopen("C-small-attempt0.in","r");
	fpout=fopen("C-small.out","w");
	if(fpin==NULL)
		exit(10);
	fscanf(fpin,"%d",&T);
	for(i=0;i<T;i++){
		fscanf(fpin, "%d", &A);
		fscanf(fpin, "%d", &B);
		x=A;
		while(x!=0){
			x=x/10;
			d++;
		}
		for(j=A;j<B;j++)
		{
			n=j;
			//fprintf(fpout, "\n\nn=%d\n", n);
			for(m=j+1;m<=B;m++){
			//	fprintf(fpout, "m=%d\n", m);
				for(k=0;k<d;k++){
					r=n%10;
					n=n/10;
					for(p=1;p<d;p++)
						r=r*10;
					n=n+r;
					if(n==m){
						if(temp!=m){
							temp=m;
							count++;
						}
				//fprintf(fpout, "%d: %d\n", j, m);
					}
					r=0;
				}
			}
		}
		fprintf(fpout, "Case #%d: %d\n", i+1, count);
		count=0;
		d=0;
		temp=0;
	}
}
