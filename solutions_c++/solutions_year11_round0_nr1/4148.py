#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<stack>
#include<cstring>
#include<cstdio>
#include<map>
#include<cstdlib>
#include<fstream>
#include<queue>
using namespace std;
int f1[1000],f2[1000],t1[1000],t2[1000],s[1000];
int main()
{
	#if 1
	freopen("1.in","r",stdin);
	freopen("1.out","w+",stdout);
	#endif
	int test,len1,len2,len;
	int temp;
	int i,j,k,t,n;
	int time1,time2,time,p1,p2;
	string str;
	scanf("%d",&t);
	for (test=1;test<=t;test++)
	{
		cin>>n;	
		len1=0;
		len2=0;
		len=0;
		for (i=0;i<n;i++)
		{
			cin>>str;
			scanf("%d",&temp);
		
			if (str=="O")  
			{
				f1[len1++]=temp;
				s[len++]=1;
			}
			else 
			{
				f2[len2++]=temp;
				s[len++]=2;
			}
		}
		t1[0]=f1[0];
		t2[0]=f2[0];
		for (i=1;i<len1;i++)
			t1[i]=abs(f1[i]-f1[i-1])+1;
		for (i=1;i<len2;i++)
			t2[i]=abs(f2[i]-f2[i-1])+1;
		time1=0;
		time2=0;
		time=0;
		p1=0;
		p2=0;
		if (s[0]==1) 
		{
			time=t1[0];
			time1=time;
			p1++;
		}
		else 
		{
			time=t2[0];
			time2=time;
			p2++;
		}
		for (i=0;i<len-1;i++)
			if (s[i]==1&&s[i+1]==1)
			{
				time+=t1[p1];
				time1+=t1[p1];
				p1++;
			}
			else if (s[i]==2&&s[i+1]==2)
			{
				time+=t2[p2];
				time2+=t2[p2];
				p2++;
			}
			else if (s[i]==1&&s[i+1]==2)
			{
				if (time<time2+t2[p2])
				{
					time=time2+t2[p2];
					time2=time;
					p2++;
				}
				else 
				{
					time++;
					time2=time;
					p2++;
				}
			}
			else if (s[i]==2&&s[i+1]==1)
			{
				if (time<time1+t1[p1])
				{
					time=time1+t1[p1];
					time1=time;
					p1++;
				}
				else 
				{
					time++;
					time1=time;
					p1++;
				}
			}
			printf("Case #%d: %d\n",test,time);
	}
	return 0;
}