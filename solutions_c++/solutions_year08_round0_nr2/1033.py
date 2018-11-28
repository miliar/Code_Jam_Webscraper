#include <stdio.h>
#include <vector>

using namespace std;

struct ab
{
	int chas1,chas2,stat;
} example;

int transfer(char s[])
{
	return (((s[0]-'0')*10+(s[1]-'0'))*60+(s[3]-'0')*10+(s[4]-'0'));
}

int rec(int k)
{
	return k==1?0:1;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.in","w",stdout);
	char chas[10];
	int T,N,Na,Nb,ka,kb,time,stat;
	vector<ab> rozklad;
	scanf("%d",&N);
	for(int z=0;z<N;z++)
	{
		scanf("%d%d%d",&T,&Na,&Nb);
		ka=kb=0;

		for(int i=0;i<Na;i++)
		{
			scanf("%s",chas);
			example.chas1=transfer(chas);
			example.stat=0;
			scanf("%s",chas);
			example.chas2=transfer(chas)+T;
			rozklad.push_back(example);
		}

		for(int i=0;i<Nb;i++)
		{
			scanf("%s",chas);
			example.chas1=transfer(chas);
			example.stat=1;
			scanf("%s",chas);
			example.chas2=transfer(chas)+T;
			rozklad.push_back(example);
		}

		for(int i=0;i<rozklad.size()-1;i++)
			for(int j=0;j<rozklad.size()-1-i;j++)
				if(rozklad[j].chas1>rozklad[j+1].chas1){
					example=rozklad[j];
					rozklad[j]=rozklad[j+1];
					rozklad[j+1]=example;
				}

		while(rozklad.size()>0)
		{
			if(rozklad[0].stat==0) ka++;
			else kb++;
			time=rozklad[0].chas2;
			stat=rozklad[0].stat;
			rozklad.erase(rozklad.begin());

			for(int i=0;i<rozklad.size();i++)
			{
				if(rozklad[i].stat==rec(stat)&&rozklad[i].chas1>=time)
				{
					stat=rec(stat);
					time=rozklad[i].chas2;
					rozklad.erase(rozklad.begin()+i);
					i--;
				}
			}
		}
		printf("Case #%d: %d %d\n",z+1,ka,kb);
	}
	return 0;
}