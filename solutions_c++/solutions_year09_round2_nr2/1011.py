// b.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

int p[3];
int main()
{
	fstream in("B-large.in",ios::in),out("B-large.out",ios::out);
	vector<int> ivec;
	vector<int>::iterator iter;
	int T;
	int i,j,k,m,n;
	char ch;
	string str,tstr;
	in>>T;
	for(i=0;i<T;i++)
	{
		in>>str;
		for(j=str.size()-1;j>0;j--)
		{
			if(str[j]<=str[j-1])
				tstr+=str[j];
			else
			{
				tstr+=str[j];


		//		else
				{
					sort(tstr.begin(),tstr.end());
					for(m=0;m<tstr.size();m++)
						if(tstr[m]>str[j-1])
						{
							ch=tstr[m];
							tstr[m]=str[j-1];
							str[j-1]=ch;
							break;
						}
						for(n=j,m=0;n<str.size();n++)
						{
							str[n]=tstr[m++];
						}
						out<<"Case #"<<i+1<<": "<<str<<endl;
						tstr="";
						break;
				}
			}
		}
				if(j==0)
				{
					tstr+=str[0];
					sort(tstr.begin(),tstr.end());
					if(tstr[0]!='0')
					{
						str=tstr.substr(1,tstr.size()-1);
						tstr=tstr.substr(0,1);
						tstr=tstr+"0"+str;
						out<<"Case #"<<i+1<<": "<<tstr<<endl;
						
					}
					else
					{
						for(k=0;k<tstr.size();k++)
							if(tstr[k]>'0')
							{
								str=tstr[k];
								tstr[k]='0';
								break;
							}
							str+=tstr;
						//	cout<<str<<endl;
							out<<"Case #"<<i+1<<": "<<str<<endl;
					}
					tstr="";
				}

	}


	in.close();
	out.close();
	return 0;
}


