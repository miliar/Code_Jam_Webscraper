#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int P,Q,l[110];
int best[110][110];

int f (int s,int e)
{
	if(best[s][e]!=-1)
		return best[s][e];
	if(e==s+1)
		return best[s][e]=0;
	int i,minf=(1<<30);
	for(i=s+1;i<e;i++)
		minf=min (minf,f (s,i)+f (i,e)-l[s]+l[e]-2);
	return best[s][e]=minf;
}

int main ()
{
	FILE *fin,*fout;
	fin=fopen ("Bribe the Prisoners.in","r");
	fout=fopen ("Bribe the Prisoners.out","w");
	
	int N,n;
	fscanf (fin,"%d",&N);
	int i;
	for(n=1;n<=N;n++)
	{
		fscanf (fin,"%d %d",&P,&Q);
		l[0]=0;
		l[Q+1]=P+1;
		for(i=1;i<=Q;i++)
			fscanf (fin,"%d",&l[i]);
		sort(&l[0],&l[Q+2]);
		memset (best,-1,sizeof best);
		f (0,Q+1);
		fprintf (fout,"Case #%d: %d\n",n,best[0][Q+1]);
	}
	return 0;
}
