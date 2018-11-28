#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue> 
#include <cctype> 
#include <cassert>

using namespace std;

#define VV vector
#define PB push_back
#define SZ(v) ((int)(v).size()) 
#define ll long long
#define ld long double
#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi VV<int>
#define vs VV<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))


int main()
{
	//freopen("myinput.txt", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

	int T;
	scanf_s("%d", &T);
	
	rep(i, T)
	{
		int N;
		scanf_s("%d", &N);
		
		int O_pos = 1;
		int B_pos = 1;

		//char * OB = new char[N];
		//int * pos = new int[N];
		
		ll c_time = 0;
		ll o_time = 0;
		ll b_time = 0;
		rep(j, N)
		{
			char k;
			cin >> k;
			int pos;
			cin >> pos;
			//scanf_s("%c",&k);
			//scanf_s("%d",&pos);
			//scanf_s("%c %d",&(OB[j]), &(pos[j]));
			if (k == 'B')
			{
				//
				int tim = abs(B_pos - pos) + 1;
				if (c_time == b_time)// means last move was b
				{
					c_time = c_time + (ll) tim;
					b_time = c_time;
				}
				else if(b_time < c_time) // last move was o
				{
					ll temp = b_time + (ll) tim;
					if (temp > c_time)
					{
						c_time = temp;
						b_time = temp;
					}else
					{
						b_time = c_time + 1;
						c_time = b_time;
					}
				}
				
				B_pos = pos;
			}
			else
			{
				// orange
				//
				int tim = abs(O_pos - pos) + 1;
				if (c_time == o_time)// means last move was b
				{
					c_time = c_time + (ll) tim;
					o_time = c_time;
				}
				else if(o_time < c_time) // last move was o
				{
					ll temp = o_time + (ll) tim;
					if (temp > c_time)
					{
						c_time = temp;
						o_time = temp;
					}else
					{
						//o_time = temp;
						o_time = c_time + 1;
						c_time = o_time;
					}
				}
				
				O_pos = pos;
			}
			
		}
		
		//cout << ans << endl;
		printf("Case #%d: %lld\n", i+1, c_time); // 

		//delete [] OB;
		//delete [] pos;

	}
	
	return 0;
}
