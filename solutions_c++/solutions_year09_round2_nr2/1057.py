#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
bool judge(char a[],char b[])
{
	int len=strlen(a);
	int i,j;
	for(i=0,j=len-1;i<=j;i++,j--)
	{
		if(a[i]!=b[j])
			return false;
	}
	return true;
}
int main()
{
	freopen("inb2.in","r",stdin);
	freopen("outb2.txt","w",stdout);
	int i,j,len,t,temp,test=0;
	char s[205],str[205],a[205];
	scanf("%d",&t);
	while(t--)
	{
		scanf("%s",s);
		test++;
		strcpy(str,s);
		len=strlen(s);
		sort(s,s+len);
		printf("Case #%d: ",test);
		int lena=0,pos=0,max,pos1=0;
		if(judge(s,str))
		{
			for(i=0;i<len;i++)
			{
				if(s[i]!='0')
				{
					a[lena++]=s[i];
					pos=i;
					break;
				}
			}
			a[lena++]='0';
			for(i=0;i<len;i++)
			{
				if(i!=pos)
					a[lena++]=s[i];
			}
			a[lena]='\0';
			printf("%s\n",a);
		}
		else
		{
			bool flag=false;
			for(i=len-1;i>=0&&!flag;i--)
			{
				max=10;
				for(j=i+1;j<len;j++)
				{
					if(str[j]>str[i])
					{
						flag=true;
						temp=(str[j]-'0');
						if(temp<max)
						{
							pos=j;
							pos1=i;
							max=temp;
						}
					}
				}
			}
			i=0;lena=0;
			while(i<len)
			{
				if(i>=pos1)
				{
					s[pos1]=str[pos];
					for(j=pos1;j<len;j++)
					{
						if(j!=pos)
							a[lena++]=str[j];
					}
					a[lena]='\0';
					sort(a,a+lena);
					for(i=pos1+1,j=0;i<len;i++,j++)
						s[i]=a[j];
					break;
				}
				else
				{
					s[i]=str[i];
					i++;
				}
			}
			s[len]='\0';
			printf("%s\n",s);
		}
	}
    return 0;
}




