// a.cpp : 定义控制台应用程序的入口点。
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
#define NULL 0





int main()
{
	fstream in("A-large.in",ios::in),out("A-large.out",ios::out);
	int T;
	int i,j,k,m,n;
	char ch;
	string str,tstr,bstr;
	int base;
	long long result;
	in>>T;
	for(i=0;i<T;i++)
	{
		in>>str;
		base=1;
		bstr="";
		bstr+=str[0];
		for(j=1;j<str.size();j++)
		{
			for(k=0;k<bstr.size();k++)
			{
				if(str[j]==bstr[k])
					break;
			}
			if(k==bstr.size())
			{
				bstr+=str[j];
				base++;
			}
		}
		result=1;
		if(bstr.size()>1)
		{
			ch=bstr[0];
			bstr[0]=bstr[1];
			bstr[1]=ch;
		
//			cout<<base<<" "<<bstr<<endl;
			for(j=1;j<str.size();j++)
			{
				for(k=0;k<bstr.size();k++)
					if(bstr[k]==str[j])
					{
						result*=base;
						result+=k;
						break;
					}
			}
		}
		else
		{
			for(j=1;j<str.size();j++)
			{
				result*=2;
				result+=1;
			}
		}
		out<<"Case #"<<i+1<<": "<<result<<endl;
	}

	in.close();
	out.close();
	return 0;
}

