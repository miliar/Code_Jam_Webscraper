#include <iostream>
#include <set>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <map>
#include <stdlib.h>
//#include <ctime>
//#include <fstream>
using namespace std;

#define INF 1000000000
#define PI acos(-1.0)
#define MP make_pair
const double EPS=1e-8;

pair<pair<int,int>,int> a[1001];

bool cmp(pair<pair<int,int>,int>a,pair<pair<int,int>,int>b){
	return a.second<b.second;
}

int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int tt;
	cin>>tt;
	for (int T=1; T<=tt; T++){
		int x,s,r,t,n;
		cin>>x>>s>>r>>t>>n;

		int S=x;

		for (int i=0; i<n; i++){
			cin>>a[i].first.first>>a[i].first.second>>a[i].second;
			S-=a[i].first.second-a[i].first.first;
		}



		sort(a,a+n,cmp);

		double tl=t;

		double res=0;
///////////////////////
		double ttt=S/(double)(r);

			if (ttt>tl){
				double l1=tl*(r);
				res+=tl;
				tl=0;

				res+=(S-l1)/(double)(s);
			}
			else{
				res+=ttt;
				tl-=ttt;
			}
//////////////////////////////////
		int p=0;
		for (int i=0; i<n; i++){

			

			int l=a[i].first.second-a[i].first.first;

			double t=l/(double)(r+a[i].second);

			if (t>tl){
				double l1=tl*(r+a[i].second);
				res+=tl;
				tl=0;

				res+=(l-l1)/(double)(s+a[i].second);
			}
			else{
				res+=t;
				tl-=t;
			}

			p=a[i].first.second;
		}



		printf("Case #%d: %.9f\n",T,res);

	}


} 