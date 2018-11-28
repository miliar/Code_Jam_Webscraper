// CJ_R1C_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <stdio.h>

int countdif(char * msg)
{
	int count=0;
	char dif[255];
	memset(dif,0,255);
	for (int i=0; i<strlen(msg); i++)
	{
		dif[msg[i]]=1;
	}

	for (int i=0; i<255; i++)
	{
		count += dif[i];
	}
	return count;
}

void createnum(char *msg,__int64* num,int base)
{
	int v=0;
	int next=0;
	for (int i=0; i<strlen(msg); i++)
	{
		if (msg[i]!='*')
		{
			if (i==0) v=1;
			else
			{
				v=next;
				if (next==0) next++;
				next++;
			}
			char tmp = msg[i];
			msg[i]='*';
			num[i]=v;
			for (int j=i+1; j<strlen(msg); j++)
			{
				if (msg[j]==tmp) 
				{
					msg[j]='*';
					num[j]=v;
				}
			}
		}
	}
}

__int64 getnum(__int64* num,int base,int len)
{
	__int64 value=0;
	__int64 p=1;
	for (int i=len-1; i>=0;  i--)
	{
		value+=num[i]*p;
		p*=base;
	}
	return value;
}
int _tmain(int argc, _TCHAR* argv[])
{
	FILE * fout;
	fout = fopen("d:\\cj\\Al.out","w+b");
	std::string str_in = "d:\\cj\\A-large.in";
	std::ifstream is(str_in.c_str());
	std::string line;
	int T;
	is >> T;
	char msg[62];
	__int64 num[62];
	char result[20];
	memset(msg,0,62);

	for (int i=0; i<T; i++)
	{
		is >> msg;
		int base = countdif(msg);
		if (base<2) base=2;
		createnum(msg,num,base);
		__int64 result = getnum(num,base,strlen(msg));
		char out[1000];
		
		sprintf(out,"Case #%d: %I64d\n",i+1,result);
        fwrite(out,strlen(out),1,fout);

	}
	
	

	fclose(fout); 
	return 0;
}