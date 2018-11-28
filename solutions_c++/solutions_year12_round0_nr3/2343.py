#include <stdio.h>
#include <assert.h>
#include <time.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

int P[6], D[6];

int main() {
	freopen("C.in", "r",stdin);
	freopen("C.out","w",stdout);
	int A,B,n,m,i,j,ans,nod,T,tst=0;
    set<int> Set;
	
    scanf("%d",&T);
	while(T--){
        scanf("%d %d",&A,&B);
		
        nod=0;
        for(i=A;i!=0;i/=10)++nod;
        //fprintf(stderr,"%d\n",nod);      
        for(i=10,j=0;j<nod-1;++j,i*=10) P[j]=D[nod-2-j]=i;
        //for(j=0;j<nod-1;++j)
        //  fprintf(stderr,"%d %d\n",P[j],D[j]); 

        ans=0;
        for(n=A;n<B;++n){
            Set.clear();
            for(i=0;i<nod-1;++i){
                m=(n%P[i])*D[i]+n/P[i];
                if(m>n&&m<=B){
                    //++ans;
                    Set.insert(m);
                    //fprintf(stderr,"%d, ",m);
                }
            }
            ans+=int(Set.size());
        }
		printf("Case #%d: %d\n",++tst,ans);
        //if(T>0)printf("\n");
		//fprintf(stderr,"Case #%d: %d\n",tst,ans);
	}
	return 0;
}
