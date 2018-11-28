#include<iostream>
#include<vector>
#include<algorithm>
#include<utility>
#include<queue>

using namespace std;

int cmp(pair<pair<int,int>,int> a,pair<pair<int,int>,int> b)
{
	if(a.first.first > b.first.first || (a.first.first==b.first.first && a.first.second > b.first.second))
		return 0;
	return 1;
}

int main()
{
	int T,caseNo=1;
	scanf("%d\n",&T);
	while(T--)
	{
		printf("Case #%d: ",caseNo);
		caseNo++;

		int turn,NA,NB,cntA=0,cntB=0,t1,t2,t3,t4;
		scanf("%d\n%d %d\n",&turn,&NA,&NB);
		
		vector<pair<pair<int,int>,int> > schedule(NA+NB);
		for(int i=0;i<NA+NB;i++)
		{
			scanf("%d:%d %d:%d\n",&t1,&t2,&t3,&t4);
			schedule[i] = make_pair(make_pair(t1*60+t2,t3*60+t4),i<NA?1:2);
		}

		sort(schedule.begin(),schedule.end(),cmp);
		
		priority_queue<int,vector<int>,greater<int> > trainA,trainB;

		for(int i=0;i<NA+NB;i++)
		{
			if(schedule[i].second == 1)
			{
				if( !trainA.empty() && trainA.top() <= schedule[i].first.first )
				{
					trainA.pop();
					trainB.push(schedule[i].first.second+turn);
				}
				else
				{
					cntA++;
					trainB.push(schedule[i].first.second+turn);
				}
			}
			else
			{
				if( !trainB.empty() && trainB.top() <= schedule[i].first.first )
				{
					trainB.pop();
					trainA.push(schedule[i].first.second+turn);
				}
				else
				{
					cntB++;
					trainA.push(schedule[i].first.second+turn);
				}
			}
		}
		printf("%d %d\n",cntA,cntB);
	}
	return 0;
}
