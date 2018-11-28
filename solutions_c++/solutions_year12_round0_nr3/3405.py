// p1.cpp : 定义控制台应用程序的入口点。
//
#include "StdAfx.h"
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <string.h>
using namespace std;
char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};


int main() 
{
	char buffer[256];
	fstream out;
	ofstream in;
	in.open("D:\\xx.out",ios::trunc); 
	out.open("D:\\xx.in",ios::in);
	int i,j;
	j=0;
	while(j<31)
	{
			out.getline(buffer,256,'\n');
			for(int i=0;i<sizeof(buffer);i++)
			{
				if (buffer[i]!=' ')
				{
					buffer[i]=a[buffer[i]-97];
				}		
			}
			if (j>0)
			{			
				in<<"Case #"<<j<<": ";
				in<<buffer<<endl;
			}
			j++;
	}
	out.close();
	in.close();
	cin.get();
	return 0;
}