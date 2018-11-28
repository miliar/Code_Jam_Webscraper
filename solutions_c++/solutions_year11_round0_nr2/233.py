// zero.lin`s google_codejam.cpp 
//


#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <cctype>
#include <cmath>


#include "google_codejam\stdafx.h"
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef long long ll;

#define rep(i,n) for(int i=0;i<n;++i)
#define all(n) n.begin(),n.end()
#define sz(o) (int)(o.size())
#define mset(o,v) memset(o,v,sizeof(o))
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define mk(first,second) make_pair(first,second)
#define present(container, element) (container.find(element) != container.end()) 
#define cpresent(container, element) (find(all(container),element) != container.end())

const int inf=1<<28;
const double eps=1e-11;

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d",&testcase);
	
	rep(caseID,testcase)
	{
		int c,o;
		vector<char> s;
		scanf("%d ",&c);
		char m[26][26];
		char d[26][26];
		mset(m,0);
		mset(d,0);
		for(int i=0;i<c;++i)
		{
			char a,b,c;
			scanf("%c%c%c ",&a,&b,&c);
			m[a-'A'][b-'A']=c;
			m[b-'A'][a-'A']=c;
		}
		scanf("%d ",&o);
		for(int i=0;i<o;++i)
		{
			char a,b;
			scanf("%c%c ",&a,&b);
			d[a-'A'][b-'A']=-1;
			d[b-'A'][a-'A']=-1;
		}
		int n;
		scanf("%d ",&n);
		int have=0;
		for(int i=0;i<n;++i)
		{
			char now;
			scanf("%c",&now);
			if(have>0 && m[now-'A'][s[have-1]-'A']>0)
			{
				char l=s[have-1];
				s.pop_back();
				s.push_back(m[now-'A'][l-'A']);
			}
			else
			{
				bool ok=true;
				for(int j=0;j<s.size();++j)
				{
					if(d[now-'A'][s[j]-'A']==-1)
						ok=false;
				}
				if(ok)
				{	s.push_back(now);
					have++;
				}
				else
				{
						s.resize(0);
						have=0;
				}
			}
		}
		printf("Case #%d: [",caseID+1);
		for(int i=0;i<have-1;++i)
		{
			printf("%c, ",s[i]);
		}
		if(have>0)
			printf("%c",s[s.size()-1]);
		printf("]\n");
	}
	
	return 0;
}

