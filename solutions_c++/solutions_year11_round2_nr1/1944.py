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
#include <cstdio>
#include <cstring>
#include <iostream>
double w[110],t[110],wp[110],owp[110],oowp[110],rpi[110],sum;
int T,n;
char a[110][110];
using namespace std;
int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n",&T); 
	for(int test=1;test<=T;test++){
		scanf("%d ",&n);
		for(int i=1;i<=n;i++){
			w[i]=t[i]=0;
			for(int j=1;j<=n;j++){
				scanf("%c",&a[i][j]);
				if(a[i][j]=='.') continue;
				if(a[i][j]=='1') w[i]++;
				t[i]++;
			}
			scanf("\n");
		}
		for(int i=1;i<=n;i++){ 
			wp[i]=0; 
			if(!t[i]) continue;
			wp[i]=w[i]/t[i];
		}
		for(int i=1;i<=n;i++){ 
			sum=owp[i]=0;
			if(!t[i]) continue;
		        for(int j=1;j<=n;j++)
				if(a[i][j]!='.'){
				   if(t[j]<=1) continue;
				   if(a[j][i]=='1') sum+=(w[j]-1)/(t[j]-1);
				   else sum+=w[j]/(t[j]-1);
				} 
			owp[i]=sum/t[i];
		}
		
		for(int i=1;i<=n;i++){ 
			sum=oowp[i]=0;
			if(!t[i]) continue;
		        for(int j=1;j<=n;j++)
				if(a[i][j]!='.') sum+=owp[j];
			oowp[i]=sum/t[i];
		}
                
		for(int i=1;i<=n;i++) 
			rpi[i]=(wp[i]+oowp[i])/4.0+(owp[i]/2.0);
		
		printf("Case #%d:\n",test);
		for(int i=1;i<=n;i++)
			printf("%.7lf\n",rpi[i]);
	}
}
