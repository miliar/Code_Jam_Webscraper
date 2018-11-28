#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <utility>

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define pi 2*acos(0.0)
#define eps 1e-9
#define INF 1000000000
#define LL long long
#define PII pair<int,int> 
#define PDD pair<double,double> 

using namespace std;

int musuh[30],comb[30][30];
int ada[30];
int T,x,y,z,A,a,b;
string ans;
char urut[100],list[5];

int main()
{
	scanf("%d",&T);
	for(x=1;x<=T;x++)
	{
		ans.clear();
		memset(musuh,-1,sizeof(musuh));
		memset(comb,-1,sizeof(comb));
		memset(ada,0,sizeof(ada));
		
		scanf("%d",&A);
		while(A--)
		{
			scanf("%s",list);
			a=list[0]-'A',b=list[1]-'A';
			comb[a][b] = comb[b][a] = list[2]-'A';
		}
		
		scanf("%d",&A);
		while(A--)
		{
			scanf("%s",list);
			a=list[0]-'A',b=list[1]-'A';
			musuh[a]=b,musuh[b]=a;
		}
		
		scanf("%d",&A);
		scanf("%s",urut);
		
		for(z=0;z<A;z++)
		{
			ans+=urut[z];
			ada[urut[z]-'A']++;
			if(ans.size()==1) continue;
			
			b=ans[ans.size()-2],a=ans[ans.size()-1];
			if(comb[b-'A'][a-'A']!=-1)
			{
				ans.erase(ans.size()-2,2);
				ada[a-'A']--,ada[b-'A']--;
				ada[comb[b-'A'][a-'A']]++;
				ans+=(comb[b-'A'][a-'A']+'A');
			} else
			
			if((musuh[a-'A']!=-1)&&(ada[musuh[a-'A']]))
			{
				memset(ada,0,sizeof(ada));
				ans.clear();
			}
		}
		
		printf("Case #%d: [",x);
		for(y=0;y<ans.size();y++)
		{
			if(y) printf(", ");
			printf("%c",ans[y]);
		}
		printf("]\n");
	}
	return 0;
}

