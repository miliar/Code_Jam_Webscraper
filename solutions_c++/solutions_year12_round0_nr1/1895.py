/*
  Problem No : 
  Author     : Debashis Maitra
  Complexity :
  Date       :
*/

#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <ctype.h>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <sstream>

using namespace std;

#define CLR(x) memset((x),0,sizeof(x))
#define pb push_back
#define sz size()
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORALL(i,x) for(int i=0;i<x.size();i++)
#define FORALLR(i,x) for(int i=x.size()-1;i>=0;i--)
#define SWAP(x,y) (x)+=(y);y=(x)-(y);x=(x)-(y);
#define lint long long
#define MAX 1000
#define INF 1<<30

typedef vector<int> vi;
typedef vector<string> vs;

int cases,caseno;
char strIn[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"};
char strOut[] ={"our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"};
char maps[255];
//char mapped[255];
bool input()
{
	return false;
}
void detectMapping()
{
	for(int i = 0; i < strlen(strIn); i++ )
	{
		maps[ strIn[i] ] = strOut[ i ];
		//mapped[ strOut[i]] = 1;
	}
	maps['z'] = 'q';
	maps['q'] = 'z';
	maps[' '] = ' ';
	//mapped['q'] = 1;
	/*for( int i = 'a';  i <= 'z'; i++ )
	{
		if( !mapped[i])printf("%c.....",(char)i);
		if(maps[i])printf("%d %d %d\n",(char)i-'a', maps[i] - 'a',(i+maps[i])%26 );
		else printf("missing %c\n", (char)i);
	}*/

}
void process()
{
	string str;
	getline(cin,  str );
	if(str.length() == 0) getline(cin,  str ); 
	for( int i = 0; i < str.length();i++ )
	{
		//printf("%c");
		str[i] = maps[ str[i]];
	}
	cout << "Case #"<< (++caseno)<<": " << str << endl;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("outputA.txt","w",stdout);
	detectMapping();
	cin >> cases;

	while(cases-- )
	{
		process();
	}
}