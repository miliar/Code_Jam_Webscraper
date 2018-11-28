//Author: Fluorine
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

vector <pair <int,int> > a;
int tot,x,y,n,m;
char str[100];

int main(){
	scanf("%d",&tot);
	for (int cases=0;cases<tot;++cases){
		a.clear();
		int maxl=1000000,maxd=1000000;
		int maxr=-100,maxu=-100;
		scanf("%d",&n);
		for (int i=0;i<n;++i){
			scanf("%d%d%s",&x,&y,&str);
			if (str[0]=='B'){
				if (x<maxl) maxl=x;
				if (x>maxr) maxr=x;
				if (y<maxd) maxd=y;
				if (y>maxu) maxu=y;
			}
			else{
				a.push_back(make_pair(x,y));
				scanf("%s",&str);
			}
		}
		printf("Case #%d:\n",cases+1);
		scanf("%d",&m);
		for (int i=0;i<m;++i){
			scanf("%d%d",&x,&y);
			if ((x>=maxl)&&(x<=maxr)&&(y>=maxd)&&(y<=maxu)){
				printf("BIRD\n");
				continue;
			}
			int l=maxl,r=maxr,u=maxu,d=maxd;
			if (x<l) l=x;
			if (x>r) r=x;
			if (y<d) d=y;
			if (y>u) u=y;
			bool t=true;
			for (int i=0;i<a.size();++i){
				if ((a[i].first>=l)&&(a[i].first<=r)&&(a[i].second>=d)&&(a[i].second<=u)){
					t=false;
					break;
				}
			}
			if (t) printf("UNKNOWN\n");
			else printf("NOT BIRD\n");
		}
	}
	return 0;
}
