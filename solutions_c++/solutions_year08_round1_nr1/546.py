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

int n;
int lista[800];
int listb[800];

int cmp( const void *a , const void *b ) 
{ 
	int *c = (int *)a; 

	int *d = (int *)b; 

	return *c - *d; 
} 

int cmpd( const void *a , const void *b ) 
{ 
	int *c = (int *)a; 

	int *d = (int *)b; 

	return *d - *c; 
} 

void doing()
{
	int i;

	qsort(lista, n, sizeof(int), cmp);
	qsort(listb, n, sizeof(int), cmpd);

	long long int ans = 0;
	long long int temp;

	for (i=0; i<n; ++i) {
		temp = (long long int)(lista[i]) * (long long int)(listb[i]);
		ans += temp;
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
			cin >> n;
			
			for (i=0; i<n; ++i) {
				cin >> lista[i];
			}
			for (i=0; i<n; ++i) {
				cin >> listb[i];
			}

			doing();
		}
	}

	return 0;
}
