#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>

#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<list>
#include<set>
#include <algorithm>
using namespace std;

#define FOR(i,m,n) for(int i=m;i<n;i++)
#define FORE(i,m,n) for(int i=m;i<=n;i++)

typedef long long int int64;

int main()
{	char str[][100]={"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv","our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"};
	char arr[100]={0};
	for(int i=0;i<3;i++)
	{
		FOR(j,0,strlen(str[i]))
		{
			arr[str[i][j]-'a']=str[i+3][j];
		}
	}
	arr['q'-'a']='z';
	arr['z'-'a']='q';
	//FOR(i,0,26)
	//	cout<< (char)(i+'a')<<" "<<arr[i]<<endl;
	int ch;
	cin>>ch;getchar();
	FORE(i,1,ch)
	{
		string st;
		getline(cin,st);
		cout<<"Case #"<<i<<": ";
		FOR(j,0,st.length())
		{
			if(st[j]!=' ')
				cout<<arr[st[j]-'a'];
			else
				cout<<" ";
		}
		cout<<endl;
	}

	return 0;
}
