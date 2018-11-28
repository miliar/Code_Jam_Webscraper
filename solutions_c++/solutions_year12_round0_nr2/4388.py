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
#include <string>
#include <cstring>
#include <queue>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()

typedef long long ll;

int main (){
	freopen ("Bl.in" , "rt" , stdin);
	freopen ("Bl.out" , "wt" , stdout);

	int tests , c = 1 , googlers , surprising , p,temp ;
	cin>>tests;
	while(tests--)
	{
		int res = 0 ;
		cin>>googlers>>surprising>>p;
		for(int i=0 ; i<googlers ; i++)
		{
			cin>>temp;
			if(temp == 0)
			{
				if(p==0)
					res++;
				continue;
			}
			if(temp/3 >= p)
				res++;
			else if(surprising>0 && temp/3 == p-1 && temp%3 == 0)
				res++ , surprising--;
			else if ( temp/3 == p-1 && temp%3 == 1)
				res++ ;
			else if(temp/3 == p-1 && temp%3 == 2)
				res++;
			else if(surprising>0 &&temp/3 == p-2 && temp%3 == 2)
				res++ , surprising--;
		}

		cout<<"Case #"<<c<<": "<<res<<endl;
		c++;
	}

	return 0;
}
