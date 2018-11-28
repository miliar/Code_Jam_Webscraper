#include <iostream>
#include <cassert>
#include <algorithm>
#include <iomanip>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <iterator>
#include <utility>
#include <functional>
#include <bitset>
#include <cctype>
#include <list>
#include <set>
#include <map>
using namespace std;

#define PB push_back
#define PF push_front
#define PP pop()
#define EM empty()
#define FOR(i,a,b) for(int i = (int )a;i<(int )b;i++)
#define REP(i,n) FOR(i,0,n)

typedef pair<int,int> pi;
typedef pair<int,pi> tri;
typedef vector<pi> vii;
typedef vector<tri> viii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<vi> vvi;

int main()
{
	int No;
	char a[100];
	scanf("%d",&No);

	int cases  = 0;
yash:

	while(No--)
	{
		cases++;
		int S,M;
		scanf("%d\n",&S);
		vs SE,Query;
		for(int i=0;i<S;i++)
		{
			gets(a);string in = a;
			SE.PB(in);
		}

		scanf("%d\n",&M);
		vector<pair<int,string> > Q;
		map<string,int> QN;
		REP(i,M){

			gets(a);string in = a;
			Query.PB(in);
			QN[in]++;
		}

		/** Solve **/
		for(int i=0;i<S;i++)
			if(!QN[SE[i]])
			{
				printf("Case #%d: %d\n",cases,0);
				goto yash;
			}


		int ans = 0;
		map<string,int> temp;
		for(int i=0;i<M;i++)
		{
			ans++;
			int count = 0,j;
			for(int j=i;j<M && count<(S-1);j++)
			{
				if(!temp[Query[j]]) count++;
				temp[Query[j]]++;
			}
			int k = 0;
			for(k=0;k<S;k++) if(!temp[SE[k]]) break;
			while(i<M)
			{
				if(Query[i] != SE[k])
					i++;
				else
				{
					i--;
					break;
				}
			}
			temp.clear();
		}
		printf("Case #%d: %d\n",cases,ans-1);
	}
}
