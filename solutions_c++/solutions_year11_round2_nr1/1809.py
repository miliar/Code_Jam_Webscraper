#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
#include <utility>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;
const int INF=~(1<<31);
int n,sz,g,h,i,j,T,pos1,pos2,i1,i2,sh,st,mn,cnt,root,t;
double ans,d;
vector<string> a;
vector<double> owp,oowp;
vector<pair<double,int> > wp;
int main(){
        freopen("input.txt","r",stdin);
	    freopen("output.txt","w",stdout);

        cin>>T;t=0;
		while(t++<T){
			cin>>n;
			owp.assign(n,0);
			wp.assign(n,make_pair(0,0));
			oowp.assign(n,0);
			a.resize(n);
			for(i=0;i<n;i++)cin>>a[i];
			for(i=0;i<n;i++){
				for(j=0;j<n;j++)if(a[i][j]!='.')
					{wp[i].first+= a[i][j]=='1'; wp[i].second++;}
			}
			for(i=0;i<n;i++){
				g=0;
				for(j=0;j<n;j++)if(a[i][j]!='.')
				{owp[i]+=(wp[j].first-int(a[j][i]=='1'))/(wp[j].second-1);g++;}
				owp[i]/=g;
			}
			for(i=0;i<n;i++){
				g=0;
				for(j=0;j<n;j++)if(a[i][j]!='.'){oowp[i] += owp[j];g++;}
				oowp[i]/=g;
			}
			cout<<"Case #"<<t<<':'<<endl;
			for(i=0;i<n;i++){
				printf("%.9lf\n",0.25*(wp[i].first/wp[i].second)+0.5*owp[i]+0.25*oowp[i]);
			}
		}
     
return 0;
}