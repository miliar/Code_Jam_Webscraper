#include<stdio.h>
#include<algorithm>
FILE*in=fopen("input.txt","r");
FILE*out=fopen("output.txt","w");
struct LIST
{
	double x; double y;
	int n;
	bool operator()(LIST a,LIST b)
	{
		if(a.x/a.y!=b.x/b.y) return (a.x/a.y)<(b.x/b.y);
		if(a.x!=b.x) return a.x<b.x;
		if(a.y!=b.y) return a.y<b.y;
		if(a.n!=b.n) return a.n<b.n;
	}
}list[1001];
int N;
int main()
{
	int T;
	fscanf(in,"%d",&T);
	int t,i;
	for(t=1;t<=T;t++)
	{
		fscanf(in,"%d",&N);
		for(i=1;i<=N;i++) fscanf(in,"%lf",&list[i].x);
		for(i=1;i<=N;i++) fscanf(in,"%lf",&list[i].y);
		for(i=1;i<=N;i++) list[i].n=i-1;
		std::sort(list+1,list+1+N,LIST());
		fprintf(out,"Case #%d: ",t);
		for(i=1;i<=N;i++) fprintf(out,"%d ",list[i].n);
		fprintf(out,"\n");
	}
}