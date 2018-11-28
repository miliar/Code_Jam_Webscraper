// CJ09Welcome.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
using namespace std;

int find(char * str,char * p)
{
	int count=0;
	if(strlen(p)==1){
		for(;*str;++str)
			if(*str==*p)++count;
		return count;
	}
	
	while(*str!=0 && *str!=*p)++str;
	if(*str==0)return count;

	count+=find(str+1,p+1);
	count%=10000;
	count+=find(str+1,p);
	count%=10000;

	return count;
}


int _tmain(int argc, _TCHAR* argv[])
{
	int cases;
	cin>>cases;
	char p[]="welcome to code jam";
	char buf[1024];
	cin.getline(buf,1024);

	for(int c=0;c<cases;c++)
	{
		
		memset(buf,0,1024);
		cin.getline(buf,1024);
		int count=find(buf,p);

		printf("Case #%d: %04d\n",c+1,count);
	}
	return 0;
}

