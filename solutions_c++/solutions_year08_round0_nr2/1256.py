#include<iostream>
#include<algorithm>
#include<assert.h>
using namespace std;
struct Node
{
	int s,e;
	bool flag;
};
Node NN[256];
int T,nA,nB;
int ansA,ansB;
bool visit[256];
bool cmp(const Node& A,const Node &B)
{
	if(A.s==B.s)return A.e<B.e;
	return A.s<B.s;
}
void read()
{
	int sh,sm,eh,em,j=0;
	cin>>T>>nA>>nB;
	for(int i=0;i<nA;i++)
	{
		scanf("%d:%d %d:%d",&sh,&sm,&eh,&em);
		NN[j].s=sh*60+sm;
		NN[j].e=eh*60+em+T;
		NN[j].flag=true;
		j++;
	}
	for(int i=0;i<nB;i++)
	{
		scanf("%d:%d %d:%d",&sh,&sm,&eh,&em);
		NN[j].s=sh*60+sm;
		NN[j].e=eh*60+em+T;
		NN[j].flag=false;
		j++;
	}
	sort(NN,NN+nA+nB,cmp);
	assert(j==nA+nB);
}

void solve()
{
	ansA=0,ansB=0;
	bool flag;
	int tmpe,j;
	memset(visit,false,sizeof(visit));
	for(int i=0;i<nA+nB;i++)
	{
		if(visit[i])continue;
		visit[i]=true;
		if(NN[i].flag)
		{
			
			ansA++;
			flag=NN[i].flag;
			tmpe=NN[i].e;
			for(j=i+1;j<nA+nB;j++)if(NN[j].flag==!flag&&!visit[j])
			{
				if(tmpe<=NN[j].s)
				{
					flag=!flag;
					tmpe=NN[j].e;
					visit[j]=true;
				}
			}
		}
		else
		{
			ansB++;
			flag=NN[i].flag;
			tmpe=NN[i].e;
			for(j=i+1;j<nA+nB;j++)if(NN[j].flag==!flag&&!visit[j])
			{
				if(tmpe<=NN[j].s)
				{
					flag=!flag;
					tmpe=NN[j].e;
					visit[j]=true;
				}
			}
		}
	}
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int cas;
	cin>>cas;
	for(int ca=1;ca<=cas;ca++)
	{
		read();
		solve();
		printf("Case #%d: %d %d\n",ca,ansA,ansB);
	}
}