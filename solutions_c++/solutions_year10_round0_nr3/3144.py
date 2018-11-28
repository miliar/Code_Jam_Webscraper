#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
int main()
{
	int T;
	int t;
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	fin>>T;
	for(t=1;t<=T;t++)
	{
		int i,j;
		int r,k,n;
		int l1=0,l2=0;
		int total=0;
		int times=0;
		int sum=0;
		int g[1000];
		int add[1000]={0};
		bool used[1000]={0};
		fin>>r>>k>>n;
		for(i=0;i<n;i++)
		{		
			fin>>g[i];
			total+=g[i];
		}
		fout<<"Case #"<<t<<": ";
		if(total<=k)
		{
			fout<<r*total<<endl;
		}
		else
		{
			i=0;
			while(!used[i])
			{
				used[i]=true;
				total=0;
				while(total+g[i]<=k)
				{
					total+=g[i];
					i=(i+1)%n;
				}
			}
			j=i;
			i=0;
			memset(used,0,sizeof(used));
			bool p=false;
			while(times<r && !used[i])
			{
				used[i]=true;
				if(i==j)
					p=true;
				total=0;
				while(total+g[i]<=k)
				{
					total+=g[i];
					i=(i+1)%n;
				}
				if(p)
				{
					add[l2]=total;
					l2++;
				}
				else
				{
					sum+=total;
					l1++;
				}
				times++;
			}
			total=0;
			for(i=0;i<l2;i++)
				total+=add[i]; 
			if(r>l1)
			{
				sum+=(total)*((r-l1)/l2);
				for(i=0;i<(r-l1)%l2;i++)
					sum+=add[i];
			}
			fout<<sum<<endl;
		}
	}
	return 0;
}
