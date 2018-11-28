
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<string>
#include<string.h>
#include<cstring>
#include<stack>
#include<queue>
#include<cassert>

using namespace std;

#define LL long long int 
#define PII pair<int,int> 
#define PB push_back
#define MP make_pair
#define INF 1000000000

double wp[200],owp[200],oowp[200];
char s[200][200];
int win[200],tot[200],test;
int main(){
	int i,n,t,j;
	scanf("%d",&t);
	for(test=1;test<=t;test++){
		memset(win,0,sizeof(win));
		memset(tot,0,sizeof(tot));

		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf(" %s",s[i]);
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(s[i][j]=='.')
					continue;
				tot[i]++;
				if(s[i][j]=='1')
					win[i]++;
			}
			wp[i]=win[i]/(double)tot[i];
		}
		double cwp;
		for(i=0;i<n;i++){
			cwp=0;
			for(j=0;j<n;j++){
				if(s[i][j]=='.')
					continue;
				if(s[i][j]=='1')
					cwp+=(win[j])/(double)(tot[j]-1);
				else
					cwp+=(win[j]-1)/(double)(tot[j]-1);
			}
			owp[i]=cwp/tot[i];
		}
		for(i=0;i<n;i++){
			cwp=0;
			for(j=0;j<n;j++){
				if(s[i][j]=='.')
					continue;
				cwp+=owp[j];	
			}
			oowp[i]=cwp/tot[i];
		}
		printf("Case #%d:\n",test);
		for(i=0;i<n;i++){
			printf("%.12lf\n",(0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]));
		}
	}
	return 0;
}
