// test.cpp : Defines the entry point for the console application.
//
//
#include "stdafx.h"

#include "iostream"
#include "math.h"
#include "string"

#include <algorithm> 
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <climits>

using namespace std;

short casenum;
short caseindex;

int p,k,l;
int presstimes[1001];


int cmp( const void *a , const void *b ) 
{ 
	int *c = (int *)a; 

	int *d = (int *)b; 

	return *d - *c; 
} 

void doing()
{
	int i;
	int j;
	qsort(presstimes, l, sizeof(int), cmp);

	long long int ans = 0;
	i=0;
	j=0;

	while (i<l) {
		if (i % k == 0) {
			++j;
			if (j>p) {
				cout << "Case #" << caseindex << ": ";
				cout << "Impossible" << endl;
			}
		}
		ans += presstimes[i]*j;
		++i;
	}


	cout << "Case #" << caseindex << ": ";
	cout << ans;
	cout << endl;
}


int main()
{
	int i;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	while (cin>>casenum) {
		for (caseindex = 1; caseindex <= casenum; ++caseindex) {
			cin >>p >> k >> l;

			for (i =0; i< l; ++i) {
				cin >> presstimes[i];
			}
			doing();
		}
	}

	return 0;
}
