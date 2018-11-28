#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <algorithm>
#include <utility>
#include <string>
#include <functional>
#include <sstream>
#include <fstream>
using namespace std;
#define FOR(i,a,b) for (i=(a);i<=(b);i++)
#define fori(it,v) for (it=(v).begin();it!=(v).end();it++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(c) c.begin(),c.end()
#define pf push_front
#define popb pop_back
#define popf pop_front
typedef pair<int,int> ii;
FILE *in,*out;
bool lit[30][300];
char dic[50010][31],s[1005];

int main()
{
	int t,T,L,d,n,poz,nr,i,j,good;
	in=fopen("test.in","r");
	out=fopen("test.out","w");
	fscanf(in,"%d%d%d\n",&L,&d,&t);
	FOR(i,1,d)
		fgets(dic[i]+1,30,in);
	FOR(T,1,t)
	{
		poz=nr=0;
		memset(s,0,sizeof(s));
		memset(lit,0,sizeof(lit));
		fgets(s+1,1000,in);
		n=strlen(s+1);
		if (s[n]=='\n')
		{
			s[n]=0;
			n--;
		}
		FOR(i,1,n)
		{
			poz++;
			if (s[i]=='(')
			{
				while (s[i+1]>='a'&&s[i+1]<='z')
				{
					i++;
					lit[poz][s[i]]=1;
				}
				i++;
				continue;
			}
			lit[poz][s[i]]=1;
		}
		FOR(i,1,d)
		{
			good=1;
			FOR(j,1,L)
				if (!lit[j][dic[i][j]])
				{
					good=0;
					break;
				}
			if (good)
				nr++;
		}
		fprintf(out,"Case #%d: %d\n",T,nr);
	}
	fclose(in);
	fclose(out);
        return 0;
}
