#include<stdio.h>

int min(int x,int y)
{
	if(x<=y) return x;
	else return y;
}

int main()
{
	freopen("E:\\TDDOWNLOAD\\B-large.in","r",stdin);
	freopen("E:\\TDDOWNLOAD\\B-large.out","w",stdout);
	
	int T;
	scanf("%d\n",&T);
	for(int cse=1;cse<=T;cse++)
	{
		int n,s,p;
		scanf("%d%d%d",&n,&s,&p);
		
		int cur=0,pot=0;
		for(int i=1;i<=n;i++)
		{
			int x;
			scanf("%d",&x);
			if(x%3==0)
			{
				if(x/3>=p) cur++;
				else if(x/3>0&&x/3+1>=p) pot++;
				else ;
			}
			else if(x%3==1)
			{
				if(x/3+1>=p) cur++;
				else ;
			}
			else
			{
				if(x/3+1>=p) cur++;
				else if(x/3+2>=p) pot++;
				else ;
			}
		}
		
		//printf("cur %d pot %d\n",cur,pot);
		int ans=cur+min(s,pot);
		printf("Case #%d: %d\n",cse,ans);
	}
	return 0;
}
