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

long long l;
long long t;
long long n;
long long c;
vector<long long> p;
long long tp;
vector<long long> res;

void solve(int kase)	{

	long long k = tp / t;
	int curIndex = 0;
	long long tot = 0;
	forp(0,c,i)	{
		
	}
	
	long long placesleft = n - (k * c);
	
}

void brute(int kases)	{
	
	int curI = 0;
	long long tot = 0;
	long long curN = 0;
	while (tot + (p[curI]*2) <= t && curN != n-1)	{
		tot += p[curI] * 2;
		curI = (curI + 1) % c;
		curN++;
	}
	
	res.clear();
	res.pb(((tot + (p[curI]*2)) - t) / 2);
	tot += p[curI] * 2;
	forp(curN+1,n,i)	{
		res.pb(p[i % c]);
		tot += p[i%c] * 2;
	}
	
	sort(res.begin(), res.end());
	int curIndex = res.size() -1;
	forp(0,l,i)	{
		if (curIndex < 0)
			break;
// 		cout << res[curIndex] << " " << curIndex << endl;
		tot -= res[curIndex];
		curIndex--;
	}
	
	cout << "Case #" << kases << ": " << tot << endl;
}

int main()	{

	int asdf;
	cin >> asdf;
	forp(0,asdf,z)	{
		cin >> l >> t >> n >> c;
		p.clear();
		tp = 0;
		
		forp(0,c,i)	{
			long long blah;
			cin >> blah;
			p.pb(blah);
			tp += blah;
		}
		
		brute(z+1);
		cerr << (z+1) << "/" << asdf << endl;
	}
}