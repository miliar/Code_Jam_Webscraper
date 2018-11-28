// Sai
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


int r,c;
char inp[55][55];

bool check(int x,int y)
{	
	if(inp[x][y]!='#') return true;
	if(x+1<r && y+1<c)
	{
	if(inp[x+1][y]!='#' || inp[x][y+1]!='#' || inp[x+1][y+1]!='#')
		return false;
	inp[x][y]='/';	inp[x+1][y+1]='/';
	inp[x+1][y]='\\';inp[x][y+1]='\\';
	return true;
	}
	return false;
}

int main()
{
	freopen("square_tiles_l.in","r",stdin);
	freopen("square_tiles_l.out","w",stdout);
	int no_of_testcases;
	cin>>no_of_testcases;
	for(int tcase=1;tcase<=no_of_testcases;++tcase)
	{
		cin>>r>>c;
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
				cin>>inp[i][j];
		bool possible=true;
		for(int i=0;i<r && possible;i++)
			for(int j=0;j<c && possible;j++)
				if(check(i,j)==false)
					possible=false;
		cout<<"Case #"<<tcase<<":\n";
		if(possible)
		{
			for(int i=0;i<r;i++)
			{
				for(int j=0;j<c;j++)
					cout<<inp[i][j];
				cout<<endl;
			}
		}
		else
			cout<<"Impossible"<<endl;
	}
}
