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
#include <bitset>
#include <set>
#include <map>
using namespace std;

int main() {
	freopen("C.in", "r",stdin);
	freopen("C.out","w",stdout);
	int x,T,tst=0;
	
  scanf("%d",&T);
	while(T--){
    vector<int> s(20);
    int sum=0; 
    scanf("%d",&x);
    for(int i=0;i<20;++i){
      scanf("%d",&s[i]);
		  sum+=s[i];
    }
    
    bool done=false;
    vector< vector<int> > V(2000001); 
    for(int mask=0; mask<(1<<20); ++mask){
      
      int tmp=0;
      vector<int> Z, Q;
      for(int i=0; i<20; ++i) {
        if(mask & (1<<i)) {
          tmp += s[i];
          Z.push_back(s[i]);
        } else Q.push_back(s[i]);
      }

      if(V[tmp].size()>0) {
        done=true;
        printf("Case #%d:\n",++tst);
		    for(int j=0;j<V[tmp].size();++j)printf("%d ",V[tmp][j]);
        
        printf("\n");
		    for(int j=0;j<Z.size();++j)printf("%d ",Z[j]);
        printf("\n");
        break;
      }
      if(sum-tmp == tmp){
        done=true;
        printf("Case #%d:\n",++tst);
		    for(int j=0;j<Q.size();++j)printf("%d ",Q[j]);
        printf("\n");
		    for(int j=0;j<Z.size();++j)printf("%d ",Z[j]);
        printf("\n");
        break;
      }
      if(tmp==20)
		    fprintf(stderr,"%d\n",mask);
      V[tmp] = Z; V[sum-tmp] = Q;    
    }
    
    if(done)continue;
		printf("Case #%d:\nImpossible\n",++tst);
    //if(T>0)printf("\n");
		//fprintf(stderr,"Case #%d: %d\n",tst,ans);
	}
	return 0;
}
