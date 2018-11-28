#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <deque>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <sstream>

#define For(i,a,n) for(int i =a ; i < n ; ++i )
#define all(x) (x).begin(),(x).end()
#define n(x) (int)(x).size()
#define pb(x) push_back(x)

using namespace std;
typedef pair<int,int> pii;
int po[9]={1,10,100,1000,10000,100*1000,1000*1000,10*1000*1000,100*1000*1000};
int t;
int a;
int b;
int ln(int x)
{
	int ret = 0;
	while(x)
	{
		x/=10;
		ret++;
	}
	return ret;
}

int d[8];

int check(int x) 
{	
	int bx = x;
	int p =ln(x);
	int ret = 0;
	For(i,0,p)
	{
		x=(x+(x%10)*po[p])/10;
		if(x <= b && x >= a && bx < x)
		{
			d[i] = x;
			bool bo =false;
			For(j,0,i)
				if(d[j]==x)
				{
//					cerr << bx << " with " << x << " FAILD BY " << j  << " " << i << endl;
					bo = true;
					break;
				}
			if(bo)
				continue;
			ret++;
//			cerr << bx << " with " << x << endl;
		}
		else
			d[i] = -1;
	}
	return ret;
}

int main()
{
	ios::sync_with_stdio(false);
	cin >> t;
	For(it,0,t)
	{
		cin >> a >> b;
		int ans=0;
		For(i,a,b+1)
			ans+=check(i);
		cout << "Case #" << it+1 << ": " << ans << endl;
	}
	return 0;
}
