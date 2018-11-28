#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<stdlib.h>
using namespace std;
struct node
{
	char str[3];
	int p;
};
int olist[105];
int blist[105];
node list[105];
int main(void){
	FILE*in=fopen("D://Downloads/A-large.in","rt");
	FILE*out=fopen("C:/Users/lenovo/Desktop/out.txt","wt");
	int test; fscanf(in,"%d",&test);
	for(int testi=1;testi<=test;testi++)	{
		int n; fscanf(in,"%d",&n);
		int i,oi=1,bi=1;
		blist[0]=olist[0]=1;
		for(i=0;i<n;i++)
		{
			fscanf(in,"%s%d",list[i].str,&list[i].p);
			if(list[i].str[0]=='O') olist[oi++]=list[i].p;
			else blist[bi++]=list[i].p;
		}
		int t=0,op=1,bp=1,d;
		oi=bi=0;
		for(i=0;i<n;i++)
		{
			if(list[i].str[0]=='O')
			{
				d=abs(list[i].p-op)+1;
				oi++;
				op=list[i].p;
				t+=d;
				if(bp<blist[bi+1])
				{
					bp+=d;
					if(bp>blist[bi+1]) bp=blist[bi+1];
				} 
				else
				{
					bp-=d;
					if(bp<blist[bi+1]) bp=blist[bi+1];
				}
			}
			else
			{
				d=abs(list[i].p-bp)+1;
				bi++;
				bp=list[i].p;
				t+=d;
				if(op<olist[oi+1])
				{
					op+=d;
					if(op>olist[oi+1]) op=olist[oi+1];
				} 
				else
				{
					op-=d;
					if(op<olist[oi+1]) op=olist[oi+1];
				}

			}
		}
		
			fprintf(out,"Case #%d: %d\n",testi,t);
	}

	return 0;
}