#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
#include<cctype>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<cmath>

using namespace std;

#define fo(a,b) for(a=0;a<b;a++)
#define re return
#define co continue
#define sf scanf
#define pf printf

int inf = 1000000000;
vector<int> V;
int n;

int debug = 0;

bool ok() {
	int i;
	for(i=0;i<n;i++)
	  if( V[i] > i ) re false;
	re true;
}

int main() {
	int t, cases = 1;
	for( sf("%d", &t); t--; ) {

		char str[100][100];
		cin >> n; int i, j;
		for(i=0;i<n;i++)
		  scanf("%s", str[i]);

		V.clear();
		for(i=0;i<n;i++) {
		  int index = 0;
		  for(j=0;j<n;j++)
		    if( str[i][j] == '1' ) index = j;

		  V.push_back(index);
		}

		int res = 0;

		while( !ok() ) {
			int i;
			for(i=0;i<n;i++)
			 if( V[i] > i ) break;

			for(j=i+1;j<n;j++) {
			  if( V[j] < V[j-1] && V[j] <= j-1 ) {
			    swap(V[j], V[j-1]); break;
			  }
			}

			res++;
		}
		pf("Case #%d: %d\n", cases++, res);
	}
	return 0;
}
