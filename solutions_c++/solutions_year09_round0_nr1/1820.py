#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <set>

using namespace std;

set <string> dictionary[30];
int L,D,N;
char word[100];
char buf[1000];
vector <string> tokens;
int count;

void solve(int k)
{
	int i;

	if( k >= L ) 
	{
		count++;
		return;
	}

	for( i = 0; i < tokens[k].size(); i++ )
	{
		word[k] = tokens[k][i];
		word[k + 1] = '\0';
		string s = word;
		if( dictionary[k + 1].find(s) != dictionary[k + 1].end() )
			solve(k + 1);
	}
}

int main()
{
	int i,j;

	int kase;

	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small.out","w",stdout);

	scanf("%d %d %d",&L,&D,&N);

	for( i = 0; i < 30; i++ ) dictionary[i].clear();
		
	gets(buf);

	for( i = 0; i < D; i++ ) 
	{
		gets(buf);
		string s = buf;
		for( j = 1; j <= strlen(buf); j++ )
		{
			dictionary[j].insert(s.substr(0,j));
		}
	}

	for( kase = 1; kase <= N; kase++ )
	{
		gets(buf);
		tokens.clear();

		//tokens.resize(N * 2);
		bool group = false;
		int k = 0;	
		string ss;

		for( i = 0; i < strlen(buf); i++ )
		{
			if( buf[i] == '(' ) group = true;
			else if( buf[i] == ')' ) 
			{
				group = false;
				tokens.push_back(ss);
				ss = "";
			}

			else if( !group )
			{
				ss += buf[i];
				tokens.push_back(ss);
				ss = "";
			}
			else ss += buf[i];
		}
		count = 0;
		solve(0);

		printf("Case #%d: %d\n",kase,count);
	}

	return 0;
}