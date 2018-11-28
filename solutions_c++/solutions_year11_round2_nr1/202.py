#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

char m[101][101];
double wp[101],owp[101],oowp[101];
int g[101];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int Q;
	scanf("%d",&Q);
	for(int test=1;test<=Q;test++){
		int n;
		memset(wp,0,sizeof(wp));
		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));
		memset(g,0,sizeof(g));
		scanf("%d",&n);
		gets(m[0]);
		for(int i=0;i<n;i++)
			gets(m[i]);
		int i,j;
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(m[i][j]=='.')continue;
				g[i]++;
				if(m[i][j]=='1')wp[i]+=1;
			}
			wp[i]/=g[i];
		}
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(m[i][j]=='.')continue;
				double twp=0;
				for(int k=0;k<n;k++){
					if(k==i || k==j || m[j][k]=='.')continue;
					if(m[j][k]=='1')twp+=1;
				}
				twp/=g[j]-1;
				owp[i]+=twp;
			}
			owp[i]/=g[i];
		}
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(m[i][j]=='.')continue;
				oowp[i]+=owp[j];
			}
			oowp[i]/=g[i];
		}
		printf("Case #%d:\n",test);

		for(i=0;i<n;i++)printf("%.10lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}
	return 0;
}
