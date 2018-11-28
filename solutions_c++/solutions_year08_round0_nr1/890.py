#include <iostream>
#include <cstdio>
#include <string>
#include <queue>
#include <algorithm>

#define INF 1000000000

using namespace std;

//queue<int> list[101];
int quer[1001];

string name[101];

int S,Q;
/*
int simulate()
{
	int cur=-1, max_time=-INF;
	//cout<<"Here"<<endl;
	//cout<<"Q="<<Q<<endl; 
	
	for(int i=0;i<S;i++)
	{
		//cout<<"There"<<endl;
	
		int c=list[i].front();
		if (c>max_time)
		{
			max_time=c;
			cur=i;
		}
	}
	int ret=0;
	for (int i=0;i<Q;i++)
	{
		int q=quer[i];
		cout<<"q="<<q<<" cur="<<cur<<endl;
		cout<<"q="<<name[q]<<" cur="<<name[cur]<<endl;
		if (q==cur)
		{
			list[cur].pop();
			ret++;
			
			max_time=-INF;
			int next=-1;
			cout<<"selecting max"<<endl;
			for(int j=0;j<S;j++)
			{
				if (cur==j) continue;
				int time=list[j].front();
				if (max_time<time)
				{
					cout<<"updating max"<<" city="<<name[j]<<" time="<<time<<endl;
					max_time=time;
					next=j;
				}
			}
			cout<<"city selected="<<name[next]<<endl;
			cur=next;
		}
	}
	//cout<<"returning "<<ret<<endl;
	return ret;
}*/

int compute()
{
	int latest[101];
	for (int i=0;i<S;i++) latest[i]=INF;
	for(int i=0;i<Q;i++)
	{
		int x=quer[i];
		latest[x]=min(latest[x],i);
	}
	int cur=0, max_time=-INF;
	for(int i=0;i<S;i++)
	{
		if (latest[i]>max_time) {
			max_time=latest[i];
			cur=i;
		}
	}
	int ret=0;
	for(int i=0;i<Q;i++)
	{
		int x=quer[i];
		//cout<<"x="<<x<<endl;
		//cout<<"x="<<name[x]<<" cur="<<name[cur]<<endl;
		if (x==cur)
		{
			//cout<<"changing"<<endl;
			for (int j=0;j<S;j++) latest[j]=INF;
	
			for(int j=i+1;j<Q;j++)
			{
				int xl=quer[j];
				latest[xl]=min(latest[xl],j);
			}
			int old=cur;
			cur=0, max_time=-INF;
			for(int j=0;j<S;j++)
			{
				if (j==old) continue;
				if (latest[j]>max_time) {
					max_time=latest[j];
					cur=j;
				}	
			}
			
			ret++;
		}
	}
	return ret;
}
char buffer[100];

int main()
{
	int N;
	scanf("%d", &N);
	for(int cs=1;cs<=N;cs++)
	{
		scanf("%d", &S);
		//printf("S=%d\n",S);
		gets(buffer);
		for(int i=0;i<S;i++){
			gets(buffer);
			name[i]=string(buffer);
			//printf("got %s\n", buffer);
		}
		//for(int i=0;i<S;i++) while(!list[i].empty()) list[i].pop();
		scanf("%d", &Q);
		gets(buffer);
		//printf("Q=%d\n",Q);
		for(int i=0;i<Q;i++)
		{
			gets(buffer);
			//printf("got %s\n", buffer);
			int index=0;
			for (int j=0;j<S;j++)
			{
				if (strcmp(name[j].c_str(), buffer)==0)
				{
					index=j;
					break;
				}
			}
			quer[i]=index;
			//list[index].push(i);
		}
		//for(int i=0;i<S;i++) list[i].push(INF);
		
		//for(int i=0;i<S;i++) reverse(list[i].begin(), list[i].end());
 		int answer=compute();
		printf("Case #%d: %d\n", cs, answer);
	}
		
}
