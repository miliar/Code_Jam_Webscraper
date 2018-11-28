#include<cstdio>
int main()
{
	int test,t=1;
	scanf("%d",&test);
	while(test--)
	{
		char ch[200]={'\0'},ans[200]={'\0'};
		int a[27][27]={0},b[27][27]={0},i,j,c,d,num;
		scanf("%d",&c);
		for(i=0;i<c;i++)
		{
			scanf("%s",ch);
			a[ch[0]-'A'][ch[1]-'A']=ch[2];
			a[ch[1]-'A'][ch[0]-'A']=ch[2];			
			ch[0]='\0';
		}
		scanf("%d",&d);
		for(i=0;i<d;i++)
		{
			scanf("%s",ch);
			b[ch[0]-'A'][ch[1]-'A']=1;
			b[ch[1]-'A'][ch[0]-'A']=1;
			ch[0]='\0';
		}
		scanf("%d",&num);
		scanf("%s",ch);
		int k=1,crr[28]={0};
		ans[0]=ch[0];
		crr[ch[0]-'A']=1;
		for(i=1;ch[i]!='\0';i++)
		{
			if(k==0)
				ans[k++]=ch[i];
			else if(a[ans[k-1]-'A'][ch[i]-'A'])
				ans[k-1]=a[ans[k-1]-'A'][ch[i]-'A'];
			else 
			{
				int check=0;
				for(j=0;j<k;j++)
				{
					if(check==0)
					{
						if(b[ch[i]-'A'][ans[j]-'A']==1 )
						{
							check=1;
							ans[j]='\0';
							k=j;
							break;
						}
					}
				}
				if(check==1)
				{
					k=0;
					ans[0]='\0';
				}
				else
				{
					ans[k++]=ch[i];
				}
			}
		}
		ans[k]='\0';
		printf("Case #%d: [",t++); 
		for(i=0;i<k-1;i++)
			printf("%c, ",ans[i]);
		if(k!=0)
			printf("%c]\n",ans[k-1]);
		else
			printf("]\n");
	}
	return 0;
}