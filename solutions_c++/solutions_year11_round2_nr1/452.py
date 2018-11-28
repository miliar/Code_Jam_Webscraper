/*
	RosyIsh's code!
	
*/


#include<iostream>
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#define VI vector<int>
#define PI pair<int,int>
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define fill(a,b) memset((a),(b),sizeof((a)))
typedef long long LL;
using namespace std;

#define MX 103

double p[MX], w[MX];
double wp[MX];
double owp[MX];
double oowp[MX];
double rpi[MX];
char S[MX][MX];
int n;

void doit(){

	int t,cases = 0,n=0;
	scanf("%d",&t);
	while(t-->0){
		cases++;
		scanf("%d",&n);

		for(int i=0;i<n;i++){
			scanf(" %s",S[i]);
		//	printf("--> %s\n",S[i]);
			p[i]=0;
		}
		
			
			
	
		for(int i=0;i<n;i++){
			w[i]=0; p[i]=0; rpi[i]=0; wp[i]=0; owp[i]=0; oowp[i]=0;
			for(int j=0;j<n;j++){
				if(S[i][j]=='.')continue;
				p[i]++;
				if(S[i][j]=='1')w[i]++;
			}
			wp[i] = w[i]/p[i];
			
		/*	for(int j=0;j<n;j++){
				if(j==i || S[i][j]=='.') continue;
				int px = p[i]-1, wx = w[i];
				if(S[i][j]=='1') wx--;
				wp[i][j] = (1.0*wx)/px;
			}*/
		}
		
		for(int i=0;i<n;i++){
		
			rpi[i] = 0.25*wp[i];

			double sum = 0.0,avg =0.0;

			for(int j=0;j<n;j++){
				if(S[i][j]=='.') continue;
				double px = 0, wx = 0;
				for(int k=0;k<n;k++){
					if(k==i || S[j][k]=='.')continue;
					px++;
					if(S[j][k]=='1') wx++;
				}
				sum+=(wx/px);	
			}

			avg = sum/p[i];
			owp[i] = avg;
			rpi[i] += 0.50*avg;
		}
		
		for(int i=0;i<n;i++){		
			double avg = 0.0;
			for(int j=0;j<n;j++){
				if(S[i][j]!='.'){
					avg+=owp[j];
				}
				
			}
			avg/=p[i];
			rpi[i]+=0.25*avg;
		}


		/*for(int i=0;i<n;i++){
			double avg = 0.0;
			for(int j=0;j<n;j++){
				if(j==i || S[i][j]=='.')continue;
				avg+=wp[j][i];
			}
			avg/=p[i];
			owp[i] = avg;
		}
		for(int i=0;i<n;i++){
			double avg = 0.0;
			for(int j=0;j<n;j++){
				if(j==i || S[i][j]=='.')continue;
				avg+=owp[j];
			}
			avg/=p[i];
			oowp[i] = avg;
		}
		
		
		for(int i=0;i<n;i++){
			rpi[i] = 0.25*wp[i][0] + 0.50*owp[i]+ 0.25*oowp[i];
		}*/
		
		
				
		printf("Case #%d:\n",cases);
		for(int i=0;i<n;i++){
			printf("%.10lf\n",rpi[i]);
		}
	}	

}


int main(int argc,char * argv[] ){

	if(argc>1){
		if(argv[1][0]=='s' || argv[1][0]=='S'){
			freopen("../A-small-attempt0.in","r",stdin);
			//freopen("../A-small-practice.in","r",stdin);
			freopen("../A-small-attempt0-output.out","w",stdout);
		}
		else{
			
			//freopen("../A-large-practice.in","r",stdin);
			freopen("../A-large.in","r",stdin);
			freopen("../A-large-output.out","w",stdout);
		}
	}

	doit();
	

	return 0;

}
