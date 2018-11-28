#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<ctime>
#include<cassert>
using namespace std;
#define y1 fndjifhwdn
#define ws vfsdkofsjd
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pi;
int n,tt,d;
ld l,r,m,yk;
bool can;
int p[1000];
int v[1000];
const ld eps=1e-9;
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	scanf("%d",&tt);
	for (int ti=0;ti<tt;ti++){
		scanf("%d%d",&n,&d);
		for (int i=0;i<n;i++){
			scanf("%d%d",&p[i],&v[i]);
		}
		l=0;
		r=1e12;
		for (int it=0;it<=200;it++){
			m=(l+r)/2;
			can=true;
			yk=p[0]-m;
			for (int i=0;i<n;i++){
				for (int j=0;j<v[i];j++){
					yk=max(yk,p[i]-m);
					if (yk<=p[i]+m+eps){
						yk+=d;
					} else {
						can=false;
						break;
					}
				}
				if (!can) break;
			}
			if (can) r=m; else l=m;
		}
		printf("Case #%d: %.18lf\n",ti+1,(double)r);
	}
    return 0;
}









