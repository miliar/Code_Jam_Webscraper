#pragma warning(disable: 4786)
#include<stdio.h>
#include<string>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<map>
#include<iostream>
#include<set>
#include<math.h>
#include<queue>
#include<queue>
using namespace std;
		


int tp[40];
int ntp[40];

int main()	
{			
	int  T,cs,n,k;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	//freopen("out.txt","w",stdout);
	
	//freopen("in.txt","r",stdin);
	

	scanf("%d",&T);
	
	for(cs=0;cs<=30;cs++)
	{
		tp[cs]= (1<<cs);
		ntp[cs]=tp[cs]-1;
	}
		
	for(cs=1;cs<=T;cs++)
	{
	
		printf("Case #%d: ",cs);
		scanf("%d %d",&n,&k);
		
		if((k%tp[n])==(ntp[n]))
			printf("ON\n");
		else
			printf("OFF\n");

	}
	
  	return 0;
}			