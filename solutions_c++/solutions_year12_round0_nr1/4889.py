#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<sstream>
#include<iostream>
#include<stack>
#include<list>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)

//char arr[5][105],arr2[5][105];
char to[]="yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	
	/*for(int i=0;i<26;i++)to[i]='#';
	
	for(int j=0;j<3;j++)
	{
		for(int i=0;;i++)
		{
			scanf("%c",&arr[j][i]);
			if(arr[j][i]=='\n')break;
		}
	}
	for(int i=0;i<3;i++)
	{
		for(int j=0;;j++)
		{
			scanf("%c",&arr2[i][j]);
			if(arr2[i][j]=='\n')break;
			
			to[arr[i][j]-'a']=arr2[i][j];
		}
	}
	
	for(int i=0;i<26;i++)printf("%c",to[i]);*/
	
	int T,k=0;
	
	scanf("%d%*c",&T);
	
	while(T--)
	{
		k++;
		printf("Case #%d: ",k);
		for(int i=0;;i++)
		{
			char c;
			scanf("%c",&c);
			if(c=='\n')break;
			
			if(isalpha(c))printf("%c",to[c-'a']);
			else if(c==' ')printf(" ");
		}
		printf("\n");
	}
}


/*
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
*/
































