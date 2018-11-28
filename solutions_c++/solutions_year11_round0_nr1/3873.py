#include<cstdio>
#include<cassert>
char S[1024][4];
int t[1024];
int main()
{
	int X,kase=0;
	scanf("%d",&X);
	while(X--)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%s",S[i]);
			scanf("%d",&t[i]);
		}
		int bpos=1,apos=1;
		int topress;
		int time=0,tmp,idlea=0,idleb=0;
		char whom;
		for(int i=0;i<n;i++)
		{
			whom=S[i][0];
			topress=t[i];
			if(whom=='B')
			{
				tmp=topress-bpos;
				if(tmp<0)tmp*=-1;
				//tmp++;
				if(idleb>=tmp)
				{
					time++;
					idleb=0;
					idlea+=1;
				}
				else
				{
					tmp-=idleb;
					time+=tmp;
					idlea+=tmp;
					idlea++;
					time++;
					idleb=0;
				}
				bpos=topress;
			}
			if(whom=='O')
			{
				tmp=topress-apos;
				if(tmp<0)tmp*=-1;
				//tmp++;
				if(idlea>=tmp)
				{
					time++;
					idlea=0;
					idleb+=1;
				}
				else
				{
					tmp-=idlea;
					time+=tmp;
					idleb+=tmp;
					idleb++;
					idlea=0;
					time++;
				}
				apos=topress;
			}

//			printf("idlea is %d idleb is %d\n",idlea,idleb);
//			printf("time is %d\n",time);
		}
		kase++;
	//	if(kase==386)
	//	{
	//		for(int i=0;i<n;i++)printf("%c %d ",S[i][0],t[i]);
	//		puts("");
	//	}
	//	else continue;

		printf("Case #%d: %d\n",kase,time);

	}

}
