#include<iostream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<string>
#include<algorithm>
#include<functional>
#include<iomanip>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<cassert>
using namespace std;


#define REP(i,n)		for(int i=0;i<(n);++i)
#define FOR(i,a,b)		for(int i=(a);i<=(b);++i)
#define FOREACH(i,c)	for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define ALL(x)			(x).begin(),(x).end()
//#define S(n)			scanf("%d",&n)
#define SS(a)			scanf("%s",a)

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UINT;

/*======================================IO OPTIMISED FUNCTIONS===================================*/
int sign;
int ch;
inline void S( int &x )
{
			x=0;
			while((ch<'0' || ch>'9') && ch!='-' && ch!=EOF)	ch=getchar_unlocked();
			if (ch=='-')
				sign=-1 , ch=getchar_unlocked();
			else
				sign=1;
			
			do
				x=(x<<3)+(x<<1)+ch-'0';
			while((ch=getchar_unlocked())>='0' && ch<='9');
			x*=sign;
}
/*===============================================================================================*/


string E = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string T = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

map<char,char> M;
bool vis[256];

int main()
{
	for(int i = 0; i<E.size(); i++)
		M[E[i]] = T[i] , vis[T[i]]=1;

	M['q'] = 'z';
	M['e'] = 'o';
	M['y'] = 'a';

	vis['z'] = true;
	
	char key,value;
	for(char ch = 'a'; ch<='z'; ch++)
	{
		if ( ! vis[ch] )		value = ch;
		if (M.find(ch) == M.end())	key = ch;
	}
//	cout<<key<<" "<<value<<endl;
	M[key] = value;
	
	
	int tc;
	cin>>tc;
	getchar();
	for(int i=1; i<=tc; i++)
	{
		string s;	
		getline(cin , s);
		int L = s.size();;
		
		for(int j = 0; j<L; j++)
			s[j] = M[s[j]];
		
		printf("Case #%d: %s\n",i,s.c_str());
	}
	return 0;
}












