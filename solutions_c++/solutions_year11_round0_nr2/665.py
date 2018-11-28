#include <string.h>
#include <sstream>
#include <string>
#include <map>
#include <queue>
#include <vector>
#include <set>
#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
#define ll long long
map< pair<char,char>,int > com;
map< pair<char,char>,int > clr;
map< pair<char,char>,int > :: iterator it;

vector<char>ans;

char ft[8]={'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
int find( char c )
{
	for(int i=0;i<8;++i)
		if( c == ft[i] )return 1;
	return 0;
}
char compose(char ch)
{
	while(1)
	{
		if( ans.size() == 0 )
			break;
		char tmp = ans[ans.size()-1];
		it = com.find( make_pair( ch, tmp ) );
		if( it != com.end() )
		{
			ans.pop_back();
			ch = it->second;
		}
		else
			break;
	}
	return ch;
}
void clrch( char ch )
{
	for(int i=ans.size()-1;i>=0;--i)
	{
		char tmp = ans[i];
		it = clr.find( make_pair( tmp, ch ) );
		if( it != clr.end() )
		{
			ans.clear();
			return ;
		}	
	}
	ans.push_back(ch);
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int c =0;c<T;)
	{
		com.clear();
		clr.clear();
		ans.clear();

		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i)
		{
			string str;
			cin>>str;
			com[ make_pair( str[0], str[1] ) ] = str[2];
			com[ make_pair( str[1], str[0] ) ] = str[2];
		}
		int m;
		scanf("%d",&m);
		for(int i=0;i<m;++i)
		{
			string str;
			cin>>str;
			clr[ make_pair( str[0], str[1] ) ] = 1;
			clr[ make_pair( str[1], str[0] ) ] = 1;
		}
		int k;
		scanf("%d",&k);
		string solstr;
		cin>>solstr;
		for(int i=0;i<k;++i)
		{
			//printf("str(%c)\n",solstr[i]);
			char tmp = compose( solstr[i] );
			clrch( tmp );
			/*
			for(int j=0;j<ans.size();++j)
				printf("%c ",ans[j]);
			printf("\n");
			*/
		}

		printf("Case #%d: [",++c);
		for(int i=0;i<ans.size();++i)
		{
			if( i ) printf(", ");
			printf("%c",ans[i]);
		}
		printf("]\n");
	}
}

