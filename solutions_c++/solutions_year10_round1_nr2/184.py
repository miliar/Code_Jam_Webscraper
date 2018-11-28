#include <iostream>

using namespace std;

int D,I,M,N;

int data[110];
const int inf = 1000000000;

#define MMod 100000
//int ID[MMod];
int P[MMod];
int q_l,q_r;
int dist[110][300];
bool vst[110][300];
int ID[MMod];
int spfa()
{
	memset(dist,0x3f,sizeof(dist));
	memset(vst,0,sizeof(vst));
	q_l=q_r=0;
	ID[q_r]=0;
	P[q_r]=-1;
	dist[0][0]=0;
	q_r++;
	int ret=inf;
	int np;
	while(q_l!=q_r)
	{
		int i=ID[q_l];
		int p=P[q_l];
		vst[i][p+1]=false;
		q_l=(++q_l)%MMod;
		if(i==N)
		{
			if(dist[i][p+1]<ret) ret=dist[i][p+1];
			continue;
		}
		if(dist[i+1][p+1]>dist[i][p+1]+D)
		{
			dist[i+1][p+1]=dist[i][p+1]+D;
			if(!vst[i+1][p+1])
			{
				vst[i+1][p+1]=true;
				ID[q_r]=i+1;
				P[q_r]=p;
				q_r=(++q_r)%MMod;
			}
		}
		if(p==-1)
		{
			for(np=0;np<=255;np++)
			{
				int rr=abs(data[i]-np)+dist[i][p+1];
				if(rr<dist[i+1][np+1])
				{
					dist[i+1][np+1]=rr;
					if(!vst[i+1][np+1])
					{
						vst[i+1][np+1]=true;
						ID[q_r]=i+1;
						P[q_r]=np;
						q_r=(++q_r)%MMod;
					}
				}
			}
		}
		else
		{
			int bg=p-M,ed=p+M;
			if(bg<0) bg=0;
			if(ed>255) ed=255;
			for(np=bg;np<=ed;np++)
			{
				int rr=abs(data[i]-np)+dist[i][p+1];
				if(rr<dist[i+1][np+1])
				{
					dist[i+1][np+1]=rr;
					if(!vst[i+1][np+1])
					{
						vst[i+1][np+1]=true;
						ID[q_r]=i+1;
						P[q_r]=np;
						q_r=(++q_r)%MMod;
					}
				}
			}
		}
		if(p!=-1)
		{
			int bg=p-M,ed=p+M;
			if(bg<0) bg=0;
			if(ed>255) ed=255;
			for(np=bg;np<=ed;np++)
			{
				int rr=I+dist[i][p+1];
				if(rr<dist[i][np+1])
				{
					dist[i][np+1]=rr;
					if(!vst[i][np+1])
					{
						vst[i][np+1]=true;
						ID[q_r]=i;
						P[q_r]=np;
						q_r=(++q_r)%MMod;
					}
				}
			}
		}
	}
	return ret;
}

int main()
{
	int t;
	scanf("%d",&t);
	int cse=0;
	while(t--)
	{
		cse++;
		fprintf(stderr,"%d\n",cse);
		scanf("%d%d%d%d",&D,&I,&M,&N);
		int i;
		for(i=0;i<N;i++) scanf("%d",data+i);
		int ret=spfa();
		printf("Case #%d: %d\n",cse,ret);

	}
	return 0;
}
