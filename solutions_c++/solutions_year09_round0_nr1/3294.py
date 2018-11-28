#include<stdio.h>
#include<string.h>
char ch[10000][50],ch1[10000000];
int main()
{
    long a,b,c,cas=0,i,j,h,k,res,s[20][300],m;
	
	scanf("%ld%ld%ld",&a,&b,&c);
	{
		for(i=1;i<=b;i++)
		scanf("%s",ch[i]);

		cas=0;
		for(i=1;i<=c;i++)
		{
		    cas+=1;
		    scanf("%s",ch1);
           for(h=1;h<=15;h++)
		   for(j=50;j<=145;j++)
		   s[h][j]=0;

		 k=0;
		
         for(j=0;j<strlen(ch1);j++)
		 {
		 
							  if(ch1[j]=='(')
							  {
								j=j+1;
								k=k+1;
								while(ch1[j]!=')')
							   {
								s[k][ch1[j]]=1;
								j++;
							   }
							  }
							   else
							   {
									  if(ch1[j]>='a'&&ch1[j]<='z')
									  {
									  k=k+1;
									  s[k][ch1[j]]=1;
									  }
							   }
		 }

		 

		   res=0;
		   for(h=1;h<=b;h++)
		   {
			m=0;
		    for(j=0;j<a;j++)
			if(s[j+1][ch[h][j]]==0)
			{
			m=1;
			break;
			}
			if(m==0)
		    res+=1;
		   }

		 
		 
		 printf("Case #%ld: %ld\n",cas,res);

		}
	
	
	}

 return 0;
}