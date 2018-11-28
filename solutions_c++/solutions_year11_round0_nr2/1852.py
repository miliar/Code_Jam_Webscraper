//Author : Nitin Gangahar
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <iostream>
#include <cstring>
#include <set>
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define MAX 103
#define isok(x,y) (x>=0 && x<R && y>=0 && y<C)

using namespace std;

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< VI > VII;
int C,D,N;
char temp[4];
map < pair<char,char>, char> CMAP;
set < pair<char,char> > OSET;
vector<char> Q;
char STR[MAX];
inline bool can_combine(char a,char b)
{
	if((CMAP.find(mp(b,a)) != CMAP.end()))
		return true;
	return false;
}
inline bool opposes(char a)
{
	for(int i=0;i<Q.size();i++)
	{
		char tc = Q[i];
		if((OSET.find(mp(a,tc)) != OSET.end()) || (OSET.find(mp(tc,a)) != OSET.end()))
			return true;
	}
	return false;
}
int main()
{
	int T;
	scanf("%d",&T);
	int cases = 1;
	while(T--)
	{
		CMAP.clear();
		OSET.clear();
		Q.resize(0);
		scanf("%d",&C);
		for(int i=0;i<C;i++)
		{
			scanf("%s",temp);
			CMAP[mp(temp[0],temp[1])] = temp[2];
			CMAP[mp(temp[1],temp[0])] = temp[2];
		}
		scanf("%d",&D);
		for(int i=0;i<D;i++)
		{
			scanf("%s",temp);
			OSET.insert(mp(temp[0],temp[1]));
			OSET.insert(mp(temp[1],temp[0]));
		}
		scanf("%d",&N);
		scanf("%s",STR);

		for(int i=0;i<N;i++)
		{
			if(Q.size() != 0)
			{
				char cl = STR[i];
				char last = Q[Q.size()-1];
				if(can_combine(cl,last))
				{
					Q.erase(Q.end()-1);
					Q.pb(CMAP[mp(cl,last)]);
				}
				else if(can_combine(cl,last))
				{
					Q.erase(Q.end()-1);
					Q.pb(CMAP[mp(cl,last)]);
				}
				else if(opposes(cl)) //if it opposes anything in the list
				{
					//printf("list being cleared\n");
					Q.clear();
				}
				else
					Q.pb(cl);
			}
			else
			{
				//printf("Pushing %c\n",STR[i]);
				Q.pb(STR[i]);
			}
		}
		printf("Case #%d: ",cases++);
		if(Q.size() > 1)
		{
		printf("[");
		for(int i=0;i<Q.size()-1;i++)
			printf("%c, ",Q[i]);
		printf("%c]\n",Q[Q.size()-1]);
		}
		else if(Q.size() == 1)
			printf("[%c]\n",Q[0]);
		else
			printf("[]\n");
		
	}	
	return 0;
}
