#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<limits.h>
#include<iostream>
#include<iomanip>
#include<sstream>
#include<algorithm>
#include<functional>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<complex>
#define EPS (1e-10)
#define PI (3.141592653589793238)
#define MP make_pair
typedef long long ll;
using namespace std;

int main(void){
	int T;
	scanf("%d",&T);
	for(int casenum=1;casenum<=T;casenum++){
		int i,j,k,n;
		scanf("%d",&n);
		vector<int> oldcard(10100);
		for(i=0;i<n;i++){
			int a;
			scanf("%d",&a);
			oldcard[a]++;
		}
		int ans=0;
		for(i=1;i<=n;i++){
			vector<int> card=oldcard;
			vector<int> point(10100);
			bool ok=true;
			for(j=1;j<=10000;j++){
				if(card[j]==0)continue;
				if(card[j]>point[j]){
					int mai=card[j]-point[j];
					for(k=0;k<i;k++){
						if(card[j+k]<mai){ok=false;break;}
						card[j+k]-=mai;
					}
					if(!ok)break;
					point[j+k]+=mai;
				}
				point[j+1]+=point[j];
				card[j]=0;
			}
			if(ok){
				ans=max(ans,i);
			}
		}
		printf("Case #%d: %d\n",casenum,ans);
	}
	return 0;
}
