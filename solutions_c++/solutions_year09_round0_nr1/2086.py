#include <iostream>
#include <vector>
#include <queue>
#include <list>
#include <string>
#include <vector>
#include <map>
#include <fstream>
using namespace std;

bool findifstr(string a,char b)
{
	for (int i=0;i!=a.size();i++)
	{
		if (a[i]==b)
		{
			return true;
		}
	}
	return false;
}


int main()
{
	fstream f2("A-large.in");
	int L,D,N;
	f2>>L>>D>>N;

	vector<string> dictionary;
	vector<string> word;
	vector<string>check;
	vector<int>result;

	string teststring;
	string inputstr;
	string changeap;
	string copystring;
	bool isstring = true;
	int num;
	int strnum=0;

	for (int i =0;i!=L;i++)
	{
		check.push_back("0");
		teststring.push_back('0');
	}

	for (int i=0;i!=D;i++)
	{
		f2>>inputstr;
		dictionary.push_back(inputstr);
	}
	for (int m=0;m!=N;m++)
	{
		f2>>inputstr;
		strnum = 0;
		for (int i=0;i!=inputstr.length();i++)
		{
			if (inputstr[i]!='(')
			{
				teststring[strnum] = inputstr[i];
			}
			else
			{
				num = strnum;
				while (1)
				{
					i++;
					if (inputstr[i]==')')
					{
						break;
					}
					changeap.push_back(inputstr[i]);

				}
				check[num] = changeap;
				changeap.clear();
			}
			strnum++;
		}
		for(int i=0;i!=dictionary.size();i++)
		{
			copystring = dictionary[i];
			for (int j=0;j!=copystring.size();j++)
			{
				if (teststring[j]!='0')
				{
					if (copystring[j]!=teststring[j])
					{
						isstring = false;
						break;
					}
				}
				else
				{
					changeap = check[j];
					if(!findifstr(changeap,copystring[j]))
					{
						isstring = false;
						break;
					}
				}
			}
			if (isstring == false)
			{
				isstring = true;
			}
			else
			{
				word.push_back(copystring);
			}
		}
		result.push_back(word.size());
		check.clear();
		teststring.clear();
		for (int i =0;i!=N;i++)
		{
			check.push_back("0");
			teststring.push_back('0');
		}
		changeap.clear();
		copystring.clear();
		word.clear();
	}
	f2.close();
	ofstream f1("a.txt");
	for (int i=0;i!=result.size();i++)
	{
		
		f1<<"Case #"<<i+1<<":"<<" "<<result[i]<<endl;
		
	}
	f1.close();
	return 0;
}