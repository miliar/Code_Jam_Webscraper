#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
const int MAX=100;

int N,K,B,T;
struct NODE
{
	int pos,sped;
	bool f;
	int ned;
}nod[MAX];
bool cmp(NODE a,NODE b)
{
	if(a.f==b.f) return a.ned<b.ned;
	return a.f>b.f;
}
int main()
{
	freopen("F:\\B-large.in","r",stdin);
	freopen("F:\\B-large.out","w",stdout);
	//freopen("F:\\B-small-attempt1.in","r",stdin);
	//freopen("F:\\B-small-attempt1.out","w",stdout);
	
	int i,j,Te;scanf("%d",&Te);
	int CN=0;
	while(Te--)
	{
		scanf("%d%d%d%d",&N,&K,&B,&T);
		
		for(i=1;i<=N;i++) scanf("%d",&nod[i].pos);
		int num=0;
		for(i=1;i<=N;i++) 
		{
			scanf("%d",&nod[i].sped);
			if(nod[i].sped*T+nod[i].pos>=B) {nod[i].f=1;num++;}
			else nod[i].f=0;
		}
		if(num<K) {printf("Case #%d: IMPOSSIBLE\n",++CN);continue;}
		for(i=N;i>=1;i--)
		{
			nod[i].ned=0;
			if(nod[i].f==0) continue;
			
			for(j=i+1;j<=N;j++)
			{
				if(nod[j].sped<nod[i].sped)
				{
					if(nod[j].f) 
					{
						nod[i].ned+=nod[j].ned;
						break;
					}
					nod[i].ned++;
				}
			}
		}
		sort(&nod[1],&nod[N+1],cmp);
		/*
		for(i=1;i<=N;i++)
		{
			cout<<nod[i].pos<<" "<<nod[i].sped<<"      "<<nod[i].f<<"  "<<nod[i].ned<<endl;
		}
		*/
		int ans=0;
		for(i=1;i<=K;i++) ans+=nod[i].ned;
		printf("Case #%d: %d\n",++CN,ans);
	}
	//system("pause");
	return 0;
}
