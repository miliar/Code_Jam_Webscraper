#include<iostream>
using namespace std;
int h1[10];
int h2[10];
int a[10];
int b[10];
int c[2];
inline  void chang(int p,int len)
{
	int i=0;
    while(p>0)
	{
		a[len-i]=p%10;
		p/=10;
		i++;
	}
}
int main()
{  
	int i,n,j,k;
    for(i=1023;i<=9876;i++)
	{
		memset(h1,0,sizeof(h1));
		chang(i,4);
		for(j=1;j<=4;j++)
		{
			b[j]=a[j];
		}
		for(j=1;j<=4;j++)
		{
			if(h1[a[j]]==0)
				h1[a[j]]=1;
			else break;
		}
		if(j!=5) continue;
		for(j=100000/i;j<=98;j++)
		{
            chang(j,2);
			for(k=1;k<=2;k++)
			{
				c[k]=a[k];
			}
			memset(h2,0,sizeof(h2));
			for(k=1;k<=2;k++)
			{
                if(h1[a[k]]==0)
				   h2[a[k]]=1;
			    else break;
			}
			if(k!=3) continue;	
			if((i*j-b[4]*c[2])%10!=0) continue;
			chang(i*j,6);
			if(a[6]==c[2]&&a[5]==c[1])
			{
				if(a[3]==a[4]&&h1[a[3]]==0&&h2[a[3]]==0)
				{
                     h2[a[3]]=1;
					 if(h1[a[2]]==0&&h2[a[2]]==0)
					 {
						 h2[a[2]]=1;
						 if(h1[a[1]]==0&&h2[a[1]]==0)
						 {
							 printf("%d*%d=%d\n",i,j,i*j);	 
						 }
					 }
				}
			}
		}
	}
}