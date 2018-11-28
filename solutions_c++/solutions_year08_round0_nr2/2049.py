#include<iostream>
#include<algorithm>
using namespace std;

char timebeg[300],timeend[300];
int flag[300];
typedef struct node
{
	int start,end;
	int side;
}node;
node tr[300];
int cmp(node a,node b)
{
	if(a.start==b.start&&a.end<b.end||a.start<b.start) return 1;
	return 0;
}
int timevalue(char a[300])
{
	
	return ((a[0]-'0')*10+a[1]-'0')*60+(a[3]-'0')*10+a[4]-'0';
}
int num;
int main()
{
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
	int e;
	int n;
	int T;
	int i;
	int j;
	int stas;
	int newp;
	int nowside;
	int na,nb,nsum;
	scanf("%d",&n);
	for(e=1;e<=n;e++)
	{

		int ans0=0,ans1=0;
		j=0;	
		memset(flag,0,sizeof(flag));
		scanf("%d%d%d",&T,&na,&nb);
		nsum=na+nb;
        for(i=0;i<na;i++)
		{	
			tr[++j].side=0;
			scanf("%s%s",timebeg,timeend);
			tr[j].start=timevalue(timebeg);
			tr[j].end=timevalue(timeend);
		
		}
	
        for(i=0;i<nb;i++)
		{			
			tr[++j].side=1;
			scanf("%s%s",timebeg,timeend);
			tr[j].start=timevalue(timebeg);
			tr[j].end=timevalue(timeend);

		}
		
		sort(tr+1,tr+nsum+1,cmp);
		num=0;

		while(1)
		{
			for(i=1;i<=nsum;i++)
				if(flag[i]==0)
				{
					
					if(tr[i].side==0)
						ans0++;
					else ans1++;

					flag[i]=1;
					nowside=tr[i].side;
					nowside=nowside^1;
					stas=tr[i].end;
					newp=i+1;

                   while(1)
				   {
						
						bool used=false;
						j=newp;
						while(j<=nsum)
						{
							if(flag[j]==0)
							{
								if(stas+T>tr[j].start||tr[j].side!=nowside) 
								{ j++;continue;}
								used=true;
								nowside=nowside^1;
								newp=j+1;
								flag[j]=1;
								stas=tr[j].end;
							    
								break;

							}
							j++;
						}
							if(used!=true)
								break;

				   }

				}
				int ok=0;
				for(i=1;i<=nsum;i++)
					if(flag[i])ok++;
				if(ok>=nsum)
					break;
				
		}
		printf("Case #%d: %d %d\n",e,ans0,ans1);
	}
	return 0;
}