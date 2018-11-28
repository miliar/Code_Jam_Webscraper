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
		int n,m;
		scanf("%d %d ",&n,&m);
		char word[10000][11];
		for(int i=0;i<n;++i)
		{
			scanf("%s ",word[i]);
		}
		
		printf("Case #%d: ",caseID+1);
		for(int k=0;k<m;++k)
		{
			char or[27];
			scanf("%s ",or);
			char order[26];
			for(char i=0;i<26;++i)
				order[or[i]-'a']=i;
			int best=0;
			int Max=0;
			for(int i=0;i<n;++i)
			{
				set<int> have;
				for(int j=0;word[i][j]!=0;++j)
					have.insert(order[word[i][j]-'a']);
				int org=have.size();
				for(int j=0;j<n;++j){
					if(strlen(word[i])!= strlen(word[j]))
						continue;
					int Min=-1;
					for(int l=0;word[i][l]!=0;++l)
					{
						if(word[i][l]!=word[j][l])
						{
							int first=min(order[word[i][l]-'a'],order[word[j][l]-'a']);
							if(Min==-1)
								Min=first;
							else
								Min=min(Min,first);
						}
					}
					if(Min!=-1)
						have.insert(Min);
				}
				if(have.size()-org>Max)
				{
					Max=have.size()-org;
					best=i;
				}
			}
			printf("%s ",word[best]);
		}
		printf("\n");
		
	}
	
	return 0;
}

