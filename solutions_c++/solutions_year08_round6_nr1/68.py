#include <vector>
#include <list>
#include <map>
#include <set>
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

#define eps 1e-8
#define PI 3.14159265358979323846
#define push_back(a) pb(a)
typedef long long ll;

int ww[1001],hh[1001];
//int www[1001],hhh[1001];
bool v[1001];
int main(){
	int T,TT;
	scanf("%d",&T);
	for(TT=1;TT<=T;TT++){
		int n,m,i,j,k,l,h,w;
		char x[20];
		scanf("%d",&n);
		int minh=10000000,maxh=0,minw=10000000,maxw=0;
		l=0;
		for(i=0;i<n;i++){
			scanf("%d%d",&h,&w);
			gets(x);
			if(x[1]=='B'){
				if(h<minh) minh=h;
				if(h>maxh) maxh=h;
				if(w<minw) minw=w;
				if(w>maxw) maxw=w;
			}else{
				ww[l]=w;
				hh[l]=h;
				l++;
			}
		}
		bool ok=1;
		int wl=-1,wu=10000000,hl=-1,hu=10000000;
		int wl2=wl,wu2=wu,hl2=hl,hu2=hu;
		memset(v,0,sizeof(v));
		int ll=0;
		if(maxh==0){
			ok=0;
		}else{
			for(i=0;i<l;i++){
				if(ww[i]<=maxw && ww[i]>=minw){
					v[i]=1;
					if(hh[i]>maxh && hh[i]<hu){
						hu=hh[i];
					}else if(hh[i]<minh && hh[i]>hl){
						hl=hh[i];
					}
				}else if(hh[i]<=maxh && hh[i]>=minh){
					v[i]=1;
					if(ww[i]>maxw && ww[i]<wu){
						wu=ww[i];
					}else if(ww[i]<minw && ww[i]>wl){
						wl=ww[i];
					}
				}else{
					if(hh[i]>maxh && hh[i]<hu2){
						hu2=hh[i];
					}else if(hh[i]<minh && hh[i]>hl2){
						hl2=hh[i];
					}
					if(ww[i]>maxw && ww[i]<wu2){
						wu2=ww[i];
					}else if(ww[i]<minw && ww[i]>wl2){
						wl2=ww[i];
					}
				}
			}
			
			if(wl>wl2)
				wl2=wl;
			if(hl>hl2)
				hl2=hl;
			if(wu<wu2)
				wu2=wu;
			if(hu<hu2)
				hu2=hu;
			//wl2=wl,wu2=wu,hl2=hl,hu2=hu;

		}
		//sort(hh,hh+l);
		//sort(ww,ww+l);
		printf("Case #%d:\n",TT);
		scanf("%d",&m);
		for(i=0;i<m;i++){
			scanf("%d%d",&h,&w);
			if(!ok){//not find
				for(j=0;j<l;j++){
					if(hh[j]==h && ww[j]==w){
						printf("NOT BIRD\n");
						break;
					}
				}
				if(j==l){
					printf("UNKNOWN\n");
				}
			}else{
				if(h>=minh && h<=maxh && w>=minw && w<=maxw){
					printf("BIRD\n");
				}else if((h<=hl || h>=hu) || (w<=wl || w>=wu)){
					printf("NOT BIRD\n");
				}else{
					for(j=0;j<l;j++){
						if(!v[j]){
							if(ww[j]>maxw && hh[j]>maxh){
								if(w>=ww[j] && h>=hh[j]){
									printf("NOT BIRD\n");
									break;
								}
							}else if(ww[j]>maxw && hh[j]<minh){
								if(w>=ww[j] && h<=hh[j]){
									printf("NOT BIRD\n");
									break;
								}
							}else if(ww[j]<minw && hh[j]>maxh){
								if(w<=ww[j] && h>=hh[j]){
									printf("NOT BIRD\n");
									break;
								}
							}else{
								if(w<=ww[j] && h<=hh[j]){
									printf("NOT BIRD\n");
									break;
								}
							}
						}
					}
					if(j==l){
						printf("UNKNOWN\n");
					}
				}
			}
		}
		
		fflush(stdout);
	}
}
