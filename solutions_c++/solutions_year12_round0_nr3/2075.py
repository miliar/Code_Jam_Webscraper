/*************************************************************************
    > File Name: C.cpp
    > Author: mawenxuan
    > Mail: mawenxuan618@gmail.com 
    > Created Time: 日  4/15 00:21:07 2012
 ************************************************************************/

#include<cstdio>
#include<cstring>
using namespace std;
int strtonum(char * s,int l)
{
	int ret=0;
	for (int i=0;i<l;i++)
	{
		ret*=10;
		ret+=s[i]-'0';
	}
	return ret;
}
bool noLeadingZeros(int num,int l)
{
	char s[20];
	sprintf(s,"%d",num);
	if (strlen(s)!=l)return false;
	return true;
}
int solve(int a,int b)
{
	int ans=0;
	char str[20];
	char nowstr[20];
	int nownum,len;
	int numlist[20],count;
	for (int num=a;num<=b;num++)
	{
		count=1;
		numlist[0]=num;
		memset(str,0,sizeof(str));
		sprintf(str,"%d",num);
		len=strlen(str);
		nownum=num;
		memcpy(nowstr,str,len);
		for (int j=1;j<len;j++)
		{
			char temp=nowstr[0];
			for (int k=1;k<len;k++)nowstr[k-1]=nowstr[k];
			nowstr[len-1]=temp;
			nownum=strtonum(nowstr,len);
			if (noLeadingZeros(nownum,len)&&nownum>num&&nownum>=a&&nownum<=b)
			{
				bool flag=true;
				for (int k=0;k<count;k++)
				if (numlist[k]==nownum)
				{
					flag=false;
					break;
				}
				if (flag)
				{
					ans++;
					numlist[count]=nownum;
					count++;
				}
			}
		}
/*		if (count>1)
		{
			for (int k=0;k<count;k++)
				fprintf(stderr,"%d ",numlist[k]);
			fprintf(stderr,"\n");
		}
*/
	}
	return ans;
}
int main()
{
	int T;
	int A,B;
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		scanf("%d %d",&A,&B);
		printf("Case #%d: %d\n",i+1,solve(A,B));
	}
	return 0;
}
