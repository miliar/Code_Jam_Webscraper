#include<cstdio>
const int mr=1005;

int T,pr[mr],pn,pre[mr];
bool np[mr];

int find(int x)
{
	return pre[x]==x?x:(pre[x]=find(pre[x]));
}
void Union(int a,int b)
{
	pre[find(a)]=find(b);
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	for(int i=2;i<mr;i++)
	{
		if(!np[i])pr[pn++]=i;
		for(int j=0;j<pn&&i*pr[j]<mr;j++)
		{
			np[i*pr[j]]=1;
			if(i%pr[j]==0)break;
		}
	}
	scanf("%d",&T);
	int a,b,p;
	for(int tn=1;tn<=T;tn++)
	{
		scanf("%d%d%d",&a,&b,&p);
		for(int i=a;i<=b;i++)pre[i]=i;
		for(int i=a;i<=b;i++)
			for(int j=i+1;j<=b;j++)
				if(find(i)!=find(j))
				{
					bool flg=1;
					for(int k=pn-1;pr[k]>=p&&flg;k--)
						if(i%pr[k]==0 && j%pr[k]==0)flg=0;
					if(!flg)
					{
					//	printf("%d %d\n",i,j);
						Union(i,j);
					}
				}
		int cnt=0;
		for(int i=a;i<=b;i++)
			if(pre[i]==i)
				cnt++;
		printf("Case #%d: %d\n",tn,cnt);
	}
	return 0;
}
