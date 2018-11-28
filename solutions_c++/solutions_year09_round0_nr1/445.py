#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <vector>
#include <set>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;i++)
#define FOR(i,a,b) for(int i=(a),_n=(b);i<=_n;i++)
#define _m(a,b) memset(a,b,sizeof(a))

char dic[5100][20];
char q[1100],temp[1100];
string dum;
vector<string> segment;
int main()
{
	int L,D,N,len;
	
	scanf("%d %d %d",&L,&D,&N);
	REP(i,D) scanf("%s",dic+i);
	REP(ii,N) 
	{
		segment.clear();
		scanf("%s",q);
		len = strlen(q);
		for(int i = 0;i<len;i++)
		{
			if ( q[i] == '(') 
			{
				i++;
				int idx = 0;
				while (q[i]!=')') temp[idx++] = q[i++];
				temp[idx] = 0;
			}
			else temp[0] = q[i],temp[1] = 0;
			dum = temp;
			sort(dum.begin(),dum.end());
			segment.push_back(dum);
		}
		int res = 0;
		REP(i,D)
		{
			int start = 0;
			bool err = false;
			REP(j,L)
			{
				bool found = false;
				REP(k,segment[j].size()) if (dic[i][start] == segment[j][k])
				{
					found = 1;
					break;	
				}
				if (found) start++;
				else 
				{
					err = true;
					break;
				}
			}
			if (!err) res++;
		}
		printf("Case #%d: %d\n",ii+1,res);
	}
	return 0;	
}
