#include<cstdio>
#include<string>
#include<algorithm>
#include<vector>
#include<cstdio>

using namespace std;

typedef pair<int,int> PI;
typedef pair<int,PI>  PII;
int T,nA,nB;
vector<PII> events;

int parse(char *num,int type)
{
	int h=(num[0]-'0')*10+num[1]-'0';
	int m=(num[3]-'0')*10+num[4]-'0';

	if(type) m+=T;
	return h*60+m;
}

int main()
{
	int cs=0,tests,i,j;
	char start[20],end[20];


	freopen("C:\\B2.txt","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		events.clear();

		scanf("%d",&T);
		scanf("%d %d",&nA,&nB);

		for(i=0;i<nA;i++)
		{
			scanf("%s %s",start,end);
			int ss=parse(start,0);
			int ee=parse(end,1);

		//	printf("%d %d\n",ss,ee);

			events.push_back(make_pair(ss,make_pair(1,0)));
			events.push_back(make_pair(ee,make_pair(0,1)));
		}

		for(i=0;i<nB;i++)
		{
			scanf("%s %s",start,end);
			int ss=parse(start,0);
			int ee=parse(end,1);

		//	printf("%d %d\n",ss,ee);

			events.push_back(make_pair(ss,make_pair(1,1)));
			events.push_back(make_pair(ee,make_pair(0,0)));
		}

		sort(events.begin(),events.end());

		int cnt[2],ans[2];
		cnt[0]=cnt[1]=0;
		ans[0]=ans[1]=0;

		for(i=0;i<events.size();i++)
		{
			int time=events[i].first;
			int type=events[i].second.first;
			int station=events[i].second.second;

		//	printf("%d %d %d\n",time,type,station);

			if(type)
			{
				if(!cnt[station]) ans[station]++,cnt[station]++;
				cnt[ station]--;		
			}
			else
			{
				cnt[station]++;
			}
		}

		printf("Case #%d: %d %d\n",++cs,ans[0],ans[1]);
	}
	return 0;
}





