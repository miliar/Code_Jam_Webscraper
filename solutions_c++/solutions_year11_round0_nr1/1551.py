#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

struct MyStruct
{
	char c;
	int b;
};

int cal(MyStruct * myStruct,int n);

int main()
{
	
	ifstream fin("..\\A-large.in");
	ofstream fout("..\\A-large.out");

	int testNum;
	fin>>testNum;

	for(int i=1;i<=testNum;i++)
	{
		int  n;
		fin>>n;
		MyStruct * myStruct=new MyStruct[n];
		for(int j=0;j<n;j++)
		{
			fin>>myStruct[j].c;
			fin>>myStruct[j].b;
		}
		
		fout<<"Case #"<<i<<": "<<cal(myStruct,n)<<endl;
		cout<<"Case #"<<i<<": "<<cal(myStruct,n)<<endl;

	}

	return 0;
}

int cal(MyStruct * myStruct,int n)
{
	char last=myStruct[0].c;
	int OPoint=1,BPoint=1;
	int point[2]={1,1};
	int totalTime=0,lastTime=0;
	for(int i=0;i<n; i++)
	{
		int nowTime=0;
		int index=0;
		if(last!=myStruct[i].c)
		{
			last=myStruct[i].c;
			if(myStruct[i].c=='O')
				index=0;
			else
				index=1;
			if(abs(myStruct[i].b-point[index])<=lastTime)
			{
				totalTime++;
				lastTime=1;
				point[index]=myStruct[i].b;
			}
			else
			{
				totalTime=totalTime+abs(myStruct[i].b-point[index])-lastTime+1;
				lastTime=abs(myStruct[i].b-point[index])-lastTime+1;
				point[index]=myStruct[i].b;
			}
			last=myStruct[i].c;
		}
		else
		{
			int index=0;
			if(myStruct[i].c=='O')
				index=0;
			else
				index=1;
			lastTime=lastTime+abs(myStruct[i].b-point[index])+1;
			totalTime=totalTime+abs(myStruct[i].b-point[index])+1;
			last=myStruct[i].c;
			point[index]=myStruct[i].b;
		}
	}

	return totalTime;
}