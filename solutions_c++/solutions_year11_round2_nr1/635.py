#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

class data
{
public:
	int w,t;
	double wp,owp,oowp;
};

int main(){
	int T,n,t;
	int i,j,k;
	data d;
	char S[150][150];

	t = 1;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		
		for(i=0;i<n;i++)
			scanf("%s",S[i]);				
		
		vector<data> vd;	
		for(i=0;i<n;i++){
			d.w = d.t = 0;
			for(j=0;j<n;j++){
				if(S[i][j] != '.'){
					d.t++;
					if(S[i][j] == '1') d.w++;
				}
			}
			d.wp = double(d.w)/d.t;
			vd.push_back(d);
		}
		
		for(i=0;i<n;i++){
			d.owp = 0;
			for(j=0;j<n;j++){
				if(S[i][j] != '.'){
					if(S[i][j] == '0')
						d.owp += (double(vd[j].w - 1)/(vd[j].t - 1));
					else
						d.owp += (double(vd[j].w)/(vd[j].t - 1));
				}
			}
			vd[i].owp = d.owp/vd[i].t;
		}
		
		for(i=0;i<n;i++){
			vd[i].oowp = 0;
			for(j=0;j<n;j++){
				if(S[i][j] != '.')
					vd[i].oowp += vd[j].owp;
			}
			vd[i].oowp /= vd[i].t;
		}
		
		printf("Case #%d:\n",t);
		for(i=0;i<n;i++)
			printf("%.7lf\n",(0.25*vd[i].wp) + (0.50*vd[i].owp) + (0.25*vd[i].oowp));
		t++;
	}				
	return 0;
}			
	
