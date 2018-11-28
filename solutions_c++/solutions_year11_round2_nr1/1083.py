#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <list>
#include <bitset>
#include <complex>
#include <list>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
int TS,N;
char matrix[110][110];
double WP[110];
double OWP[110];
double OOWP[110];
/*
 WP (Winning Percentage) is the fraction of your games that you have won.
 In the example schedule, team A has WP = 1, team B has WP = 0, team C has WP = 2/3, 
 and team D has WP = 0.5.
 OWP (Opponents' Winning Percentage) is the average WP of all your opponents, 
 after first throwing out the games they played against you.
 For example, if you throw out games played against team D, then team B has WP = 0 and 
 team C has WP = 0.5. Therefore team D has OWP = 0.5 * (0 + 0.5) = 0.25. Similarly, 
 team A has OWP = 0.5, team B has OWP = 0.5, and team C has OWP = 2/3.
 OOWP (Opponents' Opponents' Winning Percentage) is the average OWP of all your opponents. 
 OWP is exactly the number computed in the previous step.
 For example, team A has OOWP = 0.5 * (0.5 + 2/3) = 7/12. 
 */

int main(){
	cin>>TS;
	for (int testId=1; testId<=TS; ++testId) {
		cin>>N;
		getchar();
		for (int i=0; i<N; ++i) {
			for (int j=0; j<N; ++j) {
				matrix[i][j]=getchar();
			}
			getchar();
		}
		
		for (int i=0; i<N; ++i) {
			double all,win;
			all=win=0;
			for (int j=0; j<N; ++j) {
				if (matrix[i][j]=='1'){win++;all++;}
				if (matrix[i][j]=='0'){all++;}
			}
			WP[i]=win/all;
		}
		for (int i=0; i<N; ++i) {
			double opp,sum;
			opp=sum=0;
			for (int j=0; j<N; ++j) {
				if (matrix[i][j]!='.') {
					double all,win;
					all=win=0;
					for (int k=0; k<N; ++k) {
						if (k!=i){
							if (matrix[j][k]=='1'){win++;all++;}
							if (matrix[j][k]=='0'){all++;}
						}
					}
					sum+=win/all;
					opp++;
				}
			}
			OWP[i]=sum/opp;
		}
		for (int i=0; i<N; ++i) {
			double opp,sum;
			opp=sum=0;
			for (int j=0; j<N; ++j) {
				if (matrix[i][j]!='.'){
					sum+=OWP[j];
					opp++;
				}
			}
			OOWP[i]=sum/opp;
		}
		cout << "Case #"<<testId<<":"<<endl;
		for (int i=0; i<N; ++i) {
			printf("%.6lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
		}
		
	}
	return 0;
}
