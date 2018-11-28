#include<stdio.h>
#include "stdafx.h"
#include<algorithm>
#include<vector>
#include<queue>
#include<stdlib.h>
using namespace std;
typedef pair<int,int>pii;
int main()
{
	FILE *fp=fopen("A-small-attempt0.in","r");
	FILE *fp2=fopen("out.txt","w");
	int data;
	fscanf(fp,"%d",&data);
	for(int i=0;i<data;i++)
	{
		int num;
		fscanf(fp,"%d",&num);
		vector<pii>vec;
		queue<pii>que;
		int flag[10000];
		fill(flag,flag+10000,-1);
		for(int j=0;j<num;j++)
		{
			int za,zb;
			fscanf(fp,"%d%d",&za,&zb);
			vec.push_back(make_pair(za,zb));
		}
		que.push(make_pair(0,vec[0].first));
		int mok;
		fscanf(fp,"%d",&mok);
		printf("Case #%d: ",i+1);
		fprintf(fp2,"Case #%d: ",i+1);
		for(;;)
		{
			if(que.empty())
			{
				printf("NO\n");
				fprintf(fp2,"NO\n");
				break;
			}
			pii zan=que.front();
			que.pop();
			//printf("%d %d\n",vec[zan.first].first,zan.second);
			if(mok<=vec[zan.first].first+zan.second)
			{
				printf("YES\n");
				fprintf(fp2,"YES\n");
				break;
			}
			if(flag[zan.first]>=zan.second)
			{
				continue;
			}
			flag[zan.first]=zan.second;
			int low=lower_bound(vec.begin(),vec.end(),make_pair(vec[zan.first].first-zan.second,0))-vec.begin();
			int upp=upper_bound(vec.begin(),vec.end(),make_pair(vec[zan.first].first+zan.second,2000000000))-vec.begin()-1;
			for(int q=low;q<=upp;q++)
			{
				int ab=min(abs(vec[zan.first].first-vec[q].first),vec[q].second);
				pii hoge=make_pair(q,ab);
				que.push(hoge);
			}
		}
	}
}