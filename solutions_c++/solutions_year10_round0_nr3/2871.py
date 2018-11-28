#include<iostream>
#include<queue>
#include<fstream>
using namespace std;
int main()
{
	long long int t=0,i=0,j=0,round1=0,max1=0,t1=0,temp=0,sum=0,a=0,cost=0,m=0,count=0;
	queue<long long int> v1;
	ifstream fin("C-small-attempt0.in");
	ofstream fout("small.in");
	//cin>>t;
	fin>>t;
	for(j=1;j<=t;j++)
	{
		cost=0;
		fin>>round1>>max1>>t1;
		for(i=0;i<t1;i++)
		{
			fin>>a;
			v1.push(a);
		}
		for(m=1;m<=round1;m++)
		{
			sum=v1.front();
			count=0;
			while(sum<=max1)
			{	
				count++;
				temp=v1.front();
				v1.pop();
				
				v1.push(temp);
				sum+=v1.front();
				if(count==t1)
					break;
			}
			sum-=v1.front();
			cost+=sum;
		}
		fout<<"Case #"<<j<<": "<<cost<<"\n";
		while(!v1.empty()) 
			v1.pop();
	}
}			
		
	
