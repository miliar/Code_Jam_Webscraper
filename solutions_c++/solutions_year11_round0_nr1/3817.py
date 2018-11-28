#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
using namespace std;

//#define SMALL
//#define LARGE

int o=1,oprev=1,b=1,bprev=1,opass=0,bpass=0,totaltime=0,loc=0;

int dothis(char a,int bu)
{
  if(a=='O')
  { oprev=o;
		o=bu;
		if(o>oprev)
		{
			if((o-oprev)>opass)
				oprev+=(opass);
			else
				oprev=o;
			loc=(o-oprev);
		}
		else
		{
			if((oprev-o)>opass)
				oprev-=(opass);
			else
				oprev=o;	
			loc=(oprev-o);	
		}
		opass=0;

		bpass+=(loc+1);
		totaltime+=(loc+1);
	}

  if(a=='B')
  { bprev=b;
		b=bu;
		if(b>bprev)
		{
			if((b-bprev)>bpass)
				bprev+=(bpass);
			else
				bprev=b;
			loc=b-bprev;		
		}
		else
		{
			if((bprev-b)>bpass)
				bprev-=(bpass);
			else
				bprev=b;
			loc=bprev-b;		
		}
		bpass=0;
		opass+=(loc+1);
		totaltime+=(loc+1);		
	}
	
return 0;
}

int main() 
{
//  freopen( "a.txt", "rt", stdin); 
///	freopen("atry.out", "wt", stdout);
/*#ifdef SMALL
  freopen("A-small-attempt1.in", "rt", stdin);
  freopen("A-small-attempt1.out", "wt", stdout);
//#endif
#ifdef LARGE
*/  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);
//#endif
	int N;
  cin>>N;
	
	for(int i=0;i<N;i++)
	{ 
		cout<<"Case #"<<i+1<<": ";
		int op;
		cin>>op;
		char a;
		int bu;
		for(int j=0;j<op;j++)
		{
			cin>>a>>bu;
			dothis(a,bu);
		}
		cout<<totaltime<<endl;
		totaltime=0;
		o=1;
		opass=0;
		b=1;
		bpass=0;
	}
	
	return 0;
}
