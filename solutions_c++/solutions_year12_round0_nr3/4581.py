#include<iostream>
#include<fstream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
#include<string>
#include<map>
#include<limits.h>

using namespace std;

int que2num(queue<int> que)
{
	int n=que.size(),num=0;
	for ( int i = n-1; i >=0; i-- )
	{
		num+=que.front()*pow(10,i);que.pop();
	}
	return num;
}

int retVal(int x,int A,int B)
{
	int ret=0,tmp=x;
	map<int,bool> seen;
	
	stack<int> stac;queue<int> que;
	
	//extract digits
	
	while(tmp>0)
	{
		stac.push(tmp%10);tmp/=10;
	}
	while(!stac.empty())	{que.push(stac.top());stac.pop();}
	
	// x is in que
	int a=x;
	//cout<<"\t";
	while(seen[a]!=true)
	{
		seen[a]=true;
		//cout<<a<<" ";
		a=que.front();que.pop();que.push(a);
		a=que2num(que);
		
		if(A<=x && x<a && a<=B)	ret++;
		
	}
	
	return ret;
}
int main (int argc, char const* argv[])
{
	int n=0,A,B,ans=0;
	queue<int> que;
	ifstream cin("/home/ash/Downloads/C-small-attempt0.in");
	ofstream file("output.txt");
	
	cin>>n;
	//*
	for ( int p = 0; p < n; p++ )
	{
		cin>>A>>B;
		ans=0;
		for ( int i = A; i <= B; i++ )
		{
			//cout<<"i: "<<i;
			ans+=retVal(i,A,B);
			//cout<<" ans: "<<ans<<endl;
		}
		file<<"Case #"<<p+1<<": "<<ans<<endl;
		
	}
	//*/
	return 0;
}
