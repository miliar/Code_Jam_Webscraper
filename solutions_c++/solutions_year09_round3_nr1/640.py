#include<stdio.h>
#include<algorithm>
#include<stdlib.h>
#include<iostream>

#include<string>
#include<vector>
#include<stack>
using namespace std;




char ch[100];
int len;
int ji[100];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	 
    int t;
	scanf("%d",&t);
	int i,j,k;
	
    for(k=1;k<=t;k++)
	{
	    scanf("%s",ch);
		len=strlen(ch);
		printf("Case #%d: ",k);
		if(len==1)
		{
		   puts("1");
		   continue;
		}
        int sum=0;
		for(i=0;i<len;i++)
		{
		    for(j=0;j<i;j++)
				if(ch[i]==ch[j])
					break;
			if(j<i)
				continue;
			sum++;
		} 
        ji[0]=1;
		for(i=1;i<len;i++)
		{
		    if(ch[i]==ch[i-1])
				ji[i]=1;
			else
				break;
		}
		int kk;
		if(i<len)
		{
		   ji[i]=0;
		   i++;
		   kk=2;
		   while(i<len)
		   {
		      
              for(j=0;j<i;j++)
			  {
			      if(ch[i]==ch[j])
					  break;
			  }
			  if(j<i)
			  {
			     ji[i]=ji[j];
			  }
			  else
				 ji[i]=kk++;
			  i++;
		   }
		}
		if(sum==1)
			sum++;
		__int64 fang=1;
		__int64 ans=0;
		for(i=len-1;i>=0;i--)
		{
		    ans+=ji[i]*fang;
            fang*=sum;
		}
		printf("%I64d\n",ans);
	}
    return 0;
}