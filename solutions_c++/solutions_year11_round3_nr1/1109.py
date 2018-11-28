#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define clr(x) memset((x), 0, sizeof(x))
#define SORT(x) sort(x.begin(),x.end())
#define forn(i, n) for(int i = 0; i< n; i++)
#define all(i, x) for(int i = 0; i< x.size(); i++)
const long double EPS = 1e-11;

int T,R,C;
char a[51][51];
int main()
{
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
//	freopen("test.txt","r",stdin);//  freopen("test.out","w",stdout);
//	int i,j;
	cin>>T;
	for(int caseID = 1; caseID <= T; caseID++)
	{	
		cout<<"Case #"<<caseID<<": "<<endl;
		int bn = 0;
		cin>>R>>C;
		forn(i,R)
		{
			forn(j,C)
			{
				cin>>a[i][j];
				if(a[i][j] == '#')
					bn++;
			}
		}
		if(bn%4 != 0)
		{
			cout<<"Impossible"<<endl;
			continue;
		}
		int poss = 1;
		forn(i,R)
		{
			forn(j,C)
			{
				if(a[i][j] == '#')
				{
					if(i+1<R && j+1<C
						&& a[i+1][j] == '#'
						&& a[i][j+1] == '#'
						&& a[i+1][j+1] == '#')
					{
						a[i][j] = '/';
						a[i+1][j] = 92;
						a[i][j+1] = 92;
						a[i+1][j+1] = '/';
					}
					else
					{
						poss = 0;
						break;
					}
				}
			}
			if(poss == 0)
				break;
		}
		if(poss == 0)
			cout<<"Impossible"<<endl;
		else
		{
			forn(i,R)
			{
				forn(j,C)
				{
					cout<<a[i][j];
				}
				cout<<endl;
			}
		}
//		cout<<endl;		
	}
//	while(1);

	return 0;
}