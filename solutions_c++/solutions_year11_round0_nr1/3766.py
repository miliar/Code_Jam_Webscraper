#include<stdio.h>
#include<string.h>
int a[102],b[102],c[102][2];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout); 
	int t,n,i,j,k,x,sum,ans,pos1,pos2,pos3,cas=0;
	char s[2];
	scanf("%d",&t);
	while(t--)
	{
		cas++;
		sum=0; ans=0;
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		memset(c,0,sizeof(c));
		scanf("%d",&n);
		pos1=1; pos2=1;
		for(i=1;i<=n;i++) 
		{
			scanf("%s%d",&s[0],&x);
			//if(ans<x) ans=x;
			
			if(strcmp(s,"O")==0)
			{
				a[pos1++]=x;
				c[i][0]=0;
				c[i][1]=x;
			}
			else 
			{
				b[pos2++]=x;
				c[i][0]=1;
				c[i][1]=x;
			}
		}
		//for(i=1;i<=n;i++) printf("%d %d\n",c[i][0],c[i][1]);
		pos1=1; pos2=1;  pos3=1; ans=n;
		i=1; j=1;
		while(ans>0)
		{
			if(c[pos3][0]==0 && c[pos3][1]==i) 
			{
				ans--;
				sum++;
				pos1++;
				pos3++;	
				if(b[pos2] && b[pos2]>j) j++;
				else if(b[pos2] && b[pos2]<j) j--;
			}
			else if(c[pos3][0]==1 && c[pos3][1]==j )
			{
				ans--;
				sum++;
				pos2++;
				pos3++;
				if(a[pos1] && a[pos1]>i) i++;
				else if(a[pos1] && a[pos1]<i) i--;
			}
			else 
			{
				if(b[pos2] && b[pos2]>j) j++;
				else if(b[pos2] && b[pos2]<j) j--;
				if(a[pos1] && a[pos1]>i) i++;
				else if(a[pos1] && a[pos1]<i) i--;
				sum++;
			}
		}
		printf("Case #%d: %d\n",cas,sum);	
			
	}
}	