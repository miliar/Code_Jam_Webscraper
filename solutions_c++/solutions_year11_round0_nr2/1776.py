#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
char change[50][4],clear[50][3],str[999];
char temp[10],arr[999];
char find_change(char a,char b,int c)
{
	int i=0;
	for(i=0;i<c;i++)
	{
		if((change[i][0]==a && change[i][1]==b) || (change[i][0]==b && change[i][1]==a))
		{
			return change[i][2];
		}
	}	
	return 0;
}
bool find_clear(char a,char b,int d)
{
	int i=0;
	for(i=0;i<d;i++)
	{
		if((clear[i][0]==a&&clear[i][1]==b) || (clear[i][0]==b&&clear[i][1]==a))
		{
			return true;
		}
	}
	return false;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++)
	{
		int c,d,n,i,j;
		scanf("%d",&c);
		memset(arr,0,sizeof(arr));
		for(i=0;i<c;i++)
		{
			scanf("%s",temp);
			change[i][0]=temp[0];
			change[i][1]=temp[1];
			change[i][2]=temp[2];
		}
		scanf("%d",&d);
		for(i=0;i<d;i++)
		{
			scanf("%s",temp);
			clear[i][0]=temp[0];
			clear[i][1]=temp[1];
		}
		scanf("%d%s",&n,str);
		char ch;
		for(i=0,j=0;i<n;i++)
		{
			arr[j]=str[i];
			j++;
			if(j>1)
			{
				while((ch=find_change(arr[j-1],arr[j-2],c)))
				{
					j-=1;
					arr[j-1]=ch;
					arr[j]=arr[j+1]=0;
					if(j<=1)break;
				}
			}
			if(j>1 && d)
			{
				int k,h;
				for(k=0;k<j;k++)
				{
					for(h=k+1;h<j;h++)
					{
						if(find_clear(arr[k],arr[h],d))
						{
							j=0;
							arr[j]=0;
							memset(arr,0,sizeof(arr));
							break;
						}
					}
					if(j==0)break;
				}
			}
		}
		int l=strlen(arr);
		printf("Case #%d: [",test);
		for(i=0;i<l-1;i++)
			printf("%c, ",arr[i]);
		if(l>0)
		printf("%c]\n",arr[i]);
		else
		printf("]\n",arr[i]);
	}
	return 0;
}
