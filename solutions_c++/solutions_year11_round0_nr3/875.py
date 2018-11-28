/* {{{ */
#include<cstdio>
#include<climits>
#include<cmath>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<map>
#include<list>
#include<sstream>
#include<set>
#include<queue>
#include<vector>
#include<string>
#include<fstream>
#include<istream>
#include<iostream>
#include<bitset>
using namespace std;
/* }}}  */

typedef long long ll;
typedef unsigned long long ull;
const int MAX=21;
int arr[1<<MAX],sum[1<<MAX],osum[1<<MAX];
int v[2000];

int main(int argc,char **argv){
       
    int tc,no;
    scanf(" %d",&no);
    for(tc=1;tc<=no;tc++) {
            printf("Case #%d: ",tc);
            int n,i;
            scanf(" %d",&n);
            int tot=0;
            for(i=0;i<n;i++) {
                    scanf(" %d",&v[i]);
                    tot ^=v[i];
            }
            if(tot!=0) {
                printf("NO\n");
                continue;
            }
            sort(v,v+n);
            memset(arr,0,sizeof(arr));
            sum[0]=sum[1]=sum[2]=0;
            int j;
            int curmax=0;
            for(i=0;i<n;i++) {
                  int curstep=i+1;
                  memcpy(osum,sum,sizeof(int)*(curmax+1));
                  memset(sum,0,sizeof(int)*(curmax+1));
                  for(j=curmax;j>=0;j--){
                        if(((arr[j]>0) and (arr[j]<curstep)) || (j==0))
                        {
                            int idx=j^v[i];
                            curmax=max(curmax,idx);
                            if((arr[idx]>0) and (arr[idx]<curstep)){
                                 if((osum[j]+v[i])>sum[idx]) sum[idx]=osum[j]+v[i];

                                }
                            

                            if(arr[idx]==0)
                            {
                              arr[idx]=curstep;
                              sum[idx]=osum[j]+v[i];
                            }
                        }
                  }
            }
    
        int ans=-1;

              for(j=curmax;j>0;j--){
                        if(arr[j] and ((j^tot)==j)) {
                            ans=max(ans,sum[j]);
                        }
                  }
                  if(ans==-1) printf("NO\n");
                  else printf("%d\n",ans);
    }


    return 0;
}


