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
#define sz 100

int n, m;
string matrix[sz];

bool blue(int i, int j) {
	return (i < n && j < m && matrix[i][j] == '#');
}

void update(int i, int j, char ch) {
	if (i < n && j < m) matrix[i][j] = ch;
}

int main ()
{
    int nTest; gi(nTest);
    forn(test, nTest)
    {
		cin >> n >> m;
		forn(i, n) cin >> matrix[i];

		bool possible = true;
		forn(i, n) forn(j, m) if(blue(i, j)) {
			if (!blue(i, j+1)) possible = false;
			if (!blue(i+1, j)) possible = false;
			if (!blue(i+1, j+1)) possible = false;
			update(i, j, '/'); update(i+1, j+1, '/');
			update(i+1, j, '\\'); update(i, j+1, '\\');
		}

		cout << "Case #" << test+1 << ": " << endl;
		if (possible) {
			forn(i, n) cout << matrix[i] << endl; 
		} else {
			cout << "Impossible" << endl; 
		}
    }
    return 0;
}