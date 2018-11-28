
#include<stdio.h>
#include<string.h>
int k1,k2;
char str[105];
int l1[27][50],l2[27][50],res[105];
int main()
{
	int a,b,c,t,n,i,j,l,h,ca=1;
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: [",ca++);
		memset(l1,0,sizeof(l1));
		memset(l2,0,sizeof(l2));
		scanf("%d",&k1);
		for(i=0;i<k1;i++)
		{
			scanf("%s",str);
			a=str[0]-'A';
			b=str[1]-'A';
			c=str[2]-'A';
			l1[a][b]=l1[b][a]=c;
		}
		scanf("%d",&k2);
		for(i=0;i<k2;i++)
		{
			scanf("%s",str);
			a=str[0]-'A';
			b=str[1]-'A';
			l2[a][b]=l2[b][a]=1;
			//printf("a:%d b:%d \n",a,b);
		}
		scanf("%d",&n);
		scanf("%s",str);
		for(j=i=0;i<n;i++)
		{
			//printf("i:%d j:%d \n",i,j);
			a=str[i]-'A';
			if(!j)
			{
				res[j++]=a;
				continue;
			}
			b=res[j-1];
			while(l1[a][b])
			{
				a=l1[a][b];
				j--;
				if(!j)break;
				b=res[j-1];
			}
			if(!j)
			{
				res[j++]=a;
				continue;
			}
			for(h=1,l=j-1;l>=0;l--)
			{
				b=res[l];
				//printf("a:%d b:%d \n",a,b);
				if(l2[a][b])
				{
					h=0;j=0;break;
				}
			}
			if(h)res[j++]=a;
		}
		if(j)printf("%c",res[0]+'A');
		for(i=1;i<j;i++)
			printf(", %c",res[i]+'A');
		puts("]");
	}
}
