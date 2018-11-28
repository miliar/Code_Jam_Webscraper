#include<stdio.h>
int abs(int x);
int abs(int x){
	if(x<0) return x*-1;
	else return x;
}
int main(){
	int t,n,O[101],B[101],se[201][3],on,bn,total,op,bp,oc,bc,ot,bt,gap;
	char temp;
	FILE *fp=fopen("a.out","w");
	scanf("%d",&t);
	for(int casen = 1 ; casen <= t ; casen ++)
	{
		scanf("%d",&n);
		on=0;
		bn=0;
		for(int i=0;i<n;i++){
			int t1;
			scanf(" %c %d",&temp,&t1);
			if(temp=='O'){ O[on++]=t1; se[i][0]=t1; se[i][1]=1;}
			else{ B[bn++]=t1; se[i][0]=t1; se[i][1]=2;}
		}
		total=0;
		op=1;
		bp=1;
		oc=0;
		bc=0;
		ot=0;
		bt=0;


		for(int i=0;i<n;i++){
			if(se[i][1]==1){
				ot+=abs(op-O[oc])+1;
				op=O[oc++];

				se[i][2]=ot;
			}
			else{
				bt+=abs(bp-B[bc])+1;
				bp=B[bc++];
				se[i][2]=bt;
			}

		}
		gap=0;
		for(int i=1;i<n;i++){
			if(se[i][1]!=se[i-1][1]){
				if(se[i][2]<=se[i-1][2]){
					gap=(se[i-1][2]-se[i][2])+1;
					for(int j=i;j<n;j++)
						if(se[j][1]==se[i][1]) se[j][2]+= gap;
				}
				else gap=0;
				
			}
			
		}

		fprintf(fp,"Case #%d: %d\n",casen,se[n-1][2]);

	}
}