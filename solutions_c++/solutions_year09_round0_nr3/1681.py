#include<cstdio>
#include<cstring>
char str[501];
char m[]="welcome to code jam";
int len,mLen;
int getNum(int start, int t)
{
if(t>=mLen)
	return 1;
if(start>=len)
	return 0;
int result=0,i,count;
for(i=start;i<len;++i)
	if(str[i]==m[t])
		{
		for(++i,count=1;i<len && str[i]!=m[t+1];++i)
			{
			if(str[i]==m[t]) 
				++count;
			}
		result=(result+count*getNum(i,t+1))%10000;
		}
return result;
}
int main()
{
int nT,t,i,j,count,result;
mLen=strlen(m);
scanf("%d",&nT);
getc(stdin);
for(t=1;t<=nT;++t)
	{
	result=0;
	gets(str);
	len=strlen(str);
	for(i=0;i<len;++i)
		{
		if(str[i]==m[0])
			{
			for(++i,count=1;i<len && str[i]!=m[1];++i)
				if(str[i]==m[0]) ++count;
			result=(result+count*getNum(i,1))%10000;
			}
		}
	printf("Case #%d: %04d\n",t,result);
	}
}