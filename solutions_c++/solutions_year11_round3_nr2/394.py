#include<iostream>
#include<vector>
#include<cstring>
#include<stdio.h>
#include<string>
#include<cassert>
#include<algorithm>
using namespace std;

#define forn(i,n) for (int i=0;i<(n);i++)
#define init(a,v) memset(a,v,sizeof(a))
#define gi(t) scanf("%d",&(t))
#define sz 1000010

int l, c, n, cnt;
long long t;
long long ele[sz];
long long sum[sz];
long long save; 

bool UDF(pair <int, int> p1, pair <int, int> p2) {
	return (p1.first > p2.first);
}

int main ()
{
    int nTest; gi(nTest);
    forn(test, nTest)
    {
		cin >> l >> t >> n >> c;
		forn(i, n) {
			if (i < c) cin >> ele[i];
			else ele[i] = ele[i-c];
		}

		forn(i, n) {
			if (i) sum[i] = sum[i-1] + 2*ele[i];
			else sum[i] = 2*ele[i];
		}

		int index = n; 
		forn(i, n) if (sum[i] > t) {
			index = i; break; 
		}

		vector < pair < int, int > > pairs;
		if (index != n) pairs.push_back(make_pair((int)(sum[index] - t), 1));
		for (int j = index + 1, k = 0; j < n && k < c; j++, k++) {
			cnt = (n-j-1)/c + 1; 
			pairs.push_back(make_pair((int)(2*ele[j]), cnt));
		}

		if (index != n) sort(pairs.begin(), pairs.end(), UDF);

// 		forn(i, pairs.size()) {
// 			cout << pairs[i].first << ' ' << pairs[i].second << endl;
// 		} cout << endl; 
		
		save = 0LL;
		forn(i, pairs.size()) if (l) {
			if (l < pairs[i].second) {
				save += ((long long) l)*pairs[i].first;
				l = 0; 
			}
			else {
				l -= pairs[i].second;
				save += ((long long) pairs[i].second)*pairs[i].first;
			}
// 			cout << save << endl; 
		} save /= 2; 

		long long answer = sum[n-1] - save;
// 		cout << sum[n-1] << ' ' << save << endl; 
        cout << "Case #" << test+1 << ": " << answer << endl;
    }
    return 0;
}
