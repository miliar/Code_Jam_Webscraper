#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

typedef struct{
    int end;
    long long int sum;
}NODE;


int main(){
    
    //freopen("a.in","r",stdin);
    //freopen("out.txt","w",stdout);
    
    NODE store;
    vector<NODE> vec;
    int i, j, cas, z;
    long long int man[1000];
    long long int time, limit, group, cnt, more, total, counter, tmp;
    
    scanf("%d", &cas);
    
    for( z=1; z<=cas; ++z ){
        
        scanf("%d %d %d", &time, &limit, &group);
        cnt = 0;
        for( i=0; i<group; i++ ){
            scanf("%lld", &man[i]);
            cnt += man[i];
        }
        
        if( cnt <= limit ){
            printf("Case #%d: %lld\n", z, cnt*time);
            continue;
        }
        
        vec.clear();
        cnt = 0;
        for( i=0; i<group; ++i ){
            if( (cnt+man[i]) > limit )
                break;
            else
                cnt += man[i];
        }
        
        store.sum = cnt;
        store.end = i-1;
        vec.push_back(store);
        
        counter = time-1;
        total = store.sum;
        while( counter-- ){
            j = i + group;
            cnt = 0;
            for( i; i<j; ++i ){
                if( i==group ){
                    i = 0;
                    j -= group;
                }
                if( (cnt+man[i]) > limit )
                    break;
                else
                    cnt += man[i];
            }
            
            store.sum = cnt;
            store.end = i-1;
            
            if( store.end == vec[0].end ){     //cycle detection
                if( store.sum == vec[0].sum )
                    more = 0;
                else{
                    more = store.sum - vec[0].sum;
                    total += more;
                    vec[0].sum = store.sum;
                }
                ++counter;
                break;
            }
            
            vec.push_back(store);
            total += store.sum;
        }
        
        if( counter==-1 )
            printf("Case #%d: %lld\n", z, total);
        else{
            counter = time - counter;
            tmp = time / counter;
            cnt = tmp*total - more;
            tmp = time - tmp*counter;
            for( i=0; tmp>0; ++i,--tmp )
                cnt += vec[i].sum;
            printf("Case #%d: %lld\n", z, cnt);
        }
    }
    
    return 0;
}
