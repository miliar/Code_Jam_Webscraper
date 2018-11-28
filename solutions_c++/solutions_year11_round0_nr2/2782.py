/*
** In the name of God **
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it))
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define EPS 1e-8
#define MOD 1000000007
#define INF 100000000
#define SQR(a) ((a)*(a))
#define pb push_back
typedef long long ll;
typedef unsigned long long ull;
typedef long double lld;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
#define ORANGE true
#define BLUE false
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tnum;
	scanf("%d",&tnum);
	map<string,char> mp;
	map<char,char> mp2;
	int C,D,N;
	char ch,ch2;
	string st(2,'0');
	FOR(q,1,tnum+1)
	{
		mp.clear();
		mp2.clear();
		scanf("%d",&C);
		FR(i,C)
		{
			scanf(" %c%c%c",&st[0],&st[1],&ch);
			mp[st]=ch;
			swap(st[0],st[1]);
			mp[st]=ch;
		}
		scanf("%d",&D);
		FR(i,D)
		{
			scanf(" %c%c",&ch,&ch2);
			mp2[ch]=ch2;
			mp2[ch2]=ch;
		}
		int visited[30]={0};
		scanf("%d",&N);
		char s[200];
		scanf("%s",s);
		string ans;
		for(int i=0;s[i];i++)
		{
			visited[s[i]-'A']++;
			ans+=s[i];
			int len = ans.size();
			if(len>1)
			{
				st[0]=ans[len-2];st[1]=ans[len-1];
				while(mp.find(st)!=mp.end())
				{
					visited[ans[len-1]-'A']--;
					visited[ans[len-2]-'A']--;
					ans.erase(ans.end()-2,ans.end());
					ans+=mp[st];
					len--;
					visited[ans[len-1]-'A']++;
					if(len<2)break;
					st[0]=ans[len-2];
					st[1]=ans[len-1];				
				}
				if(len>1)
				{
					ch=ans[len-1];
					if(mp2.find(ch)!=mp2.end())
					{
						if(visited[mp2[ch]-'A']>0)
						{ CLR(visited,0); ans.clear();}
					}
				}
			}
		}
		printf("Case #%d: [",q);
		FR(i,ans.size())
			if(i==0)printf("%c",ans[i]);
			else printf(", %c",ans[i]);
		printf("]\n");
		
	}

}