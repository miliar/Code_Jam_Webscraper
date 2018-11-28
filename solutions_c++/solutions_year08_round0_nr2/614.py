#include<iostream>
#include<queue>
#include<deque>
using namespace std;
struct Time
{
	int hour,minute;
	Time(){}
	Time(int t1,int t2):hour(t1),minute(t2){}
	bool operator ==(const Time &a)const
	{
		if(hour==a.hour&&minute==a.minute)
			return true;
		return false;
	}
	bool operator <(const Time &a) const
	{
		if(hour==a.hour)
			return minute>a.minute;
		else
			return hour>a.hour;
	}
};
struct Station
{
	Time start , end;
	Station(){}
	Station(int t1,int t2,int t3,int t4)
	{
		start.hour=t1;start.minute=t2;
		end.hour=t3;end.minute=t4;
	}
	bool operator ==(const Station &a) const
	{
		if(a.start==start&&a.end==end)	return true;
		return false;
	}
	bool operator < (const Station & a) const
	{
		if(a.start.hour==start.hour)
			return start.minute>a.start.minute;
		else return start.hour>a.start.hour;
	}
};

priority_queue<Station> dq1,dq2;
priority_queue<Time> car1,car2 ;
void Init()
{
	while(!dq1.empty())
		dq1.pop();
	while(!dq2.empty())
		dq2.pop();
	while(!car1.empty())
		car1.pop();
	while(!car2.empty())
		car2.pop();
}
void Get_Table(char str1[], char str2[],int num)
{
	int hour1=0,minuter1=0,hour2=0,minuter2=0;
	hour1 = (str1[0]-'0')*10+str1[1]-'0';
	minuter1 = (str1[3]-'0')*10+str1[4]-'0';

	hour2 = (str2[0]-'0')*10+str2[1]-'0';
	minuter2 = (str2[3]-'0')*10+str2[4]-'0';
	if(num==1)
		dq1.push(Station(hour1,minuter1,hour2,minuter2));
	else
		dq2.push(Station(hour1,minuter1,hour2,minuter2));
}
int main()
{

	int N ,cases , t ;
	int Na , Nb ;
	int i , j , k ;
	char str1[111],str2[111];	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	while( 1 ==scanf("%d",&N))
	{
		for(cases=1;cases<=N;cases++)
		{
			Init();
			scanf("%d",&t);
			scanf("%d%d",&Na,&Nb);
			for(i=0;i<Na;i++)
			{
				scanf("%s%s",str1,str2);
				Get_Table(str1,str2,1);
			}
			for(i=0;i<Nb;i++)
			{
				scanf("%s%s",str1,str2);
				Get_Table(str1,str2,2);
			}
			Time S , T  ;
			int ans1=0,ans2=0;
			while(dq1.size()||dq2.size())
			{

				if(dq1.empty())
				{
					while(dq2.size())
					{
						S=dq2.top().start;T=dq2.top().end;
						dq2.pop();
						if(car2.empty())
							ans2++;
						else
						{
							if(car2.top()<S)
								ans2++;
							else
								car2.pop();
						}
					}
					
				}
				else
				if(dq2.empty())
				{
					while(dq1.size())
					{
						S=dq1.top().start;T=dq1.top().end;
						dq1.pop();
						if(car1.empty())
							ans1++;
						else
						{
							if(car1.top()<S)
								ans1++;
							else
								car1.pop();
						}
					}
				}
				else

				if(!(dq1.top()<dq2.top()))
				{
					S= dq1.top().start,T=dq1.top().end;
					dq1.pop();
					if(car1.empty())
						ans1 ++;
					else
					{
						if(car1.top()<S)	ans1++;
						else car1.pop();
					}
					car2.push(Time(T.hour+(T.minute+t)/60,(T.minute+t)%60));
				}
				else
				{
					S= dq2.top().start,T=dq2.top().end;
					dq2.pop();
					if(car2.empty())
						ans2 ++;
					else
					{
						if(car2.top()<S)	ans2++;
						else	car2.pop();
					}
					car1.push(Time(T.hour+(T.minute+t)/60,(T.minute+t)%60));
				}
			}
			cout<<"Case #"<<cases<<": "<<ans1<<" "<<ans2<<endl;
		}
	}

	return 0  ;
}