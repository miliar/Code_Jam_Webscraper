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
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int P, T, N;
    scanf("%d", &T);
    for (int nCase = 1; nCase <= T; ++nCase) {
        scanf("%d", &N);
        vector<pair<int, int> > vec[2];
        char ch[2];
        int ans = 0;
        for (int i = 0; i < N; ++i) {
            scanf("%s %d", ch, &P);
            vec[ch[0]=='O'].push_back(make_pair(P, i));
        }
        int index0 = 0, index1 = 0;
        int pos0 = 1, pos1 = 1, step;
        while (index0 < vec[0].size() && index1 < vec[1].size()) {
            if (vec[0][index0].second < vec[1][index1].second) {
                step = abs(vec[0][index0].first - pos0) + 1;
                pos0 = vec[0][index0].first;
                ++index0;
                if (vec[1][index1].first > pos1) {
                    pos1 += step;
                    if (pos1 > vec[1][index1].first)
                        pos1 = vec[1][index1].first;
                }
                else {
                    pos1 -= step;
                    if (pos1 < vec[1][index1].first)
                        pos1 = vec[1][index1].first;
                }
            }
            else {
                step = abs(vec[1][index1].first - pos1) + 1;
                pos1 = vec[1][index1].first;
                ++index1;
                if (vec[0][index0].first > pos0) {
                    pos0 += step;
                    if (pos0 > vec[0][index0].first)
                        pos0 = vec[0][index0].first;
                }
                else {
                    pos0 -= step;
                    if (pos0 < vec[0][index0].first)
                        pos0 = vec[0][index0].first;
                }
            }
            ans += step;
        }
        while (index0 < vec[0].size()) {
            ans += abs(vec[0][index0].first - pos0) + 1;
            pos0 = vec[0][index0].first;
            ++index0;
        }
        while (index1 < vec[1].size()) {
            ans += abs(vec[1][index1].first - pos1) + 1;
            pos1 = vec[1][index1].first;
            ++index1;
        }
        printf("Case #%d: %d\n", nCase, ans);
    }
    return 0;
}


