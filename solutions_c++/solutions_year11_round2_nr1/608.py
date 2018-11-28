#include <list>
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <sstream>
#include "ttmath/ttmath.h"

using namespace std;

typedef unsigned long long int u64;
typedef long long int i64;

typedef ttmath::Big<5,5> MyBig;

char games[110][110];

MyBig tot[110];
MyBig win[110]; 
MyBig WP[110][110];
MyBig OWP[110];
MyBig OOWP[110];
MyBig res[110];

int main() {
	int NC;

	cin >> NC;
	
	for(int cs=1;cs<=NC;cs++) {
		int N;
		cin >> N;
		for(int i=0;i<N;i++) {
			tot[i]=0;
			win[i]=0;
			for(int j=0;j<N;j++) {
				cin >> games[i][j];
				if(games[i][j]=='.')
					continue;
				tot[i]++;
				if(games[i][j]=='1')
					win[i]++;
			}
		}
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				switch(games[i][j]) {
					case '.': WP[i][j]=win[i]/tot[i]; break;
					case '1': WP[i][j]=(win[i]-1)/(tot[i]-1); break;
					case '0': WP[i][j]=win[i]/(tot[i]-1); break;
				}
			}
			WP[i][N]=win[i]/tot[i];
		}
		
		for(int i=0;i<N;i++) {
			OWP[i]=0;
			for(int j=0;j<N;j++) {
				if(games[i][j]!='.')
					OWP[i]+=WP[j][i];
			}
			OWP[i]/=tot[i];
		}
		
		for(int i=0;i<N;i++) {
			OOWP[i]=0;
			for(int j=0;j<N;j++) {
				if(games[i][j]!='.')
					OOWP[i]+=OWP[j];
			}
			OOWP[i]/=tot[i];
		}
			
		cout << "Case #" << cs << ": " <<  endl;
		
		MyBig z25=0.25,z5=0.5;
		for(int i=0;i<N;i++) {
			
			res[i] = z25*WP[i][N]+z5*OWP[i]+z25*OOWP[i];
			cout << res[i] << endl;
		}
		
	}
	
	return 0;
}