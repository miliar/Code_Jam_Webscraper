#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<sstream>
#include<map>
#include<string>
#include<algorithm>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<cmath>

using namespace std;

map<char, char> trans;

void print_result(int i, string list)
{
	if (i != 1)
		cout << endl;
	cout<<"Case #"<< i<< ": ";
	for (int j = 0; j < list.size(); j++)
	{
       cout << trans[list[j]];
	}
}

void populate_trans(char real, char fake)
{
	if (trans[fake] != NULL)  {
		return;
	}
		trans[fake] = real;
}

void main()
{
    string fake_string = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvqz";
	string real_string = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upzq";
	for (int i = 0; i < fake_string.size(); i ++)
	{
		populate_trans(real_string[i], fake_string[i]);
	}
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int num_case;
	string newLine;
	string list;
    cin>>num_case;
	getline(cin,newLine);
		for(int i=1; i <= num_case; i++)
		{
			getline(cin,list);
            print_result(i, list);
		}
	}



