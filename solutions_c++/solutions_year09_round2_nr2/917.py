#include<stdio.h>
#include<algorithm>
#include<string>

using namespace std;


char in[50];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    
	int t;
	scanf("%d",&t);
    int i,j,k;
	for(k=1;k<=t;k++)
	{
	    scanf("%s",in);
	    int len=strlen(in);
		for(i=0;i<len;i++)
			in[i]-='0';
		printf("Case #%d: ",k);
        if(len==1)
		{
		   printf("%d0\n",in[0]);
		   continue;
		}
		for(i=1;i<len;i++)
		{
		    if(in[i]>in[i-1])
				break;
		}
        if(i==len)
		{
		   in[len++]=0;
		   sort(in,in+len);
		   for(i=0;i<len;i++)
		   {
		       if(in[i]!=0)
			   {
			      j=i;
				  break;
			   }
		   }
		   printf("%d",in[j]);
		   for(i=0;i<len;i++)
		   {
		       if(i==j)
				   continue;
			   printf("%d",in[i]);
		   }
		   puts("");
		}
		else
		{
		   for(i=len-1;;i--)
			   if(in[i]>in[i-1])
				   break;
		   j=i-1;
		   for(i=0;i<j;i++)
			   printf("%d",in[i]);
		   i=j;
		   j=in[j];
		   int ii=0;
		   
		   while(i<len)
		   {
		      in[ii++]=in[i];
			  i++;
		   }
		   len=ii;
           sort(in,in+len);
		   for(i=0;i<ii;i++)
		   {
		       if(in[i]>j)
			   {
			      j=i;
				  break;
			   }
		   }
		   printf("%d",in[j]);
		   for(i=0;i<len;i++)
		   {
		       if(i==j)
				   continue;
			   printf("%d",in[i]);
		   }
		   puts("");
		}
	}
    return 0;
}