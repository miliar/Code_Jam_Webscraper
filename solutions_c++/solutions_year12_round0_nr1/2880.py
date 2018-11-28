#include <iostream>
#include <stdlib.h>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
int main()
{
	freopen("G://GCJ/A-small.in","r",stdin);
	freopen("G://GCJ/1.out","w",stdout);
	string one="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qz";
	string two="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zq";
	int size=one.size();
	int T;
	scanf("%d",&T);
	getchar();
	for (int i=0;i<T;i++)
	{
		string come;
		string res;
		getline(cin,come);
		int size1=come.size();
		for (int j=0;j<size1;j++)
		{
			for(int k=0;k<size;k++)
			{
				if (come[j] == one[k])
				{
					res+=two[k];
					break;
				}
			}
		}
		printf("Case #%d: ",i+1);
		cout<<res<<endl;
	}
	return 0;
}