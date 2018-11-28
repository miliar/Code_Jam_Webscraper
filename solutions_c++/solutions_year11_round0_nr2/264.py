/*
 * Author: OpenLegend
 * Created Time:  2011-5-7 14:57:02
 * File Name: b.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
int C[26][26], O[26][26];
char buf[1005];
int main() {
    freopen("b.out", "w", stdout);
    int test, cas = 0;
    scanf("%d", &test);
    while(test --){
        memset(C, -1, sizeof(C));
        memset(O, -1, sizeof(O));
        int k;
        scanf("%d", &k);
        for(int i = 0; i < k; i ++){
            scanf("%s", buf);
            C[buf[0]-'A'][buf[1]-'A'] = C[buf[1]-'A'][buf[0]-'A'] = buf[2] - 'A';
        }
        scanf("%d", &k);
        for(int i = 0; i < k; i ++){
            scanf("%s", buf);
            O[buf[0]-'A'][buf[1]-'A'] = O[buf[1]-'A'][buf[0]-'A'] = 1;
        }
        vector<int> vec;
        int n;
        scanf("%d%s", &n, buf);
        for(int i = 0; i < n; i ++){
            int x = buf[i] - 'A';
            if(vec.size() > 0 && C[x][vec.back()] != -1){
                int tmp = C[x][vec.back()];
                vec.pop_back();
                vec.push_back(tmp);
            }else{
                bool over = false;
                for(int j = 0; j < (int)vec.size(); j ++){
                    if(O[vec[j]][x] != -1){
                        over = true; break;
                    }
                }
                if(over) vec.clear();
                else vec.push_back(x);
            }
        }
        printf("Case #%d: [", ++cas);
        for(int i = 0; i < (int)vec.size(); i ++){
            if(i != 0) printf(", ");
            printf("%c", vec[i]+'A');
        }
        printf("]\n");
    }
    return 0;
}

