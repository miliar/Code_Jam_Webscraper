#include<iostream>
#include<queue>
#include<stdio.h>
using namespace std;
void SWAP(int&x,int&y) 
{
	x^=y,y^=x,x^=y;
}
int gcd(int x,int y)
{
	if(!y) return x;
	return gcd(y,x%y);
}
int main(void)
{
	FILE*in=fopen("D://in.txt","r");
	FILE*out=fopen("D://out.txt","w");
    int t;
	fscanf(in,"%d",&t);
	for(int i=1;i<=t;i++)
	{
	    int n;
		fscanf(in,"%d",&n);
		int x,y,z,a,b,c,d;
		fprintf(out,"Case #%d: ",i);
		if(n==2)
		{
			fscanf(in,"%d%d",&x,&y);
			if(x<y) SWAP(x,y);
			c=x-y;
			d=(c-y%c)%c;
			fprintf(out,"%d\n",d);
		}
		if(n==3)
		{
			fscanf(in,"%d%d%d",&x,&y,&z);
			if(x<y) SWAP(x,y);
			if(y<z) SWAP(y,z);
			if(x<y) SWAP(x,y);
			a=x-y; b=x-z;
			c=gcd(a,b);
			d=(c-y%c)%c;
			fprintf(out,"%d\n",d);
		}
	}
	return 0;
}
		