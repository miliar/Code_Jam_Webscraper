#include <stdio.h>
#include <set>
#include <algorithm>
#include <assert.h>

using namespace std;

#define MAX 200

pair<pair<int,int>, int> sc[MAX];
/*
 * sc[i].first.first  : minuto de partida
 * sc[i].first.second : minuto de chegada
 * sc[i].second       : estacao de partida
 */
int s[2];

int solve(int n,int t)
{
	multiset<pair<int,int> > arrival;
	/*
	 *  .first    : horario de diponibulidade
	 *  .second   : estacao em que ficara disponivel
	 */
	int c[2]={0,0};
	int i;
	pair<int,int> tmp;
	sort(sc, sc+n);
	s[0]=s[1]=0;
	for(i=0;i<n;++i)
	{
		while(!arrival.empty() && (*(arrival.begin())).first<=sc[i].first.first)
		{
			++c[(*(arrival.begin())).second];
			arrival.erase(arrival.begin());
		}
		if(c[sc[i].second]==0)
		{
			++s[sc[i].second];
			++c[sc[i].second];
		}
		--c[sc[i].second];
		tmp.first=sc[i].first.second+t;
		tmp.second=!sc[i].second;
		assert(tmp.second==0 || tmp.second==1);
		arrival.insert(tmp);
	}
	return 0;
}

int main()
{
	int t;
	int na,nb;
	int i;
	int t1,t2;

	int cnt, ncase;

	scanf("%d",&ncase);
	for(cnt=1;cnt<=ncase;++cnt)
	{
		scanf("%d %d %d",&t,&na,&nb);
		for(i=0;i<na+nb;++i)
		{
			scanf("%d:%d",&t1,&t2);
			//printf("%02d:%02d\n",t1,t2);
			sc[i].first.first=60*t1+t2;
			scanf("%d:%d",&t1,&t2);
			//printf("%02d:%02d\n",t1,t2);
			sc[i].first.second=60*t1+t2;
			assert(sc[i].first.first!=sc[i].first.second);
			sc[i].second=i>=na;
			assert(sc[i].second==0 || sc[i].second==1);
		}
		solve(na+nb,t);
		printf("Case #%d: %d %d\n",cnt,s[0],s[1]);
	}
	return 0;
}

