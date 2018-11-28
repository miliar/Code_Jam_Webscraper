#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <ctype.h>
#include <queue>
using namespace std;



struct Chick
{
	int x,v;
	bool can;
};
int Finish;
vector <Chick> arr;
vector <Chick> tarr;
int n,needChick;
int maxTime;

bool Check(int swaps)
{
	int arrived = 0;
	int bad = 0;
	for (int i = n-1; swaps >= 0 && i >= 0; i --)
	{
		if (!arr[i].can)
		{
			bad ++;
			continue;
		}
		if (swaps < bad)
			break;
		swaps -= bad;
		arrived ++;
	}
	return arrived >= needChick;
}



int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t ;
	cin >> t;
	for (int test = 0; test < t ; test ++)
	{
		cin >> n >> needChick >> Finish >> maxTime;
		tarr.resize(n);
		for (int i = 0; i < n; i ++)
			cin >> tarr[i].x;
		for (int i = 0; i < n; i ++)
			cin >> tarr[i].v;	
		int maxArrive = 0;
		for (int i = 0; i < n; i ++)
		{
			tarr[i].can = (Finish-tarr[i].x) <= maxTime*tarr[i].v;
			if (tarr[i].can)
				maxArrive++;
		}
		if (maxArrive < needChick)
		{
			cout << "Case #" << test+1 << ": " << "IMPOSSIBLE" << endl;
			continue;			
		}
		int l = 0, r = 2501;
		while (l < r)
		{
			arr = tarr;
			int m = (l+r)/2;
			if (Check(m))
				r = m;
			else
				l = m+1;
		}
		cout << "Case #" << test+1 << ": " << r << endl;
	}
	return 0;
}
