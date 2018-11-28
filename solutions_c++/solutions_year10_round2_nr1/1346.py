#include<iostream>
#include<cmath>
#include<cstdio>
#include<string.h>
using namespace std;



int main()
{
	freopen("c:\\2.in","r",stdin);
	freopen("c:\\out2.txt","w",stdout);

	typedef struct 
	{
		int n;
		int p[100];
		char ch[100];

	}JG;

	int  n,m,k,t;
	cin>>t;

	for(k=1;k<=t;k++)
	{
		JG jg[300];
		int max=0;
		jg[0].n=0;

		int i,j;
		char tem[100];
		cin>>n>>m;
		for(i=0;i<n;i++)
		{
			scanf("%s",tem);
			int point=0;
			int now=1;
			while(now<strlen(tem))
			{
				char chs[50];
				int chsp=0;
				while((tem[now]!='/')&&(now<strlen(tem)))
				{
					chs[chsp++]=tem[now++];
				}
				chs[chsp]='\0';

				int s;
				bool found=false;
				int uu;
				for(s=0;s<jg[point].n;s++)
					if(strcmp(chs,jg[jg[point].p[s]].ch)==0)
					{
						uu=jg[point].p[s];
						found=true;
						break;

					}
				if(found)
				{
					//cout<<"找到"<<chs<<"前往"<<uu<<endl;
					point=uu;
				}
				else
				{
					
					jg[point].p[jg[point].n++]=++max;
					strcpy(jg[max].ch,chs);
					jg[max].n=0;
					point=max;
					//cout<<"未找到"<<chs<<"添加"<<max<<endl;
				}
			now++;

			}
			

		}
		int sum=0;
		for(j=1;j<=m;j++)
		{
			scanf("%s",tem);
			int point=0;
			int now=1;
			while(now<strlen(tem))
			{
				char chs[50];
				int chsp=0;
				while((tem[now]!='/')&&(now<strlen(tem)))
				{
					chs[chsp++]=tem[now++];
				}
				chs[chsp]='\0';

				int s;
				bool found=false;
				int uu;
				for(s=0;s<jg[point].n;s++)
					if(strcmp(chs,jg[jg[point].p[s]].ch)==0)
					{
						
						
						uu=jg[point].p[s];
						found=true;
						break;

					}
				if(found)
				{
					//cout<<"找到"<<chs<<"前往"<<uu<<endl;
					point=uu;
				}
				else
				{
					
					jg[point].p[jg[point].n++]=++max;
					strcpy(jg[max].ch,chs);
					jg[max].n=0;
					point=max;
					sum++;
					//cout<<"未找到"<<chs<<"添加"<<max<<endl;
				}
			now++;

			}

		}
		cout<<"Case #"<<k<<": "<<sum<<endl;
	}

return 0;
}
