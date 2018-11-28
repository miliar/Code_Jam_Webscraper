#include<stdio.h>
FILE *in=fopen("input.txt","r");
FILE *out=fopen("output.txt","w");
int t,c,n,m,p,D[101][101],w[101],i,j,x,y;
int main()
{
	fscanf(in,"%d",&t);
	while(t>c){
		c++;
		fprintf(out,"Case #%d: ",c);
		fscanf(in,"%d%d%d",&n,&m,&p);
		for(i=0;i<n;i++)fscanf(in,"%d",&w[i]);
		for(i=0;i<n;i++){
			x=(w[i]+2)/3,y=(w[i]+4)/3;
			if(w[i]<=1)x=y=0;
			if(w[i]>=28)x=y=10;
			if(x>=p)x=1;else x=0;if(y>=p)y=1;else y=0;
			if(i==0){D[i][0]=x,D[i][1]=y;continue;}
			for(j=0;j<=m&&j<=i+1;j++){
				if(j>=1)D[i][j]=D[i-1][j-1]+y;
				if(D[i][j]<D[i-1][j]+x)D[i][j]=D[i-1][j]+x;}}
		fprintf(out,"%d\n",D[n-1][m]);
		for(i=0;i<n;i++)for(j=0;j<=m;j++)D[i][j]=0;
	}
}