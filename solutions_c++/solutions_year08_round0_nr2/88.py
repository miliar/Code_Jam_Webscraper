#include <cstdio>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>

#include <set>
#include <vector>
#include <utility>
#include <map>

#include <algorithm>
#include <cassert>

using namespace std;


typedef pair<int,int> pii;
typedef vector<string> VS;
typedef vector<int> VI;

typedef __int64 ll;

#define all(v) (v).begin(),(v).end()
#define foreach(it, v, type) for(type::iterator it = (v).begin(); it != (v).end(); ++it)
#define pb push_back
#define forn(i,N) for(int i=0;i<(N); ++i)

FILE * f = fopen("b-large.in","rt");
//FILE * g = fopen("b-mine.out","wt");
//ifstream f("c-large.in",ifstream::in);
ofstream g("b-large.out",ofstream::out);

struct sched
{
	int dep; int arr;
	int side;
};

struct orderCmp
{
	bool operator() (const sched& sh1, const sched& sh2)
	{
		return sh1.dep < sh2.dep;
	}
};

//get a first available train for this scheduled
VI::iterator findAvail(VI& v, int dep)
{
	foreach(it,v,VI)
		if (*it<=dep)
			return it;
	return v.end();
}
int main()
{
	int Tests; /*f>>Tests;*/
	fscanf(f,"%d",&Tests);
	string s;

	forn(TestIndex,Tests)
	{
		//fprintf(g,"Case #%d: ",TestIndex+1);
		g<<"Case #"<<TestIndex+1<<": ";
		cout<<"Case #"<<TestIndex+1<<": "<<endl;
		int na, nb;
		int t;
		fscanf(f,"%d\n",&t);
		fscanf(f,"%d %d\n",&na,&nb);
		vector<sched> Orders;
		forn(i,na+nb)
		{
			int h1, m1, h2, m2;
			fscanf(f,"%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
			sched sh;
			sh.dep = h1*60 + m1;
			sh.arr = h2*60 + m2;
			sh.side = (i<na)?0:1;
			Orders.pb(sh);
		}
		sort(all(Orders),orderCmp());
		
		vector<VI> Tr(2);
		VI Count(2,0);
		
		while (Orders.size())
		{
			sched sh = Orders.front();
			Orders.erase(Orders.begin());
			
			VI::iterator it =findAvail(Tr[sh.side],sh.dep);
			
			if (it==Tr[sh.side].end())
			{
				Tr[sh.side].push_back(0);
				Count[sh.side]++;
			}
			
			it =findAvail(Tr[sh.side],sh.dep);
			assert(it !=Tr[sh.side].end());

			//move this train to the other side
			Tr[sh.side].erase(it);
			Tr[1-sh.side].pb(sh.arr+t);
		}

		g<<Count[0]<<" "<<Count[1]<<endl;
	}
	return 0;
}