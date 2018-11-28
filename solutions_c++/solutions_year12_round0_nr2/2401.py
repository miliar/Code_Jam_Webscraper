#include<stdio.h>
int main()
{
    int zes;scanf("%d",&zes);
    for (int z=1;z<=zes;z++)
    {
	int p,n,s,sum;
	scanf("%d%d%d",&n,&s,&p);
	int res=0;
	for (int i=0;i<n;i++)
	{
	    scanf("%d",&sum);
	    if(sum%3==1)
	    {
		if(sum/3+1>=p) 
		{
		    res++;
		    continue;
		}
	    }else
	    if(sum%3==2)
	    {
		if(sum/3+1>=p) 
		{
		    res++;continue;
		}
		if(s>0)
		{
		    if(sum/3+2>=p)
		    {
			s--;res++;
		    }
		}
	    }
	    else
	    {
		if(sum/3>=p) {res++; continue;}
		if(s>0)
		{
		    if(sum>0 && sum/3+1>=p) { s--;res++;}
		}
	    }
	}
	printf("Case #%d: %d\n",z,res);
    }
}
