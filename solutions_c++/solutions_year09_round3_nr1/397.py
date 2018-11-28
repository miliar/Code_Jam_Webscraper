/*
ID: aditya21
PROG: calfflac
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main() 
{
	ifstream fin ("d:\\io\\A-large.in");
	ofstream fout ("d:\\io\\A-large.out");

	int a, b, c;
	int i, j, k;
	int p, q, r, x, y, z;
	unsigned long long ans;
	
	int cost,max;
	string str1,str2;
	char str[100],ch;
	double d,e,f,g;
	char *pch,ch2;;
	map<char,char> table;
	map<char,char>::iterator iter,iter2;
	int base;

	fin>>a;

	for(i=0;i<a;i++)
	{
		fin>>str1;
		fout<<"Case #"<<i+1<<": ";
		cout<<"Case #"<<i+1<<": ";
		k = str1.size();
		str2 = "";
		table.clear();
		ch2 = '0';
		for(j=0;j<k;j++)
		{
			if(table.find(str1[j]) == table.end())
			{
				table[str1[j]] = ch2;
				if(ch2 == '9')
				{
					ch2 = 'a';
				}
				else
					ch2++;
			}
		}

		base = table.size();
		if(str1.size()>1 )
		{		
			ans = 0;
			if(base == 1)
			{
				base =2;
			}


			for(j=0;j<k;j++)
			{
				if(table[str1[j]] == '0')
				{
					ans = ans*base + 1;
				}
				else if(table[str1[j]] == '1')
				{
					ans = ans*base ;
				}
				else if(table[str1[j]] >= '0' && table[str1[j]] <='9')
				{
					ans = ans*base+ (table[str1[j]]-'0');
				}
				else
				{
					ans = ans*base+ (table[str1[j]]-'a') + 10;
				}
			}
		}
		else
		{
			fout<<'1'<<endl;
			continue;
		}
		fout<<ans<<endl;
	}
	
}

