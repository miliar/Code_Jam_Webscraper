#include<stdio.h>
#include<iostream>
int mod(int a) {if(a<0) return -a; else return a;}
int zero(int a) {if(a<0) return 0; else return a;}
int main()
{
	int c,a,y[100],poso=1,posb=1,p=0,q=0;
	char x[100];
	scanf("%d",&a);
	for(int i=1;i<=a;i++)
	{	scanf("%d",&c);
		for(int j=0;j<c;j++)
		{std::cin>>x[j];
		scanf("%d",&y[j]);}
		poso=1,posb=1,p=0,q=0;
	for(int j=0;j<c;j++)
	{	//printf("%c%d",x[j],y[j]);
		if(x[j]=='O'){
			if(j!=0&&x[j-1]=='O')
			{	p+=((mod(poso-y[j]))+1); q+=(mod(poso-y[j]))+1; poso=y[j];}

			else
			{p+=zero(mod(poso-y[j])-q)+1;q=zero(mod(poso-y[j])-q)+1;poso=y[j];}}
		else if(x[j]=='B'){
			if(j!=0&&x[j-1]=='B')
			{	p+=mod(posb-y[j])+1; q+=mod(posb-y[j])+1; posb=y[j]; }

			else
			{p+=zero(mod(posb-y[j])-q)+1;q=zero(mod(posb-y[j])-q)+1;posb=y[j];}
			}
	}
	printf("Case #%d: %d\n",i,p);
	}	
}
