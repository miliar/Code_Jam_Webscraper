#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <cmath>
#include <list>
#include <cstdlib>
#include <deque>
#include <stack>
#include <utility>
using namespace std;
#define mp make_pair
typedef long long ll;


char g[110][110];
double wp[110];
double cont[110];
double owp[110];
double oowp[110];
double rpi[110];


int main(){
	freopen("out.txt","w",stdout);
	int casos, n;
	scanf("%d",&casos);
	for(int u=1; u<=casos; u++){
		scanf("%d",&n);
		for(int i=0; i<n; i++)
			scanf("%s",g[i]);
		
		double val;
		for(int i=0; i<n; i++){
			cont[i] = 0.0;
			wp[i] = 0.0;
			for(int j=0; j<n; j++){			
				if(g[i][j] == '1'){
					cont[i] = cont[i] + 1.0;
					wp[i] = wp[i] + 1.0;					
				}else if(g[i][j] == '0')
					cont[i] = cont[i] + 1.0;
			}
		}
		
		for(int i=0; i<n; i++){
			owp[i] = 0.0;
			val = 0.0;
			for(int j=0; j<n; j++){
				if(g[i][j] != '.'){
					if(g[i][j] == '1')
						owp[i] += (wp[j])/(cont[j]-1.0);
					else
						owp[i] += (wp[j]-1.0)/(cont[j]-1.0);			
				}
			}
			owp[i]/= cont[i];
		}
		
		for(int i=0; i<n; i++){
			oowp[i] = 0.0;
			val = 0.0;
			for(int j=0; j<n; j++){
				if(g[i][j] != '.'){
					val = val + owp[j];					
				}
			}
			oowp[i] = val/cont[i];
			wp[i] /= cont[i];
		}
		printf("Case #%d:\n",u);
		for(int i=0; i<n; i++){
			printf("%.10lf\n",(0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]));
		}

	}
}

