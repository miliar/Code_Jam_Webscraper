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

int main(){
	int t;
	cin >> t;
	string team[110];
	for(int tc=0;tc<t;tc++){
		int n;
		double wp[110], owp[110], oowp[110], p[110], num[110];
		cin >> n;
		for(int i=0;i<n;i++){
			cin >> team[i];
			wp[i]=owp[i]=oowp[i]=p[i]=num[i]=0.;
		}
		for(int i=0;i<n;i++){
			double win=0.;
			for(int j=0;j<n;j++){
				if(team[i][j]=='1'){
					num[i]+=1.0;
					win+=1.0;
				}
				else if(team[i][j]=='0')num[i]+=1.0;
			}
			if(num[i]>0.0)wp[i]=win/num[i];
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(team[i][j]!='.'){
					double cnt=0.0, wwin=0.;
					for(int k=0;k<n;k++){
						if(k==i)continue;
						if(team[j][k]=='1'){
							cnt+=1.0;
							wwin+=1.0;
						}
						else if(team[j][k]=='0')cnt+=1.0;						
					}
					if(cnt!=0)owp[i]+=wwin/cnt;
				}
			}
			if(num[i]>0.0)owp[i]=owp[i]/num[i];
		}	
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				if(team[i][j]!='.')oowp[i]+=owp[j]/num[i];			
		
		printf("Case #%d:\n",tc+1);
		for(int i=0;i<n;i++)printf("%.8lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);		
	}
	return 0;
}
