#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>

#define mn(a,b) ((a<b) ? (a) : (b))        		
#define mx(a,b) ((a<b) ? (b) : (a))			
#define ab(a) ((a<0) ? (-(a)) : (a))			
#define fr(a,b) for(int a=0; a<b; ++a)			
#define fe(a,b,c) for(int a=b; a<c; ++a)		
#define fw(a,b,c) for(int a=b; a<=c; ++a)		
#define df(a,b,c) for(int a=b; a>=c; --a)		
#define BIG 1000000000	
#define MAX_STRING 100000
#define PB push_back
#define MP make_pair
#define X first
#define Y second

using namespace std;

set<pair<int,int> > cur;
map<pair<int,int>, int> next;
vector<pair<int,int> > tor;
int c,r,t;
pair<int,int> a,b;
set<pair<int,int> >::iterator it,jt;
map<pair<int,int>, int>::iterator mit;

int main()
{
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
scanf("%d", &c);
fw(test,1,c)
	{
	t = 0;
	scanf("%d", &r);
	cur.clear();

	fr(i,r)
		{
		scanf("%d%d%d%d", &a.X, &a.Y, &b.X, &b.Y);
		if(a.X>b.X) swap(a.X, b.X);	
		if(a.Y>b.Y) swap(a.Y,b.Y);
		fw(x,a.X,b.X)
		fw(y,a.Y,b.Y)
			cur.insert(MP(x,y));
		}
	while(cur.size()>0)
		{
//		cout<<"Next loop"<<endl;
		tor.clear();
		next.clear();
		for(it=cur.begin(); it!=cur.end(); it++)
			{
//			cout<<"Element: "<<(*it).X<<" "<<(*it).Y<<endl;
			a = b = (*it);
			a.X--;
			b.Y--;
			if(cur.find(a)==cur.end()&&cur.find(b)==cur.end())
				{
//				cout<<"To remove: "<<(*it).X<<" "<<(*it).Y<<endl;
				tor.PB(*it);	
				}
			a = b = (*it);
			a.X++;
			b.Y++;
			if(next.find(a)==next.end())
				next[a] = 1;
			else next[a]++;
			if(next.find(b)==next.end())
				next[b] = 1;
			else next[b]++;
			}
		fr(i,tor.size())
			cur.erase(tor[i]);
		for(mit=next.begin(); mit!=next.end(); mit++)
			if((*mit).Y>=2) cur.insert((*mit).X);		
		t++;
		}
	printf("Case #%d: %d\n", test, t);
	
	}
return 0;
}
