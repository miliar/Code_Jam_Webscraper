#include <iostream>
#include <cstdio>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstring>
#include <string.h>
#include <cstdlib>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <utility>
#include <cctype>
#include <list>
#include <map>
#include <limits.h>
#include <signal.h>

#define FOR(i, a, b) for ( i = a; i <= b; i++ )
#define ROF(i, a, b) for ( i = a; i >= b; i-- )
#define ALL(v) (v).begin(), (v).end()
#define MAX(a, b) ((a) >= (b) ? (a) : (b))
#define MIN(a, b) ((a) <= (b) ? (a) : (b))
#define ABS(a) ((a) < (0) ? (a)*(-1) : (a))
#define SWAP(a, b) typeof(a) T; T=a; a=b; b=T;

using namespace std;
//using namespace __gnu_cxx;

double WP[110];
double OWP[110];
double OOWP[110];
int Lost[110];
int Win[110];

int main()
{
	int test;
	scanf("%d",&test);
	int Test = 0;
	int i , j;
	char val;
	int n;
	double sum;
	int match , win , lost;
	while(test--) {
		string str[110];
		scanf("%d",&n);

		FOR(i,0,n-1) {
			cin >> str[i];
		}
		memset(WP,0.0,sizeof(WP));
		memset(OWP,0.0,sizeof(OWP));
		memset(OOWP,0.0,sizeof(OOWP));
		memset(Lost,0,sizeof(Lost));
		memset(Win,0,sizeof(Win));	
		FOR(i,0,n-1) {
			match = 0;
			win = 0;
			lost = 0;
			FOR(j,0,n-1) {
				val = str[i][j];
				if(val != '.') {
					match++;
					if(val == '0')  {
						lost++;
						Lost[i]++;
					}
					else {
						win++;
						Win[i]++;
					}
				}
			}
			//cout << Lost[i] << " " << Win[i] << endl;
			WP[i] = (float)((float)win/(float)match);
			
		}

		FOR(i,0,n-1) {
			match = 0;
			sum = 0;
			FOR(j,0,n-1) {
				val = str[i][j];
				//cout << val;
				if(val != '.') {
					match++;
				
				
				if(val == '1') {
					if(Lost[j]) {
					lost = Lost[j]-1;
					}
					else {
					lost = 0;
					}
					
					win = Win[j];
					
					//match++;
				}
				if(val == '0') {
					if(Win[j]) {
					win = Win[j]-1;
					}
					else {
					win = 0;
					}
					lost = Lost[j];
				
					//match++;
				}
				//cout << "win lost  " << win << " " << lost << endl;
				sum += (float)win/(float)(win+lost);
				}
			}
			//cout << endl;
			//cout << sum  << " " << match << endl;
			OWP[i] = (float)sum/(float)match;
			//cout << OWP[i] << endl;
		}

		FOR(i,0,n-1) {
			sum = 0;
			match = 0;
			FOR(j,0,n-1) {
				val = str[i][j];
				
				if(val != '.') {
					sum += OWP[j];
					match++;
				}
				
			}
			OOWP[i] = (float)sum/(float)match;
		}
		Test++;
		printf("Case #%d:\n",Test);
		double RPI;		
		FOR(i,0,n-1) {
			RPI = 0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i];
			printf("%.8lf\n",RPI);
		}
	}
	return 0;
}
