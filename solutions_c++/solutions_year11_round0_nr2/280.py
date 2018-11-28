#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<climits>
#include<complex>
#define mp make_pair
#define pb push_back
using namespace std;
int n,m;
char s[100000];
char inc[200][200],del[200][200];
string gao(string t)
{
	int l=t.length();
	while (1)
	{
		if (l==1)return t;
		if (inc[t[l-2]][t[l-1]]!=0)
		{
			char ch=inc[t[l-2]][t[l-1]];
			t.erase(l-2);
			t=t+ch;
		}
		else 
		{
			break;
		}
		l=t.length();
	}
	l=t.length();
	int i;
	for (i=0;i<l;i++)
	{
		if (del[t[i]][t[l-1]])
		{
			return "";
		}
	}
	return t;
}
int main()
{
	freopen("C:\\Users\\daizhy\\Downloads\\B-large (3).in","r",stdin);
	freopen("C:\\Users\\daizhy\\Documents\\output.txt","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d",&n);
		memset(inc,0,sizeof(inc));
		memset(del,0,sizeof(del));
		for (i=0;i<n;i++)
		{
			char str[5];
			scanf("%s",str);
			inc[str[0]][str[1]]=str[2];
			inc[str[1]][str[0]]=str[2];
		}
		scanf("%d",&m);
		for (i=0;i<m;i++)
		{
			char str[5];
			scanf("%s",str);
			del[str[0]][str[1]]=1;
			del[str[1]][str[0]]=1;
		}
		int l;
		scanf("%d",&l);
		scanf("%s",s);
		string out="";
		for (i=0;i<l;i++)
		{
			out=out+s[i];
			out=gao(out);
		}
		printf("Case #%d: ",++cc);
		l=out.length();
		if (!l)
		{
			puts("[]");
			continue;
		}
		putchar('[');
		putchar(out[0]);
		for (i=1;i<l;i++)
		{
			printf(", %c",out[i]);
		}
		puts("]");
	}
	return 0;
}
			
