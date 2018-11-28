#include <map>
#include <deque>
#include <iostream>
#include <fstream>
using namespace std;
deque<int> q1;
deque<int> q2;
	 
int exp(int n)
{
	int result = 0;
	while ((n/=10)>0)
	{
		result++;
	}
	result++;
	return result;
}

void num2Queue(int n, deque<int>& q)
{
	q.clear();
	while (n/10>0)
	{
		q.push_front(n%10);
		n/=10;
	}
	q.push_front(n%10);
}

int queue2Num(deque<int> q)
{
	int num=0;
	while (q.size()>0)
	{
		num=num*10+q.front();
		q.pop_front();
	}
	return num;
}

void turnQueue(deque<int>& q)
{
	int nail =q.back();
	q.pop_back();
	q.push_front(nail);
}

int calc(int n , int max)
{
	num2Queue(n,q1);
	int e = exp(n);
	int result = 0;
	for (int i = 1; i <e;i++)
	{
		turnQueue(q1);
		int m = queue2Num(q1);
		if (m>n&&m<=max)
		{
	//		cout<<n<<"\t"<<m<<endl;
			result++;
		}
	}
	return result;
}


void main()
{
	ifstream in("C:/data3.txt");
	ofstream out("C:/out.txt");


	int n= 0;
	in>>n;
	char result[1024];
	int min, max;
	for (int i = 1;i<=n;i++)
	{
		int count = 0;
		in>>min>>max;
		for (int j=min;j<=max;j++)
		{
			count+=calc(j,max);
		}
		sprintf(result,"Case #%d:%d\n",i,count);
		out<<result;
	}
	out.close();
	in.close();
}