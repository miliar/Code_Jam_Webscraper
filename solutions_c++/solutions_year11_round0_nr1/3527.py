#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

#define read freopen("A-large.in","r",stdin)
#define write freopen("zx.out","w",stdout)
#define abs(a) ((a)>0 ? (a) : -(a))

int main()
{
	read, write;
	int ncase,mnum;
	scanf("%d",&ncase);
	for(int ii=1;ii<=ncase;ii++)
	{
		scanf("%d",&mnum);
		int t1=0,t2=0,sum=0;
		int cur_b=1,cur_o=1,curtime;
		char buf;
		for(int i=1;i<=mnum;i++)
		{
			cin>>buf>>curtime;
			if(buf=='O')
			{
				int temp=abs(curtime-cur_o);
				if(t1>=temp)
				{
					sum++; t2++;
				}
				else
				{
					sum+=temp-t1+1;
					t2+=temp-t1+1;
				}
				t1=0; cur_o=curtime;
			}
			else if(buf=='B')
			{
				int temp=abs(curtime-cur_b);
				if(t2>=temp)
				{
					sum++; t1++;
				}
				else
				{
					sum+=temp-t2+1;
					t1+=temp-t2+1;
				}
				t2=0; cur_b=curtime;
			}
		}
		printf("Case #%d: %d\n",ii,sum);
	}
	return 0;
}
