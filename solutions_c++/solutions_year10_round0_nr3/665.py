// Theme Park(gcj2010).cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
using namespace std;
	int a[1001][2];
	int m[1001];
	bool visit[1001];
int main()
{
	int ts,r,k,n,bk,rk,rp,count,rcount,incount;
	long long sum,bsum,rsum;
	fstream f("d:\\gcj\\C-large.in");
	fstream of("d:\\gcj\\A-small.out");
	if(f!=NULL)
	{
		f>>ts;
		for(int t=1;t<=ts;t++)
		{
			f>>r>>k>>n;
			for(int i=0;i<n;i++)
			{
				f>>m[i];
				visit[i]=false;
			}
			for(int i=0;i<n;i++)
			{
				int j=i;
				sum=m[i];
				while(1)
				{
					j++;
					j=j%n;
					if(j==i)
					{
						j--;
						if(j==-1)
							j=n-1;
						break;
					}
					sum+=m[j];
					if(sum>k)
					{
						sum-=m[j];
						j--;
						if(j==-1)
							j=n-1;
						break;
					}
				}
				a[i][0]=sum,a[i][1]=(j+1)%n;
			}
			visit[0]=true;
			for(int i=0;;)
			{
				visit[i]=true;
				if(visit[a[i][1]]==true)
				{
					rp=a[i][1];
					break;
				}
				else
					i=a[i][1];
			}
			bsum=0;
			bk=0;
			for(int i=0;;)
			{
				if(i!=rp)
				{
					bsum+=a[i][0];
					i=a[i][1];
					bk++;
				}
				else
					break;
			}
			rsum=0;
			rk=0;
			int is=rp;
			while(1)
			{
				rsum+=a[is][0];
				rk++;
				is=a[is][1];
				if(is==rp)
					break;
			}
	
			count=0;
			sum=0;
			if(bk>=r)//不用进入环
			{
				
				for(int i=0;;)
				{
					if(i!=rp)
					{
						sum+=a[i][0];
						count++;
						if(count>=k)
							break;
					}
				}
			}
			else//进入环
			{
				sum=bsum;
				r-=bk;
				rcount=r/rk;
				sum+=rsum*rcount;
				incount=r%rk;
				is=rp;
				while(incount>0)
				{
					sum+=a[is][0];
					is=a[is][1];
					incount--;
				}
			}
			of<<"Case #"<<t<<": "<<sum<<endl;
		}
	}
	return 0;
}

