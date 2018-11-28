#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
bool used[100];
char s[100];
int a[100];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("outa2.txt","w",stdout);
	int i,j,t,n=0;
	scanf("%d",&t);
	while(t>0)
	{
	    t--;
	    scanf("%s",s);
	    n++;
	    long long sum=0,max=0;
	    memset(used,0,sizeof(used));
	    int len=strlen(s),pos=1;
	    printf("Case #%d: ",n);
	    for(i=0;i<len;i++)
	    {
             if(used[i]) continue;
             used[i]=1;
             a[i]=pos;
             if(pos>max)
             {
                max=pos;
             }
	         for(j=i+1;j<len;j++)
	         {
	             if(s[j]==s[i])
	             {
	                a[j]=pos;
	                used[j]=1;
	             }
	         }
	         if(pos==1)
	         {
                 pos=0;
             }
             else if(pos==0)
             {
                 pos=2;
             }
             else
             {
                pos++;
             }
	    }
	    max++;
	    for(i=0;i<len;i++)
	    {
	        sum=sum*max+a[i];
	    }
	    printf("%lld\n",sum);
	}
    return 0;
}




