#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <stdio.h>

#define forp(a,b,i) for (int i = a; i < b; i++)
#define pb push_back
#define mp make_pair

using namespace std;

int c;
int l,h;
vector<long long> freq;

bool divable(int a, int b)	{
	int mi = min(a,b);
	int mx = max(a,b);
	return mx % mi == 0;
}

int main()	{

	int t;
	cin >> t;
	forp(0,t,z)	{
		cin >> c >> l >> h;
		freq.clear();
		forp(0,c,i)	{
			long long blah;
			cin >> blah;
			freq.pb(blah);
		}
		
		int pos = -1;
		forp(l,h+1,i)	{
			bool yes = true;
			forp(0,freq.size(),j)	{
				yes &= divable(i,freq[j]);
			}
			if (yes)	{
				pos = i;
				break;
			}
		}
		if (pos == -1)	{
			cout << "Case #" << (z+1) <<": NO" << endl;
		} else	{
			cout << "Case #" << (z+1) <<": " << pos << endl;
		}
	}
}