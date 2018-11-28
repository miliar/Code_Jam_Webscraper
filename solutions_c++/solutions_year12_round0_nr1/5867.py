#include <stdafx.h>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <ctime>
#include <cassert>

using namespace std;

char from[300];
char c;
string s1,s2;

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	while((c=getchar())!=-1)
	{
		s1+=c;
	}
	fclose(stdin);
	freopen("input2.txt","r",stdin);
	while((c=getchar())!=-1)
	{
		s2+=c;
	}
	for (long j=0;j<s1.length();j++)
	{
		from[s1[j]]=s2[j];
		//from[s2[j]]=s1[j];
	}
	if (from['a']==0) from['a']='y';
	if (from['y']==0) from['y']='a';
	if (from['o']==0) from['o']='e';
	if (from['e']==0) from['e']='o';
	if (from['z']==0) from['z']='q';
	if (from['q']==0) from['q']='z';
	fclose(stdin);
	freopen("input3.txt","r",stdin);
	long tt;
	scanf("%ld\n",&tt);
	for (long test=1;test<=tt;test++)
	{
		printf("Case #%ld: ",test);
		while((c=getchar())!='\n')
		{
			//if (from[c]==0)
			//	printf("c=%c\n",c);
			printf("%c",from[c]);
		}
		printf("\n");
	}
}