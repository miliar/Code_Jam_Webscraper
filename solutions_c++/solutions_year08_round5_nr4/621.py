#include <iostream>
#include <sstream>
#include <cmath>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <bitset>
#include <map>
#include <algorithm>
#include <fstream>
#include <set>
using namespace std;

int h,w,r;
struct two{
	int x;
	int v;
};
struct comp
{
  bool operator()(const two s1, const two s2) const
  {
    return s1.x < s2.x;
  }
};

set < two, comp> hh[10000];
int hash_get(int x,int y,int val)
{
	int key=x*w+y;
	int key2=key%9997;
	int i;
	two temp;
	temp.x=key;
	temp.v=val;
	set<two,comp>::iterator m=hh[key2].find(temp);

	if( m==hh[key2].end())
	{
		if( val>=0)
			hh[key2].insert(temp);
		return -1;
	}
	else
		return (*m).v;
}
int recur(int x,int y)
{
	if( x==0 && y==0) return 1;
	if( x<0 || y<0) return 0;
	int v=hash_get(x,y,-1);
	if( v >=0)
		return v;
	int sum=recur(x-1,y-2);
	sum+=recur(x-2,y-1);
	hash_get(x,y,sum%10007);
	return sum%10007;
}
void main()
{
	int z,t;
	ifstream in("input.txt");
	ofstream out("output.txt");
	in>>t;
	for(z=0;z<t;z++)
	{
		in>>h>>w>>r;
		
		int i;
		for(i=0;i<10000;i++)
			hh[i].clear();
		for(i=0;i<r;i++)
		{
			int r,c;
			in>>r>>c;
			hash_get(r-1,c-1,0);
		}
		int x=recur(h-1,w-1);
		out<<"Case #"<<z+1<<": "<<x<<endl;
	}
}