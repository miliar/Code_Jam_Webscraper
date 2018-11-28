#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

//1 add,2 sub
struct Event
{
	int time;int flag;
};

int compare(const void * event1,const void *event2)
{
	const Event* e1=(const Event*)event1;
	const Event* e2=(const Event*)event2;
	if(e1->time!=e2->time)
		return (e1->time-e2->time);
	else
		return (e1->flag-e2->flag);
}

Event A[300];
Event B[300];

int trans(string& tim)
{
	int time2=0;
	time2=((tim[0]-'0')*10+tim[1]-'0')*60+(tim[3]-'0')*10+tim[4]-'0';
	return time2;
}


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int N,i,j,needA,needB,index1,index2,trainA,trainB,time2,turn,NA,NB;
	string tim;
	cin>>N;
	for(i=1;i<=N;i++)
	{
		trainA=trainB=index1=index2=needA=needB=0;
		cin>>turn;
		cin>>NA>>NB;
		for(j=1;j<=NA;j++)
		{
			cin>>tim;
			time2=trans(tim);
			A[index1].time=time2;
			A[index1].flag=2;
			cin>>tim;
			time2=trans(tim)+turn;
			B[index2].time=time2;
			B[index2].flag=1;
			index1++;
			index2++;
		}
		for(j=1;j<=NB;j++)
		{
			cin>>tim;
			time2=trans(tim);
			B[index2].time=time2;
			B[index2].flag=2;
			cin>>tim;
			time2=trans(tim)+turn;
			A[index1].time=time2;
			A[index1].flag=1;
			index1++;
			index2++;
		}
		qsort(A,index1,sizeof(Event),compare);
		qsort(B,index2,sizeof(Event),compare);
		for(j=0;j<index1;j++)
		{
			if(A[j].flag==1)
				trainA++;
			else
			{
				if(trainA==0)
				{
					trainA++;
					needA++;
				}
				trainA--;
			}
		}
		for(j=0;j<index2;j++)
		{
			if(B[j].flag==1)
				trainB++;
			else
			{
				if(trainB==0)
				{
					trainB++;
					needB++;
				}
				trainB--;
			}
		}
		cout<<"Case #"<<i<<": "<<needA<<" "<<needB<<endl;
	}
	return 0;
}