
#include <vector>
#include <list>
#include <map>
#include <set>
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
#define pb push_back
#define mkp make_pair
#define vi vector<int>
#define vii vector<int> :: iterator
#define si set <int>
#define sii set <int> :: iterator
#define is insert
#define vpi vector <pair<int,int> >
#define vpii vector <pair <int,int> > :: iterator
#define spi set <pair<int,int> >
#define spii set <pair <int,int> > :: iterator
#define for_each(tip,it,multime) for( tip it = multime.begin();it!=multime.end();++it)

using namespace std;


int n;

char buff[1000];

int main()
{

	
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	int t;
	
	scanf("%d",&t);
	
	for(int tt=0;tt<t;tt++)
	{
		vector<int> poz;

		scanf("%d",&n);
		fgets(buff,1000,stdin);
		
		for(int j=0;j<n;j++)
		{
			fgets(buff,1000,stdin);
			int last = -1;
			for(int i=0;i<n;i++)
			{
				if( buff[i]  == '1' ) last = i;
			}
			poz.pb(last);
		}

		int ans = 0 , tmp;

		for(int j=0;j<n;j++)
		{
			for(int i=j;i<n;i++)
			{	
				if( poz[i] <= j )
				{
					for( int k= i; k >=j+1; k--)
					{
						ans++;
						tmp = poz[k];
						poz[k] = poz[k-1];
						poz[k-1] = tmp;
					}
					break;
				}
			}
		}		


		printf("Case #%d: %d\n",tt+1,ans);
	
	
	}
	
	return 0;
}
