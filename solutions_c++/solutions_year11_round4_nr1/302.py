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
		int i,j,k;
		int x,s,r,t,n;
		scanf("%d %d %d %d %d",&x,&s,&r,&t,&n);
		vector<int> sta,end,w;
		int now=0;
		for(i=0;i<n;i++){
			int a,b,c;
			scanf("%d %d %d",&a,&b,&c);
			if(now<a){
				sta.push_back(now);
				end.push_back(a);
				w.push_back(0);
			}
			sta.push_back(a);
			end.push_back(b);
			w.push_back(c);
			now=b;
		}
		if(now<x){
			sta.push_back(now);
			end.push_back(x);
			w.push_back(0);
		}
		vector<pair<int,int> > ve;
		for(i=0;i<w.size();i++){
			ve.push_back(MP(w[i],i));
		}
		sort(ve.begin(),ve.end());
		double left=t;
		double tim=0;
		for(i=0;i<ve.size();i++){
			double len=end[ve[i].second]-sta[ve[i].second];
			double spd=s+w[ve[i].second];
			double hispd=r+w[ve[i].second];
			if(hispd*left>=len){
				double ti=len/hispd;
				left-=ti;
				tim+=ti;
			}else{
				double lenleft=len-hispd*left;
				tim+=left;
				left=0;
				double ti=lenleft/spd;
				tim+=ti;
			}
		}
		printf("Case #%d: %.10lf\n",casenum,tim);
	}
	return 0;
}
