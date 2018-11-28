#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

class data
{
public:	
	int v,p;
};

int main(){
	int i,j,k;
	int T,C,D,t;
	int v,p;
	double lo,hi,mid;
	double f,g,h;
	data d;
	
	t = 1;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&C,&D);
		vector<data> vd;
		
		for(i=0;i<C;i++){
			scanf("%d%d",&d.p,&d.v);
			vd.push_back(d);
		}
		
		lo = 0; hi = 1e+14;
		for(j=0;j<=150;j++){
			mid = lo + (hi - lo)/2;
			
			f = -1e+8;
			bool flag = true;
			for(i=0;i<vd.size();i++){
				g = vd[i].p - mid;
				g = max(g,f + D);
				f = g + ((vd[i].v - 1)*D);
				
				if(f > (vd[i].p + mid)){
					flag = false;
					break;
				}
			}
			if(flag) hi = mid;
			else lo = mid;
		}
		
		printf("Case #%d: %.7lf\n",t,(lo+hi)/2);
		t++;
	}
	return 0;
}
