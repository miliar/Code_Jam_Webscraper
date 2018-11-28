#include <iostream>
#include <cstdio>
#include <map>
#include <vector>
#include <set>
#include <numeric>
#include <iterator>
#include <sstream>
#include <queue>
#include <list>

#define pb push_back
#define mp make_pair
#define foreach(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();++i)

using namespace std;

const int dirx[] = {0, 1, 0, -1};
const int diry[] = {1, 0, -1, 0};

void process(int tcase)
{
    int n;
    int dir=0;
    int x=0,y=0;
    vector<int> xs[6010],ys[6010];
    cin >> n;
    for(int i=0;i<n;i++)
    {
	string str;
	int time;
	cin >> str >> time;
	for(int j=0;j<time;j++) for(int k=0;k<str.size();k++)
	{
	    if(str[k] == 'F')
	    {
		int nx = x+dirx[dir];
		int ny = y+diry[dir];
		if(x == nx) 
		    ys[x+3005].pb(min(y,ny)+3005);
		else
		    xs[y+3005].pb(min(x,nx)+3005);
		x=nx,y=ny;
	    }
	    if(str[k] == 'R') dir = (dir + 1) % 4;
	    if(str[k] == 'L') dir = (dir + 3) % 4;
	}
    }

    set<pair<int,int> > S,S2,S3;
    set<int> V;

    for(int i=0;i<6010;i++) 
    {
	sort(xs[i].begin(),xs[i].end());
	for(int j=0;j<xs[i].size();j++)
	    if(V.count(xs[i][j])) V.erase(xs[i][j]); else V.insert(xs[i][j]);
	foreach(j,V) 
	{
	    S.insert(mp(i,*j));
	    S2.insert(mp(*j,i));
	}
    }

    int curx=-1,cury;
    foreach(i,S)
    {
	if(i->first != curx) 
	{
	    curx = i->first, cury = i->second;
	}
	else
	{
	    if(cury + 1 < i->second)
	    {
		for(int j=cury+1;j<i->second;j++)
		    S3.insert(mp(curx,j));
	    }
	    cury = i->second;
	}
    }
    cury = -1;
    foreach(i,S2)
    {
	if(i->first != cury)
	{
	    cury = i->first; curx = i->second;
	}
	else
	{
	    if(curx + 1 < i->second)
	    {
		for(int j=curx+1;j<i->second;j++)
		    S3.insert(mp(j,cury));
	    }
	    curx = i->second;
	}
    }

    cout << "Case #" << tcase << ": " << S3.size() << endl;
}

int main(void)
{
    int T;
    cin >> T;
    for(int t=1;t<=T;t++)
    {
        process(t);
    }
}
