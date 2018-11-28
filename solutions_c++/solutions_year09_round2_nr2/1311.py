#include<stdio.h>
#include<bitset>
#include<string.h>
#include<algorithm>
using namespace std;
int n,sol[10],v[10],nr;
char acum;
bitset<10> m;
void vezi()
{
	int x=0;
	for(int i=1; i<=n; i++)
		x=x*10+sol[i];
	if(acum==-1)
	{
		if(x==nr)
			return;
		printf("%d\n",x);
		acum=1;
		return;
	}
        if(x==nr)
		acum=-1;	
}
void back(int k)
{
	if(acum==1)
		return;
	if(k==n+1)
	{
		vezi();
		return;
	}
	for(int i=1; i<=n && acum!=1; i++)
	{
		if(!m[i])
		{
			m[i]=1;
			sol[k]=v[i];
			back(k+1);
			m[i]=0;
		}
	}
}
inline void rezolva()
{
       /* scanf("%d",&nr);
        int x1=nr;
	n=0;
	while(x1)
	{
		v[++n]=x1%10;
		x1/=10;
	}
	sort(v+1,v+n+1);
	acum=0;
        back(1);
	if(acum==1)
		return;
	bitset<10> scris;
	scris.reset();
	for(int i=1; i<=n; ++i)
	{
		if(v[i]==0)
			continue;
		printf("%d",v[i]);
		scris[i]=1;
		break;
	}
	printf("0");
	for(int i=1; i<=n; ++i)
	{
		if(scris[i]==1)
			continue;
		printf("%d",v[i]);
	}
	printf("\n");    */
	scanf("%d",&nr);
	int x=nr;
	int cate[11]={0};
	while(x)
	{
		++cate[x%10];
		x/=10;
	}
	int cate1[11];
	for(int i=nr+1; ; ++i)
	{
        	int aux=i;
                memset(cate1,0,sizeof(cate1));
		while(aux)
		{
			++cate1[aux%10];
			aux/=10;
		}
		bool ok=true;
		for(int i=1; i<10 && ok; ++i)
		{
                	if(cate[i]!=cate1[i])
				ok=false;
		}
		if(ok)
		{
			printf("%d\n",i);
			return;
		}
	}
}	
int main()
{
	freopen("pb.in","r",stdin);
	freopen("pb.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1; i<=T; ++i)
	{
		printf("Case #%d: ",i);
		rezolva();
	}
	return 0;
}

