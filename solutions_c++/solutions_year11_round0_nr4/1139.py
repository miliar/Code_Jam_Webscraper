//head               
#include <cstdlib>   
#include <cstring>   
#include <memory>    
#include <cstdio>    
#include <fstream>   
#include <iostream>  
#include <cmath>     
#include <string>    
#include <sstream>   
#include <stack>     
#include <queue>     
#include <vector>    
#include <set>       
#include <map>       
#include <algorithm> 
#include <deque>     
#include <list>      
                     
using namespace std; 


int main () {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int T, N, val;
    scanf("%d", &T);
    for (int nCase = 1; nCase <= T; ++nCase) {
        vector<pair<int, int> > vec;
        scanf("%d", &N);
        for (int i = 1; i <= N; ++i) {
            scanf("%d", &val);
            if (val != i) {
                vec.push_back(make_pair(val, i));
            }
        }
        printf("Case #%d: %lf\n", nCase, (double)vec.size());
    }
    return 0;
}
