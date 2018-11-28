#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
#define mx 110
#define eps 1e-9
vector < int > W[mx];
vector < int > L[mx];
int wn[mx],ln[mx];
double wp[mx],owp[mx],oowp[mx],up,rpi;
char line[mx][mx];
int main(){
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int t,cas,i,n,opp,j;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			W[i].clear();
			L[i].clear();
			wn[i] = ln[i] = wp[i] = owp[i] = oowp[i] = 0;
		}
		for(i=0;i<n;i++){
			scanf("%s",line[i]);
			for(j=0;line[i][j];j++){
				if(line[i][j]=='1'){W[i].push_back(j);wn[i]++;}
				else if(line[i][j]=='0'){L[i].push_back(j);ln[i]++;}
			}
		}
		for(i=0;i<n;i++){
			wp[i] = (double)wn[i]/(double)(wn[i]+ln[i]);
			up = 0;
			for(j=0;j<wn[i];j++){
				opp = W[i][j];
				up += (double)wn[opp]/(double)(wn[opp]+ln[opp]-1);
			}
			for(j=0;j<ln[i];j++){
				opp = L[i][j];
				up += (double)(wn[opp]-1)/(double)(wn[opp]+ln[opp]-1);
			}
			owp[i] = up/(double)(wn[i]+ln[i]);
		}
		for(i=0;i<n;i++){
			up = 0;
			for(j=0;j<wn[i];j++){
				opp = W[i][j];
				up += owp[opp];
			}
			for(j=0;j<ln[i];j++){
				opp = L[i][j];
				up += owp[opp];
			}
			oowp[i] = up/(double)(wn[i]+ln[i]);
		}
		printf("Case #%d:\n",cas);
		for(i=0;i<n;i++){
			rpi = ( (0.25 * wp[i]) + (0.50 * owp[i]) + (0.25 * oowp[i]) );
			printf("%.7lf\n",rpi+eps);
		}
	}
	return 0;
}