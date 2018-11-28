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




int main() 
{
//  freopen( "a.txt", "rt", stdin); 
//	freopen("atry.out", "wt", stdout);
/*#ifdef SMALL
 */ freopen("A-small-attempt0.in", "rt", stdin);
  freopen("A-small-attempt0.out", "wt", stdout);
/*#endif
#ifdef LARGE
  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);
*/
//#endif
	int N;
  cin>>N;
	
for(int tt=0;tt<N;tt++)
{ 
cout<<"Case #"<<tt+1<<":\n";

int r,c;
cin>>r>>c;
int b=0;
char a[100][100];
for(int i=0;i<r;i++)
	for(int j=0;j<c;j++)
		{
			cin>>a[i][j];
			if(a[i][j]=='#') b++;
		}

//cout<<b;

if(b%4==0)
{

for(int i=0;i<r;i++)
	for(int j=0;j<c;j++)
		{
			if(a[i][j]=='#')
			{ static int count;

				if(a[i][j+1]=='#' && a[i+1][j]=='#' && a[i+1][j+1]=='#')
				{count++;
//			red++;
				b=b-4;
				a[i][j+1]='\\';a[i+1][j]='\\';a[i+1][j+1]='/';a[i][j]='/';
				} //cout<<count;
}
}

if(b==0)
{

for(int i=0;i<r;i++)
	{for(int j=0;j<c;j++)
		{ cout<<a[i][j];
		}
		cout<<"\n";
	}
}
else goto imp;
}


else
imp:
	cout<<"Impossible\n";

}

}


