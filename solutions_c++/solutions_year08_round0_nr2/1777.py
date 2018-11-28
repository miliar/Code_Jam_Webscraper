#include<iostream>
#include<algorithm>
using namespace std;

struct node
{
  int time;
  int sta;
  int from;
}data[500];

int ans[3];
int cur[3];

bool cmp(const node& a,const node& b)
{
	if(a.time!=b.time) return a.time<b.time;
	else return a.from>b.from;
}


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int N;
	int line=0;
	scanf("%d\n",&N);
	while(N--)
	{
		int NA,NB,T;
		scanf("%d\n",&T);
		scanf("%d %d\n",&NA,&NB);
		for(int i=0;i<2*NA;i++)
		{
			int temp;
			int da=0;
			char ch;
			scanf("%d%c%d ",&temp,&ch,&da);
			da+=(temp*100);
			data[i].time=da;
			data[i].sta=1;
			data[i++].from=1;
			scanf("%d%c%d ",&temp,&ch,&da);
			da+=(temp*100);
			data[i].time=(da+T);
			data[i].sta=1;
			data[i].from=2;
		}
        int m=NA*2+NB*2;
		for(int i=2*NA;i<m;i++)
		{
			int temp;
			int da=0;
			char ch;
			scanf("%d%c%d ",&temp,&ch,&da);
			da+=(temp*100);
			data[i].time=da;
			data[i].sta=2;
			data[i++].from=1;
			scanf("%d%c%d ",&temp,&ch,&da);
			da+=(temp*100);
			data[i].time=(da+T);
			data[i].sta=2;
			data[i].from=2;
		}
		
		sort(data,data+m,cmp);
		ans[1]=0;
		ans[2]=0;
		cur[1]=0;
		cur[2]=0;
		
	//	for(int i=0;i<m;i++)
	//	printf("%d %d %d\n ",data[i].time,data[i].sta,data[i].from);
		
		for(int i=0;i<m;i++)
		{
			if(data[i].from==2)
            { 
				if(data[i].sta==1) cur[2]++;
				else cur[1]++;
            }
			else
			{
				if(cur[data[i].sta]>0)
					cur[data[i].sta]--;
				else 
				{
					ans[data[i].sta]++;
				}
			}
		}
		printf("Case #%d: %d %d\n",++line,ans[1],ans[2]);

	}
}
