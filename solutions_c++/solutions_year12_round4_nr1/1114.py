#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define maxN 100000
int d[maxN],p[maxN],t[maxN];


int Lmin(int a,int b)
{
	if (a>b) return b;
		return a;
}

int Lmax(int a,int b)
{
	if (a>b)return a;
		return b;
}

int main()
{
	int i,j,tt,k,T,n,last;

    FILE* rfp;
	FILE* wfp;
	
	rfp=fopen("A-large.in","r");
	wfp=fopen("A-large.out","w");

	fscanf(rfp,"%d",&T);
	for(k=1;k<=T;k++){
		fprintf(wfp,"Case #%d:",k);
		fscanf(rfp,"%d",&n);
		for (i=1;i<=n;i++){
			fscanf(rfp,"%d %d",&d[i],&t[i]);
			p[i]=0; 
		}
		fscanf(rfp,"%d",&last);

		p[0]=min(d[1],t[1]);d[0]=0;
		for (i=1;i<=n;i++)
		for (j=0;j<i;j++){
			if (p[j]>=d[i]-d[j])
			{
				p[i]=Lmax(Lmin(t[i],d[i]-d[j]),p[i]);
			}
		}
		
		int f=0;
		for (i=0;i<=n;i++)
		if (last-d[i]<=p[i]){
			f=1;break;
		}
        
		if (f==1) fprintf(wfp," YES");
		else fprintf(wfp," NO");
		fprintf(wfp,"\n");
	}
	fclose(rfp);
	fclose(wfp);
	return 0;
}