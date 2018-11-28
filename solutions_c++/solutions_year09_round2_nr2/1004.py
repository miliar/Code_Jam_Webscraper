#include<vector>
#include<map>
#include<set>
#include <iostream>
#include "basetsd.h"
#include <algorithm>
#include "queue"
#include "math.h"
#include<string>
#include "assert.h"

using namespace std;


//To take variable num of things as inp...
void t1()
{
	int nt;
	cin >> nt;
	string temp;
	getline(cin,temp);
	for (int tc=0;tc<nt;++tc)
	{
		string str;
		getline(cin,str);
		char *pch; 
		pch = strtok((char*)str.c_str()," ");
		while (pch != NULL)
		{
			int i = atoi(pch);
			pch = strtok(NULL," ");
			cout << i << "\n";
		}
		
	}
}

void Two()
{
	int nt;
	cin >> nt;
	string temp;
	getline(cin,temp);
	for (int tc=0;tc<nt;++tc)
	{
		string str;
		getline(cin,str);
		int i;
		for (i=str.size()-1;i>0;--i)
		{
			if (str[i]-'0' > str[i-1]-'0')
			{
				int mn = str[i-1]-'0';
				int ind = i;
				for (int tmp=i;tmp<str.size();++tmp)
				{
					if (str[tmp]-'0' < str[ind]-'0' && str[tmp]-'0' > mn)
					{
						ind = tmp;
					}
				}
				if (str[ind]-'0' > str[i-1]-'0')
				{
					char t;
					t = str[ind];
					str[ind] = str[i-1];
					str[i-1]= t;
				}
				break;
			}
		}
		if (i != 0)
		{
				//string num;
				//for (int z1=i;z1<str.size();++z1)
				//{
				//	num.push_back(str[z1]);
				//}
			for (int z1=i;z1<str.size();++z1)
			{
				for (int z2=z1+1;z2<str.size();++z2)
				{
					if (str[z1]-'0' > str[z2]-'0')
					{
						char t;
					t = str[z1];
					str[z1] = str[z2];
					str[z2] = t;
					}
				}
			}
			cout << "Case #"<<tc+1<<": "<<str.c_str()<<"\n";
		}
		else
		{
			string num;
			for (int z1=0;z1<str.size();++z1)
			{
				for (int z2=z1+1;z2<str.size();++z2)
				{
					if (str[z1]-'0' > str[z2]-'0')
					{
						char t;
						t = str[z1];
						str[z1] = str[z2];
						str[z2] = t;
					}
				}
			}
			int z1;
			
			for (z1=0;z1<str.size();++z1)
			{
				if (str[z1]!='0' )
				{
					break;
				}
			}
			num.push_back(str[z1]);
			for (int z2=0;z2<=z1;++z2)
			{
				num.push_back('0');
			}
			for (int z2=z1+1;z2<str.size();++z2)
			{
				num.push_back(str[z2]);
			}

			cout << "Case #"<<tc+1<<": "<<num.c_str()<<"\n";
		}
	}
}

int main()
{

	Two();
	return 0;
}