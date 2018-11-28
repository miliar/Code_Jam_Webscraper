#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
using namespace std;
#define ll long long
#define MAX_NODES 10001
#define LEFT(i) (((i) << 1) + 1)
#define RIGHT(i) (((i) << 1) + 2)

bool val[MAX_NODES];
pair<bool, bool> props[MAX_NODES];
int changes[MAX_NODES];
int M;

void count_root(){
    for(int i = (M - 1)/2 - 1; i >= 0; --i){
        if(props[i].first) val[i] = val[LEFT(i)] && val[RIGHT(i)];
        else val[i] = val[LEFT(i)] || val[RIGHT(i)];
    }
}

int count_min_changes(int i, bool expected_val){
    if(val[i] == expected_val) return 0;
    else if(i >= (M - 1)/2) return -1;
    int l = count_min_changes(LEFT(i), expected_val),
        r = count_min_changes(RIGHT(i), expected_val);
    //printf("l(%d) = %d; r(%d) = %d\n", LEFT(i) + 1, l, RIGHT(i) + 1, r);
    if(expected_val){
        if(props[i].first){ // AND
            if(! props[i].second){
                if(l == -1 || r == -1) return -1;
                return l + r;
            }
            else {
                if(l == -1){
                    if(r == -1) return -1;
                    return r + 1;
                }
                else {
                    if(r == -1) return l + 1;
                    return min(l, r) + 1;
                }
            }
        }
        else{ // OR
                if(l == -1){
                    if(r == -1) return -1;
                    return r;
                }
                else {
                    if(r == -1) return l;
                    return min(l, r);
                }
        }
    }
    else {
        if(props[i].first){ // AND
                if(l == -1){
                    if(r == -1) return -1;
                    return r;
                }
                else {
                    if(r == -1) return l;
                    return min(l, r);
                }
        }
        else{ // OR
            if(! props[i].second){
                if(l == -1 || r == -1) return -1;
                return l + r;
            }
            else{
                if(l == -1){
                    if(r == -1) return -1;
                    return r + 1;
                }
                else {
                    if(r == -1) return l + 1;
                    return min(l, r) + 1;
                }
            }
        }    
    }
    return -1;
}

int main(){
    int TC;
    scanf("%d", &TC);
    for(int tc = 1; tc <= TC; ++tc){
        int V;
        scanf("%d %d", &M, &V);
        for(int i = 0; i < (M - 1)/2; ++i){
            scanf("%d %d", &props[i].first, &props[i].second);
            changes[i] = 0;
        }
        for(int i = (M - 1)/2; i < M; ++i){
            scanf("%d", &val[i]);
            changes[i] = 0;
        }
        
        count_root();
        //for(int i = 0; i < M; ++i)
        //    printf("%d ", val[i]);
        //printf("\n");
        int result = count_min_changes(0, V);
        if(result == -1)
            printf("Case #%d: IMPOSSIBLE\n", tc);
        else
            printf("Case #%d: %d\n", tc, result);
    }
    return 0;
}
