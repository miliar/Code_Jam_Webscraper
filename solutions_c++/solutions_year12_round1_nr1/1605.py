#pragma comment(linker, "/STACK:16777216")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <utility>

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )

using namespace std;

int t,a,b;
vector<double> ans;
vector<double> probs;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;
	forn(i,t)
	{
		probs.clear();
		ans.clear();
		cin >> a >> b;
		probs.resize(a);
		forn(j,a)
			cin >> probs[j];
	    double prob = 1.0;
		forn(j,a)
			prob *= probs[j];
		ans.push_back(prob * (b-a+1) + (1-prob)*(b-a+1+b+1));
		forn(j,a)
		{
			int kol = a - j - 1;
			prob = 1.0;
			forn(k,kol)
				prob *= probs[k];
			ans.push_back(prob * (b-kol+j+1+1) + (1-prob)*(b-a+2+j+1+b+1));
		}
		ans.push_back(2+b);
		double minn = 1e9;
		forn(j,ans.size())
			minn = min(minn,ans[j]);
		cout << "Case #" << i+1 << ": ";
		printf("%.6f",minn);
		cout << endl;
	}
	return 0;
}