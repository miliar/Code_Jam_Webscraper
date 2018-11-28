#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("s.txt","w",stdout);
	char str[100+10];
	char buf[100+10];
	int t,k=0,c,d,n,i,j,l,i2,i3;
	char c1[40],c2[40],c3[40],d1[40],d2[40];
	cin>>t;
	while(t--)
	{
	   k++;
       scanf("%d ",&c);
       if(c>0)
	   {
		   for(i=0;i<c;i++)
		   {scanf("%c%c%c ",&c1[i],&c2[i],&c3[i]);
		  // cout<<c1[i]<<c2[i]<<c3[i]<<endl;
		   }
	   }
	   else
	   {
		   c1[0]=0,c2[0]=0;
	   }
	   scanf("%d ",&d);
	   if(d>0)
	   {
		   for(i=0;i<d;i++)
		     scanf("%c%c ",&d1[i],&d2[i]);
		   //cout<<d1<<d2<<endl;
	   }
	   else
	   {
		   d1[0]=0,d2[0]=0;
	   }
	   scanf("%d",&n);//cout<<n<<endl;
       scanf("%s",buf);
	   //cout<<n<<endl;
	   str[0]=buf[0];
	   j=0;
	   for(i=1;i<n;i++)
	   {
		   int flag=0;
		   for(i2=0;i2<c;i2++)
		      if((buf[i]==c1[i2]&&str[j]==c2[i2])||(buf[i]==c2[i2]&&str[j]==c1[i2]))
			  {
			   str[j]=c3[i2];
			   flag=1;break;
			  }
		   if(flag!=1)
		   {
			   l=j;
			   while(l>=0)
			   {
				  for(i2=0;i2<d;i2++)
				     if((str[l]==d1[i2]&&buf[i]==d2[i2])||(str[l]==d2[i2]&&buf[i]==d1[i2]))
					 {
					   j=-1;flag=2;
					   break;
					 }
				  if(flag==2)
					  break;
				     l--;
			   }
			   if(flag==0)
			   {
				   j++;
				   str[j]=buf[i];//cout<<"---"<<str[j]<<endl;
			   }
		   }
	   }
	   int len=j+1;
	   //cout<<11<<endl;
	   printf("Case #%d: [",k);
	   for(i=0;i<len;i++)
	   {
		   //cout<<i<<endl;
		  if(i!=len-1)
           printf("%c, ",str[i]);
		  else
		   printf("%c",str[i]);
	   } 
	   printf("]\n");
	}
	return 0;
}


