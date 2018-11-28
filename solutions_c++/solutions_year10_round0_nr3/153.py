//Google_C2

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;


typedef long long Type;

Type R,K,N,d[1010];
bool vis[1010];

vector<Type> v,v2,indexv;

Type ans;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    
    
    int cs=0,t;
    int i,j;
    scanf("%I64d",&t);
    while(++cs <= t){
        memset(vis,0,sizeof(vis));
        
        v.clear();
        v2.clear();
        indexv.clear();
        
        scanf("%I64d%I64d%I64d\n",&R,&K,&N);
        
        for(i=0;i<N;++i) scanf("%I64d",d+i);
        
        i=0;
        Type sum=0;
        while( true ){
            int ct = 0;
            sum = 0;
            j = i;
            while(ct<N && sum+d[j%N]<=K){
                sum += d[ j%N ];
                j++;
                ct++;
            }
            i= (j+N-1)%N;
            
            //printf("one loop , i=%d sum=%d\n",i,sum);
            
            if(vis[i]){
                j = i;
                int ii = 0;
                while( ii < indexv.size() ){
                    if( j==indexv[ii] )break;
                    ii++;
                }
                
                v2.push_back(sum);
                ii++;
                while(ii<v.size()){
                    v2.push_back( v[ii] );
                    ii++;
                }

                break;
            }
            
            vis[i]=true;
            indexv.push_back(i);
            v.push_back(sum);
            
            i = (i+1)%N;
        }
        
        //for(i=0;i<v.size();++i) printf("v[%d]=%d\n",i,v[i]);
        //for(i=0;i<v.size();++i) printf("v2[%d]=%d\n",i,v2[i]);
        
        ans =0;

        for(i=0;i<R && i<v.size();++i) ans += v[i];
        R -= v.size();

        
        //printf("ans = %d \n",ans);
        
        if(R>0){
            
            
            
            Type tms = R / v2.size();
            int left = R % v2.size();
            

            for(i=0;i<left;++i) ans += v2[i];
            
            if(tms > 0){
                Type total = 0;
                for(i=0;i<v2.size();++i) total += v2[i];
                

                
                ans += tms * total;
            }
        }
        
        printf("Case #%d: %I64d\n",cs,ans);
    }
    
    return 0;    
}
/*
123
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3


734 3 10
1 2 3 3 2 1 1 2 3 1

*/
