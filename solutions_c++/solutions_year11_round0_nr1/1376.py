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
#define gi(t) scanf("%d ",&(t))
#define gch(ch) scanf("%c",&(ch))
#define sz 101

int main ()
{
    int nTest; gi(nTest);
	int pos[sz]; 
	char rob[sz];
    forn(test, nTest)
    {
		// input
		int n; gi(n); 
// 		cout << n << endl; 
		forn(i, n) {
			scanf("%c %d ", &(rob[i]), &(pos[i])); 
// 			cout << rob[i] << ' ' << pos[i] << endl; 
		}
		
		// process
		int opos = 1, bpos = 1, btime = 0, otime = 0; 
		forn(i, n) {
			if (rob[i] == 'O') {
				otime += abs(opos - pos[i]); 
				opos = pos[i];
				otime = max(otime, btime) + 1;
			}
			else {
				btime += abs(bpos - pos[i]); 
				bpos = pos[i];
				btime = max(otime, btime) + 1;
			}
// 			cout << i << ' ' << otime << ' ' << btime << endl; 
		}
		
		// output
        cout << "Case #" << test+1 << ": " << max(otime, btime) << endl; 
    }
    return 0;
}