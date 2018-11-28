//BISMILLAHHIRRAHMANIRRAHIM


#include <iostream>
#include <limits.h>

#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

bool pr[10010];
int q[500];

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("Csm.out","w",stdout);
	int I=1,p,qn,i,j,k,r,t,T;
	for(scanf("%d",&T);I<=T;I++) {
		scanf("%d %d",&p,&qn);
		printf("Case #%d: ",I);
		r=INT_MAX;
		for(i=0;i<qn;i++) scanf("%d",&q[i]);
		do {
			memset(pr,1,p+10);
			t=0;
			for(i=0;i<qn;i++) {
				pr[q[i]]=0;
				for(j=q[i]+1;j<=p;j++) {
					if(!pr[j]) break;
					else t++;
				}
				for(j=q[i]-1;j>0;j--) {
					if(!pr[j]) break;
					else t++;
				}
				//cout<<' '<<t<<' '<<q[i]<<'\n';
			}
			if(t<r) r=t;
			//cout<<r<<' '<<t<<'\n';
		}
		while(next_permutation(q,q+qn));
		cout<<r<<'\n';
		}
	return 0;
}
