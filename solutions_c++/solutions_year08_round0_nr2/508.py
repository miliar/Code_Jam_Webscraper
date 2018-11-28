#include<iostream>
#include<queue>
using namespace std;
struct TIM
{
	int tim;
	TIM(){}
	TIM(int t){tim=t;}
};
bool operator<(const TIM &p,const TIM &q)
{
	return p.tim>q.tim;
}
struct MM
{
	int st,end;
	MM(){}
	MM(int ss,int ee){st=ss;end=ee;}
};
bool operator<(const MM &p,const MM &q)
{
	if(p.st!=q.st) return p.st<q.st;
	return p.end<q.end;
}
vector<MM>va,vb;
int main()
{
//	freopen("B-large.in","r",stdin);
//	freopen("B-large.out","w",stdout);
	MM it;
	int cas,t,A,B,test=1,i,ansa,ansb,sth,stm,endh,endm;
	scanf("%d",&cas);
	while(cas--)
	{
		scanf("%d%d%d",&t,&A,&B);
		va.clear();
		vb.clear();
		for(i=0;i<A;i++)
		{
			scanf("%d:%d %d:%d",&sth,&stm,&endh,&endm);
			it.st=60*sth+stm;
			it.end=60*endh+endm;
			va.push_back(it);
		}
		for(i=0;i<B;i++)
		{
			scanf("%d:%d %d:%d",&sth,&stm,&endh,&endm);
			it.st=60*sth+stm;
			it.end=60*endh+endm;
			vb.push_back(it);
		}
		priority_queue<TIM> dqa,dqb;
		sort(va.begin(),va.end());
		va.push_back(MM(1000000000,1000000000));
		sort(vb.begin(),vb.end());
		vb.push_back(MM(1000000000,1000000000));
		int a=0,b=0;
		ansa=0,ansb=0;
		while(1)
		{
		//	cout<<a<<" "<<b<<endl;
			if(va[a].st<=vb[b].st)
			{
				if(dqa.size()&&dqa.top().tim<=va[a].st)
				{
					dqa.pop();
				}
				else 
				{
					ansa++;
				}
				dqb.push(TIM(va[a].end+t));
				a++;
			}
			else 
			{
				
				if(dqb.size()&&dqb.top().tim<=vb[b].st)
				{
					dqb.pop();
				}
				else 
				{
					ansb++;
				}
				dqa.push(TIM(vb[b].end+t));
				b++;
			}
			if(a==A&&b==B) break;
		}
		printf("Case #%d: %d %d\n",test++,ansa,ansb);
	}	
	return 0;
}