#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
using namespace std;
#define ll long long
#define ull unsigned long long
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define sz(X) (int)X.size()
#define clr(X) memset(X,0,sizeof(X))
#define klr(X) memset(X,-1,sizeof(X))
#define pii pair<int,int>

struct ponto{
	double p;
	int q;
};
ponto v[210];
double d;
int n;

double mod(double x){
	if(x<0)return -x;
	return x;
}

int da(double m){
	double ult = v[0].p - m;
	for(int i=0;i<n;i++){
		int j;
		if(i==0)j=1;
		else j=0;
		for(;j<v[i].q;j++){
			double p = ult + d;
			if(p>v[i].p+m)return 0;
			ult = max(p,v[i].p-m);
		}
	}
	return 1;
}

int main(){
	int casos;
	scanf("%d",&casos);
	for(int caso=1;caso<=casos;caso++){
		scanf("%d %lf",&n,&d);
		for(int i=0;i<n;i++)
			scanf("%lf %d",&v[i].p,&v[i].q);
		double l=0.0,r=1e13;
		for(int rod=0;rod<200;rod++){
			double m = 0.5*(l+r);
			if(da(m))r=m;
			else l=m;
		}
		double m = 0.5*(l+r);
		printf("Case #%d: %.12f\n",caso,m);
	}	
	return 0;
}

