#include<iostream>
#include<queue>
#include<fstream>
using namespace std;
int main()
{
	int t=0,i=0,j=0,round1=0,max1=0,t1=0,temp=0,sum=0,a=0,cost=0,m=0,count=0;
	queue<int> v;
	ifstream fin("C-small-attempt1.in");
	ofstream fout("outputl.in");
	//cin>>t;
	fin>>t;
	for(j=1;j<=t;j++)
	{
		cost=0;
		//cin>>round1>>max1>>t1;
		fin>>round1>>max1>>t1;
		for(i=0;i<t1;i++)
		{
			//cin>>a;
			fin>>a;
			v.push(a);
		}
		for(m=1;m<=round1;m++)
		{
			sum=v.front();
			count=0;
			//cout<<t1<<"\n";
			while(sum<=max1)
			{	
				count++;
				temp=v.front();
				v.pop();
				
				v.push(temp);
				sum+=v.front();
				if(count==t1)
					break;
			}
			sum-=v.front();
			cost+=sum;
			//cout<<sum<<"\n";
		}
		fout<<"Case #"<<j<<": "<<cost<<"\n";
		while(!v.empty()) 
			v.pop();
	}
}			
		
	
