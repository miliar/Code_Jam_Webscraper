// CJ_R1B_B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <stdio.h>

void nextnum(char* num,int l)
{
	bool ok=false;
	int pos = 0;
	for (int j=l-2; j>=0; j--)
	{
		for (int i=l-1; i>j; i--)
		{
			if (num[i]>num[j])
			{
				//change
				char tmp = num[i];
				num[i] = num[j];
				num[j] = tmp;
				ok = true;
				pos = j;
				break;
			}
		}
		if (ok) break;
	}
	if (ok==false)
	{
		char min=num[0];
		for(int j=1; j<l; j++)
		{
			if (num[j]!='0' && num[j] < min)
			{
				min = num[j];
				pos = j;
			}
		}
		char tmp = num[0];
		num[0] = num[pos];
		num[pos] = tmp;

		num[l]='0';
		num[l+1]=0;

		l++;
		pos=0;
	}

	for (int j=pos+1; j<l-1; j++)
	{
		for (int i=j+1; i<l; i++)
		{
			if (num[i]<num[j])
			{
				char tmp = num[i];
				num[i] = num[j];
				num[j] = tmp;
			}
		}
	}


}



int _tmain(int argc, _TCHAR* argv[])
{
	FILE * fout;
	fout = fopen("d:\\cj\\Bl.out","w+b");
	std::string str_in = "d:\\cj\\B-large.in";
	std::ifstream is(str_in.c_str());
	std::string line;
	
	int T;
	is >> T;
	
	char num[23];
	char next[23];
	memset(num,0,21);
	memset(next,0,21);

	for (int i=0; i<T; i++)
	{
		is >> num;
		
		nextnum(num,strlen(num));
		
		char out[1000];
		sprintf(out,"Case #%d: %s\n",i+1,num);
        fwrite(out,strlen(out),1,fout);

	}
	
	

	fclose(fout); 
	return 0;
}