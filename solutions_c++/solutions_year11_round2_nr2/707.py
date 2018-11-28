#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<algorithm>
#include<memory.h>
#include<iomanip>
#include<cmath>
#include<fstream>
#include<map>
#include<ctime>
#include<queue>
#include<set>
#include<vector>
using namespace std;

const int MAXN = 205;

int n, d;
struct A {
	int p, v;
	bool friend operator <(const A & x,const A & y){
		return x.p<y.p;
	}
}g[MAXN];

bool find(double m)
{
	double l=g[0].p-m+d*(g[0].v-1);
	if(l-g[0].p>m) return false;
	int i=1;
	while(i<n){
		if(g[i].p-m-l>=d){
			if(-m+d*(g[i].v-1)<= m){
				l=g[i].p-m+d*(g[i].v-1);
			}else{
				return false;
			}
		}else{
			if(l+d-g[i].p>m) return 0;
			if(l+d+d*(g[i].v-1)-g[i].p<=m){
				l=l+d+d*(g[i].v-1);
			}else{
				return false;
			}
		}
		i++;
	}
	return true;
}

int main() 
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int cas=1;
	while(cas<=t){
		cin>>n>>d;
		for(int i=0;i<n;i++){
			cin>>g[i].p>>g[i].v;
		}
		sort(g,g+n);
		double l=0,r=1e12;
		while(fabs(r-l)>1e-6){
			double m=(l+r)/2;
			if(find(m)){
				r=m;
			}else{
				l=m;
			}
		}
		cout<<"Case #"<<cas<<": "<<l<<endl;
		cas++;
	}
}
