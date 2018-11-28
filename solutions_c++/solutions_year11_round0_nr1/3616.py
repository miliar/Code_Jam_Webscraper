#include <cstring>
#include <stdio.h>
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

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define pb push_back

typedef stringstream ss;
typedef long long ll;
typedef pair<int, int> pii;
typedef long double ld;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

int compFloats(const double &a, const double &b) {
  if (fabs(a - b) < eps)
    return 0;
  return a > b ? 1 : -1;
}

int totalButtonCount;
vector<pair<char,int> > jobs;
queue<int>BlueIndices;
queue<int>OrangeIndices;

int calc()
{
	int res=0 , BlueIndex=0 , OrangeIndex=0 , nextBlueTarget , nextOrangeTarget;
	pair<char,int> nextJob;
	BlueIndex = OrangeIndex = 0;
	bool freeOrange , freeBlue,d1,d2;
	freeOrange = freeBlue = true;
	for (int qj = 0; qj < totalButtonCount; ++qj) {
		nextBlueTarget = BlueIndices.front();
		nextOrangeTarget = OrangeIndices.front();

		nextJob = jobs[qj];

		if(nextJob.first=='B')
			BlueIndices.pop();
		else
			OrangeIndices.pop();

		freeBlue = BlueIndex==nextBlueTarget ? true:false;
		freeOrange = OrangeIndex==nextOrangeTarget ? true:false;

		while(true)
		{
			if((nextJob.first=='B' && BlueIndex==nextJob.second) || (nextJob.first=='O' && OrangeIndex==nextJob.second))
			{
				if(BlueIndex < nextBlueTarget)
					BlueIndex++;
				else if(BlueIndex>nextBlueTarget)
					BlueIndex--;
				if(OrangeIndex < nextOrangeTarget)
					OrangeIndex++;
				else if(OrangeIndex > nextOrangeTarget)
					OrangeIndex--;
				res++;
				break;
			}
			d1=d2=false;
			if(!freeBlue)
			{
				if(BlueIndex == nextBlueTarget)
					freeBlue = true;
				d1=true;
				if(BlueIndex < nextBlueTarget)
					BlueIndex++;
				else if(BlueIndex > nextBlueTarget)
					BlueIndex--;
			}

			if(!freeOrange)
			{
				if(OrangeIndex == nextOrangeTarget)
					freeOrange = true;
				d2=true;
				if(OrangeIndex < nextOrangeTarget)
					OrangeIndex++;
				else
					OrangeIndex--;
			}
			if(d1||d2)
				res++;
		}
	}
	return res;
}


int main()
{
	freopen("aLarge.in","r",stdin);
	freopen("aLarge.out","w",stdout);
	int tc,dummy;
	string c;
	cin>>tc;
	for (int i = 0; i < tc; ++i) {
		jobs.clear();
		while(BlueIndices.size()>0)
			BlueIndices.pop();
		while(OrangeIndices.size()>0)
			OrangeIndices.pop();
		cout<<"Case #"<<i+1<<": ";
		cin>>totalButtonCount;
		for (int j = 0; j < totalButtonCount; ++j) {
			cin>>c>>dummy;
			jobs.pb(mp(c[0],--dummy));
			switch(c[0])
			{
				case 'B':
					BlueIndices.push(dummy);
					break;
				default:
					OrangeIndices.push(dummy);
			}
		}
		cout<<calc()<<endl;
	}
	return 0;
}
