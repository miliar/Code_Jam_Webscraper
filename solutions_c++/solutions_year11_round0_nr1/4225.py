#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<cstdlib>
char a[110];
int b[110];
int i,k,conto,contb,kb,ko,n;
int fb()
{
    i=k+1;
	while(a[i]!='B'&&i<=n)
	{
		i++;
	}
    return i;
}
int fo()
{
    i=k+1;
	while(a[i]!='O'&&i<=n)
	{
		i++;
	}
    return i;
}
int sb()
{
	if(abs(b[k]-conto)+1>=abs(contb-b[kb])) return b[kb];
	else 
	{
		if(contb<b[kb]) return contb+abs(b[k]-conto)+1;
		else return contb-abs(b[k]-conto)-1;
	}
}
int so()
{
	if(abs(b[k]-contb)+1>=abs(conto-b[ko])) return b[ko];
	else 
	{
		if(conto<b[ko]) return conto+abs(b[k]-contb)+1;
		else return conto-abs(b[k]-contb)-1;
	}
}
int main()
{
	freopen("g.txt","w",stdout);
	int T,t,tt;
   scanf("%d",&T);
   
	   for(t=1;t<=T;t++)
	   {
       		scanf("%d",&n);getchar();
       		for(i=1;i<=n;i++)  
       			{
       			   a[i]=getchar(); getchar();
       			   scanf("%d",&b[i]); getchar();
       			}
       		conto=1;contb=1; 
			tt=0;
		    
       		for(k=1;k<=n;k++)
       		{
       			if(a[k]=='O')
       			{
       				tt+=abs(b[k]-conto)+1;
					kb=fb();	if(kb!=n+1)contb=sb();
					conto=b[k];
       			}
       			if(a[k]=='B')
       			{
       				tt+=abs(b[k]-contb)+1;
					ko=fo();	if(ko!=n+1)conto=so();
					contb=b[k];
       			}
       		}

			printf("Case #%d: %d\n",t,tt);
	   }
   
   return 0;
}