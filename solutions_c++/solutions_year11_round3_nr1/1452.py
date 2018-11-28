// roundc.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
using namespace std;
int main()
{   ifstream acin("2.in",ios::in);
    ofstream acout("2.out",ios::out);
	char ch[60][60];
	int row,col;
	int casenum=1;
	int ng;
	int i,j,k;
	bool result=true;
	acin>>ng;
	while(ng)
	{     result=true;
		acin>>row>>col;

		for(i=0;i<row;i++)
			for(j=0;j<col;j++)
			{
				acin>>ch[i][j];
			}
			for(i=0;i<row;i++)
				for(j=0;j<col;j++)
				{
					if(ch[i][j]=='#')
					{
						if(j==col-1||i==row-1) {result=false;goto end;}
						if(ch[i][j+1]!='#'||ch[i+1][j]!='#'||ch[i+1][j+1]!='#'){result=false;goto end;}
						else 
						 
						{
							ch[i][j]='/';
							ch[i][j+1]='\\';
								ch[i+1][j]='\\';
							ch[i+1][j+1]='/';
						}
					}
				}
end:           acout<<"Case #"<<casenum<<":"<<endl;
				if(result)
				   for(i=0;i<row;i++)
					   {
						   for(j=0;j<col;j++)
					   acout<<ch[i][j];
				     acout<<endl;    
				   }
			   else acout<<"Impossible"<<endl;
				   ng--;
				   casenum++;
	}
	return 0;
}

