// CJ_Q_C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <stdio.h>


int search(char* welcome,char* text,int i)
{
	int sum=0;
	if (welcome[i]==0) return 1;
	for (int j=0; j<strlen(text); j++)
	{
		if (text[j]==welcome[i])
		{
			if (i==0) printf("%d\n",j);
			sum += search(welcome,&text[j],i+1);	
			sum = sum % 1000;
		}
	}

	return sum;
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE * fout;
    fout = fopen("F:\\CodeJam\\\Cs.out","w+b");
    std::string str_in = "F:\\CodeJam\\\C-small-attempt0.in";
    std::ifstream is(str_in.c_str());
    std::string line;

    int N;
    is >> N;//number of cases
	char * text = new char[500];
	char welcome[30];
	sprintf(welcome,"welcome to code jam");
	memset(text,0,500);
	is.getline(text,500);
	for (int i=0; i<N; i++)
    {   
		is.getline(text,500);
		printf("%d\n",i);
		int sum = search(welcome,text,0);
		char out[1000];
		sprintf(out,"Case #%d: %04d\n",i+1,sum);
		fwrite(out,strlen(out),1,fout);

    }
   

    fclose(fout); 
	return 0;
}

