#include<cstdio>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;

typedef pair<int, long long> parka;

long long R,k,N;
vector<long long> g;
vector<parka> result;
vector<int> last;


long long solve(){
    scanf("%lld %lld %lld",&R, &k, &N);
    g = vector<long long>(N);     
    for(int i=0;i<N;++i){
            scanf("%lld",&g[i]);
    }
     
    result.clear();
    int ptr=0;
    for(int i=0;i<2*N+10;++i){         
             int start_ptr = ptr;
             long long load = 0LL;
             while(load + g[ptr] <= k){
                        load += g[ptr];
                        ptr++;           
                        if(ptr == N) ptr = 0;
                        if(ptr == start_ptr) break;
             }
             result.push_back(parka(ptr, load));
    } 
    
     //for(int i=0;i<result.size();++i) printf("%d %lld\n", result[i].first, result[i].second);
    
    last = vector<int>(N,-1);
    int idx=-1, value=-1;
    for(int i=result.size()-1;i>=0;i--){
              if(last[result[i].first]==-1){
                                            last[result[i].first] = i;
              }                           
              else{                   
                   idx=i;
                   break;
              }
    }
    long long ret = 0LL;
    for(int i=0;i<=idx && R>0;++i) {            
            ret+= result[i].second;
            R--;
    }

    int lastidx = last[result[idx].first];        
    int cycle = lastidx - idx;
    long long tsum = 0LL;
    for(int i=idx+1;i<=lastidx;++i) tsum += result[i].second;
    ret += (R / cycle) * tsum;
    R = R % cycle;
    R+=idx;
    
    for(int i=idx+1; i<=R; ++i) ret += result[i].second; 
    
    return ret;
}

int main(){
 
    int t;
    scanf("%d",&t);
    for(int tcase=1;tcase<=t;++tcase){
            long long ret = solve();
            printf("Case #%d: %lld\n", tcase, ret);
    }    
}    
