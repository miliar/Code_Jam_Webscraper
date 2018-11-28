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


const int MAX=1000;
ull arr[MAX],csum[2*MAX];
int next[MAX];
int visit[MAX],M[MAX],C[MAX];

int R,K,N;

ull getsum(int x,int y){
    if(x==0) if(y>=0) return csum[y]; else return csum[y+N];
    if(x<=y) return csum[y] - csum[x-1];
    else return csum[y+N] - csum[x-1];

}

ull calc(int x,int y){
    return getsum(x,y-1);
}

int main(int argc,char **argv){
      int no,i,tc=0;
      scanf(" %d",&no);
      while(no--){
            tc++;
            scanf(" %d %d %d",&R,&K,&N);

            memset(arr,0,sizeof(arr));
            memset(csum,0,sizeof(csum));
            memset(next,-1,sizeof(next));
            memset(visit,0,sizeof(visit));
            memset(M,0,sizeof(M));
            memset(C,0,sizeof(C));

            for(i=0;i<N;i++) scanf(" %llu",&arr[i]);
            csum[0]=arr[0];

            for(i=1;i<2*N;i++) csum[i]=csum[i-1] + arr[i%N];

            if(csum[N-1]<=K) { printf("Case #%d: %llu\n",tc,R*csum[N-1]); continue;}

            for(i=0;i<N;i++){
                    int z=0;
                    if(i > 0) z=csum[i-1];
                    int idx=distance(csum,upper_bound(csum+i,csum+2*N,K+z));
                    next[i]=idx%N;
            }

   //         for(i=0;i<N;i++) printf("%d,",next[i]); printf("\n");
    //        printf("%llu\n",calc(0,0));

            
            int rem=R,prev=-1;
            ull ans=0,prevcost=0,loopcost=0;
    
            int x=0,it=0;
            while(visit[x]<=1){
                M[x]=it++;
                visit[x]++;
                prev=x;
                x=next[x];
                ans+=calc(prev,x);
  //              printf("%llu:%llu  ,",ans,calc(prev,x));
                rem--;
                if(!rem) break;

                if(visit[x]>1) loopcost=ans - C[x];
                else C[x]=ans;
            }
           
            int li=x,llen=it-M[x];
            int  times=rem/llen,left=rem%llen;
            if(rem==0) goto gg;
//            printf("%d,%d,%llu,%d\n",li,llen,loopcost,rem);
            ans+=times*loopcost;
            while(left--){
                prev=x;
                x=next[x];
                ans+=calc(prev,x);
            }
            gg:
            printf("Case #%d: %llu\n",tc,ans);

       }
    return 0;
}
