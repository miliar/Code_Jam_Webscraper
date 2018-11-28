#include<stdio.h>
#include<vector>
#include<iostream>
#include<math.h>
#include<algorithm>
#include<string>
using namespace std;
char read[1000];
char Mass[30] = "welcome to code jam";
int func(int index,int num)
{
	int result = 0,i;
	if( Mass[num]=='m' && num>10 )
	{
		for(i=index;read[i]!='\0';++i)
		{
			result%=10000;
			if( read[i]=='m' ) result++;
		}
		return result%10000;
	}
	for(i=index;read[i]!='\0';++i)
		if( read[i]==Mass[num] )
			result+=func(i,num+1)%10000;
	return result%10000;
}
int main()
{
	int i,j,k,n,m,t,l;
	double a,b;
	fgets(read,1023,stdin);
	sscanf(read,"%d",&n);
	int result = 0;
	for(i=0;i<n;++i)
	{
		result = 0;
		fgets(read,1023,stdin);
		for(j=0;read[j]!='\0';++j)
			if( read[j]=='w' )
				result+=func(j+1,1)%10000;
		printf("Case #%d: ",i+1);
		result%=10000;
		if( result<1000 ) printf("0");
		if( result<100 ) printf("0");
		if( result<10 ) printf("0");
		printf("%d\n",result);
	}
	return 0;
}