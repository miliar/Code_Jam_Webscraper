#include<iostream>

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>



using namespace std;

class sit
{
public:
	char m[26];
	char search(char a)
	{
		for(int i=0;i<=25;i++)
		{
			if(m[i]==a)
				return i+97;
		}
	}
	void getstring()
	{
		int casenum;
		cin>>casenum;
		
		m[0]='y';
		m[1]='n';
		m[2]='f';
		m[3]='i';
		m[4]='c';
		m[5]='w';
		m[6]='l';
		m[7]='b';
		m[8]='k';
		m[9]='u';
		m[10]='o';
		m[11]='m';
		m[12]='x';
		m[13]='s';
		m[14]='e';
		m[15]='v';
		m[16]='z';
		m[17]='p';
		m[18]='d';
		m[19]='r';
		m[20]='j';
		m[21]='g';
		m[22]='t';
		m[23]='h';
		m[24]='a';
		m[25]='q';
		for(int i=1;i<=casenum;i++)
		{
		string str;
	    getline(cin,str);
		int len=str.length();
		if(len==0)
		{
			i--;
			continue;
		}
		for(int j=0;j<=len-1;j++)
		{
			if(str[j]!=' ')
			{
			int k=str[j];
			char c=search(k);
		
			str[j]=c;
			}
		}
		cout<<"Case #"<<i<<": "<<str<<endl;
		}
		
	}
};



int main()
{
		freopen("E:/in.in","rt",stdin);
		freopen("E:/out.out","wt",stdout);
	sit *s=new sit();
	s->getstring();
}