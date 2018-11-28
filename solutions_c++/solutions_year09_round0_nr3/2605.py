
#include<iostream>
#include<stdio.h>
#include<string.h>
#include<map>
#include<queue>
#include<algorithm>
using namespace std;
char text[]="welcome to code jam";

int main()
{   
	freopen("C-large.in","r",stdin);
    freopen("1.out","w",stdout);
	 int tt;
	 char str[520];
	 int tlen=strlen(text);
	 scanf("%d",&tt);
     
	 getchar();
	 int cas=1;
	 
	 while(tt--)
	 {
		 gets(str);
		 printf("Case #%d: ",cas++);
		 int slen=strlen(str);
		 if(slen<tlen)
		 {
			 printf("0000\n");
			 continue;
		 }
		 int i;
	     int  a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19;
		 a1=a2=a3=a4=a5=a6=a7=a8=a9=a10=a11=a12=a13=a14=a15=a16=a17=a18=a19=0;
		 for(i=slen-1;i>=0;i--)
		 {
            if(str[i]=='w')
			{
				a1+=a2;
				if(a1>=10000)
					a1%=10000;
			}
			else if(str[i]=='e')
			{
				a2+=a3;
			    if(a2>=10000)
					a2%=10000;
				a7+=a8;
				if(a7>=10000)
				    a7%=10000;
				a15+=a16;
				  	if(a15>=10000)
				    	a15%=10000;
				
			}
			else if(str[i]=='l')
			{
				a3+=a4;
				if(a3>=10000)
					a3%=10000;
			}
			else if(str[i]=='c')
            {
				a4+=a5;
				if(a4>=10000)
					a4%=10000;
                a12+=a13;
				if(a12>=10000)
					a12%=10000;
			}
			else if(str[i]=='o')
			{
				a5+=a6;
					if(a5>=10000)
				    	a5%=10000;
				a10+=a11;
					if(a10>=10000)
				    	a10%=10000;
				a13+=a14;
					if(a13>=10000)
				    	a13%=10000;
			}
			else if(str[i]=='m')
			{
				a6+=a7;
					if(a6>=10000)
				    	a6%=10000;
				a19++;
					if(a19>=10000)
				    	a19%=10000;
			}
			else if(str[i]==' ')
			{
				a8+=a9;
					if(a8>=10000)
				    	a8%=10000;
				a11+=a12;
					if(a11>=10000)
				    	a11%=10000;
				a16+=a17;
					if(a16>=10000)
				    	a16%=10000;
			}
			else if(str[i]=='t')
			{
				a9+=a10;
					if(a9>=10000)
				    	a9%=10000;
			}
			else if(str[i]=='d')
			{
				a14+=a15;
					if(a14>=10000)
				    	a14%=10000;
			}
			else if(str[i]=='j')
			{
				a17+=a18;
					if(a17>=10000)
				    	a17%=10000;
			}
			else if(str[i]=='a')
			{
				a18+=a19;
					if(a18>=10000)
				    	a18%=10000;
			}
		 }
	     if(a1>=10000)
             a1%=10000;
		 printf("%04d\n",a1);
	 }
	 return 0;
}

/*
3
elcomew elcome to code jam
wweellccoommee to code qps jam
welcome to code jam
*/
