#include<cstdio>
#include<climits>
#include<cstdlib>
#include<cmath>
#include<ctime>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>
#include<deque>
#include<fstream>
#include<iostream>
#include<bitset>
#include<set>
#include<map>
#include<list>
#include<string>
using namespace std;
#define pb push_back
#define fs first
#define sc second
#define mp make_pair
#define pii pair< int,int >
#define pss pair< short,short >
#define pdd pair< double,double >
#define ll long long

set< pss > s;
inline void citire()
{
	int r;
	short x1,y1,x2,y2;
	scanf("%d",&r);
	for(int i=0; i<r; ++i)
	{
		scanf("%hd%hd%hd%hd",&x1,&y1,&x2,&y2);
		for(short j=y1; j<=y2; ++j)
		{
			for(short k=x1; k<=x2; ++k)
				s.insert(mp(j,k));
		}
	}
}

inline int rezolva()
{
	int rez=0;
	pss x,y;
	bool da;
	set< pss >::reverse_iterator aux;
	while(!s.empty())
	{
        	da=false;
		set< pss > s1(s);
		for(set< pss >::reverse_iterator it=s1.rbegin(); it!=s1.rend(); ++it)
		{
			x=*it;
                        if(da)
			{
				da=false;
				aux=it;
				--aux;
				s.erase(s.find(*aux));
			}
                        y=x;
			--x.fs;
			--y.sc;
			if(s1.find(x)==s1.end() && s1.find(y)==s1.end())
				da=true;
		}
		if(da)
			s.erase(s.begin());
		++rez;  

		for(set< pss >::reverse_iterator it=s1.rbegin(); it!=s1.rend(); ++it)
		{
			x=*it;
			++x.fs;
			--x.sc;
			if(s1.find(x)!=s1.end())
			{
				++x.sc;
				s.insert(x);
			}
		}
	}

	return rez;
}	
int main()
{
	freopen("pc.in","r",stdin);
	freopen("pc.out","w",stdout);

	int T;
	scanf("%d",&T);
	for(int i=1; i<=T; ++i)
	{
		citire();
		printf("Case #%d: %d\n",i,rezolva());
	}

	return 0;
}

