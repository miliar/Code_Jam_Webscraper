#include<cstdio>
#include<iostream>
#include<cstdlib>
using namespace std;

int main()
{
	int t,n;
	scanf("%d",&t);
	FILE* pFile=fopen("11.out","w");
	for(int c=1;c<=t;c++)
	{
		int time=0,bpos=1,opos=1,pbpos=1,popos=1;
		char bot[2];int but;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%s %d",bot,&but);
			if(bot[0]=='O')
			{
				int tmp=0;
				if(abs(but-popos)-abs(opos-popos)>0) tmp=abs(but-popos)-abs(opos-popos);
				popos=opos=but;
				time+=tmp+1;
				bpos+=tmp+1;
			}
			else 
			{
				int tmp=0;
				if(abs(but-pbpos)-abs(bpos-pbpos)>0) tmp=abs(but-pbpos)-abs(bpos-pbpos);
				pbpos=bpos=but;
				time+=tmp+1;
				opos+=tmp+1;
			}
		}
		fprintf(pFile,"Case #%d: %d\n",c,time);
	}
	return 0;
}