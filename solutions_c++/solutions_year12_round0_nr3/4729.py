#include<iostream>
#include<stdio.h>
using namespace std;
int dig;
int func2(int a,int b)
{
	return (((a%10)*10+(a/10))==b);
}
int func3(int a,int b)
{
	if(a==b) return 1;
	int n1,n2,n3;
	n3=a%10;
	a=a/10;
	n2=a%10;
	n1=a/10;
	a=n3*100+n1*10+n2;
	dig--;
	if(dig==0) return 0;
	else
	return func3(a,b);
}
int main()
{
int i,j,a,b,cnt=0,t,case1=0;
scanf("%d",&t);
while(t--)
{
case1++;
cnt=0;
scanf("%d%d",&a,&b);
for( i=a;i<=b-1;i++)
{

	for( j=i+1;j<=b;j++)
	{
		if(i<10&&j<10) { if(i==j) cnt++;/*,printf("yes\n"); else printf("no\n");*/	}
		else if(i>=10&&j>=10&&i<100&&j<100)
		{
			if(func2(i,j)) cnt++;
		}
		else if(i>99&&i<1000&&j>99&&j<1000)
		 {
		dig=3;
		if(func3(i,j)) cnt++;/*,printf("yes"); else printf("NO");*/
		}
		else if(i==1000&&j==1000) cnt++;
	}
}
printf("Case #%d: %d\n",case1,cnt);
}
}
