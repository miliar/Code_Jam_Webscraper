#include<iostream>
#include<cstdio>
#include<list>

using namespace std;

struct node{
	int a;
	int b;
};

struct xpoint{
	double x;
	double y;
};

node indata[1001];


bool myfind(list<xpoint> &test,xpoint &temp)
{
	list<xpoint>::iterator iptr;
	for(iptr=test.begin();iptr!=test.end();iptr++)
	{
		if((*iptr).x==temp.x&&(*iptr).y==temp.y)
		{
			return true;
		}
	}
	return false;
}

int main()
{
	int T,N;
	
	xpoint temp;
	int ans,counter;
	scanf("%d",&T);
	counter=1;
	while(T--)
	{
		list<xpoint> myans;
		ans=0;
		
		scanf("%d",&N);
		for(int i=0;i<N;i++)
		{
			scanf("%d%d",&indata[i].a,&indata[i].b);
		}
		for(int i=1;i<N;i++)
		{
			for(int j=i-1;j>=0;j--)
			{
				if(indata[i].a<indata[j].a&&indata[i].b>indata[j].b)
				{
					temp.x=(double)(indata[j].a-indata[i].a)/(double)(indata[i].b-indata[j].b+indata[j].a-indata[i].a);
					temp.y=(double)indata[i].a+(double)(indata[i].b-indata[i].a)*(double)(indata[j].a-indata[i].a)/(double)(indata[i].b-indata[j].b+indata[j].a-indata[i].a);
					if(!myfind(myans,temp))
					{
						myans.push_back(temp);
					}
					
				}
				else if(indata[i].a>indata[j].a&&indata[i].b<indata[j].b)
				{
					temp.x=(double)(indata[i].a-indata[j].a)/(double)(indata[j].b-indata[i].b+indata[i].a-indata[j].a);
					temp.y=(double)indata[j].a+(double)(indata[j].b-indata[j].a)*(double)(indata[i].a-indata[j].a)/(double)(indata[j].b-indata[i].b+indata[i].a-indata[j].a);
					if(!myfind(myans,temp))
					{
						myans.push_back(temp);
					}
				}
			}
		}
		printf("Case #%d: %d\n",counter++,myans.size());
	}
	return 0;
}