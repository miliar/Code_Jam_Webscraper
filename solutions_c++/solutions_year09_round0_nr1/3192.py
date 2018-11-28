// PTest.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include "string.h"
#include "pcre.h"

int len,nw,nt;
const char *error;
int erroffset;

std::ifstream fi("a.i");
std::ofstream fo("aLL.o");

std::vector<std::string> vp;
std::vector<pcre *> re;

void fillW()
{
	std::string w;
	for(int i=0;i<nw;i++)
	{
		fi>>w;
		vp.push_back(w);
	}
}

void fillR()
{
	std::string w;
	for(int j=1;j<=nt;j++)
	{
		fi>>w;
		for ( int i = 0; i < w.length(); i++)
		{
			if (w[i] =='(')
				w.replace(i,1,"[");
			else if(w[i]==')')
				w.replace(i,1,"]");
		}
		pcre *regexp =(pcre_compile(w.c_str(),0,&error,&erroffset,NULL));
		int num=0;
		for(int i=0;i<vp.size();i++)
		{
			if(pcre_exec(regexp,NULL,vp[i].c_str(),vp[i].length(),0,0,NULL,0)==0)
				num++;
		}
		fo<<"Case #"<<j<<": "<<num<<std::endl;
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	fi>>len>>nw>>nt;
	fillW();
	fillR();
	return 0;
}