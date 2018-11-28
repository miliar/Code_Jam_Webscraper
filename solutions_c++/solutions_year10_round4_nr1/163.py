/**********************************************************************
Author: hanshuai
Created Time:  2010/6/5 22:11:21
File Name: a.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;
const int maxn = 205;
int k;
bool vis1[maxn], vis2[maxn];
bool equal(int t1, int t2){
    if(t1 == -1 || t2 == -1) return true;
    return t1 == t2;
}
void cal(vector<vector<int> > v2, bool vis[]){
    for(int i = 0; i < 2*k-1; i ++){
        for(int j = 0; j < 2*k-1; j ++){
            if(vis[i]) break;
            for(int l = 0; ; l ++){
                int t1 = i - l, t2 = i + l;
                if(t1 < 0 || t2 >= 2*k-1) break;
                t1 = v2[j][t1], t2 = v2[j][t2];
                if(!equal(t1, t2)){
                    vis[i] = true; break;
                }
            }
        }
    }
//    for(int i = 0; i < 2*k-1; i ++){
//        printf("i = %d, vis = %d\n", i, vis[i]);
//    }
}
bool can1[maxn], can2[maxn];
void solve(bool t1[], bool t2[]){
    for(int i = 0; i < 2*k-1; i ++){
        if(!t1[i]){
            int v = abs(k-1-i);
            int len = k + v;
            t2[len] = true;
        }
    }
}
int main() {
    freopen("a.out", "w", stdout);
    int test, cas = 0;
    scanf("%d", &test);
    while(test --){
        scanf("%d", &k);
        memset(vis1, false, sizeof(vis1));
        memset(vis2, false, sizeof(vis2));
        memset(can1, false, sizeof(can1));
        memset(can2, false, sizeof(can2));
        vector<vector<int> > vec;
        vec.push_back(vector<int>());
        for(int i = 1; i < 2*k; i ++){
            vector<int> tmp;
            int len = i, t;
            if(i > k) len = 2*k-i;
            for(int j = 0; j < len; j ++){
                scanf("%d", &t);
                tmp.push_back(t);
            }
            vec.push_back(tmp);
        }
        vector<vector<int> > v2;
        for(int i = 1; i < 2*k; i ++){
            vector<int> tmp;
            int len = i;
            if(i > k) len = 2*k-i;
            int l1 = k-len;
            for(int j = 0; j < l1; j ++) tmp.push_back(-1);
            tmp.push_back(vec[i][0]);
            for(int j = 1; j < (int)vec[i].size(); j ++){
                tmp.push_back(-1);
                tmp.push_back(vec[i][j]);
            }
            for(int j = 0; j < l1; j ++) tmp.push_back(-1);
            v2.push_back(tmp);
//                        for(int i = 0; i < (int)tmp.size(); i ++){
//                            printf("%3d", tmp[i]);
//                        }
//                        printf("\n");
        }
        cal(v2, vis1);
//        printf("\n");
        vector<vector<int> > v3;
        for(int i = 0; i < 2*k - 1; i ++){
            vector<int> tmp;
            for(int j = 0; j < 2*k-1; j ++){
                tmp.push_back(v2[j][i]);
            }
            v3.push_back(tmp);
//            for(int i = 0; i < (int)tmp.size(); i ++){
//                printf("%3d", tmp[i]);
//            }
//            printf("\n");
        }
        cal(v3, vis2);
        vector<pair<int,int> > vp;
        for(int i = 0; i < 2*k-1; i ++){
            int len = i + 1;
            if(len > k) len = 2*k - len;
            len --;
            vp.push_back(make_pair(i, k-1-len));
            vp.push_back(make_pair(i, k-1+len));
        }
        int ans = maxn*maxn;
        for(int i = 0; i < 2*k-1; i ++){
            for(int j = 0; j < 2*k-1; j ++){
                if(!vis1[i] && !vis2[j]){
                    int tmp = 0;
                    for(int l = 0; l < (int)vp.size(); l ++){
                        tmp = max(tmp, abs(vp[l].first-i)+abs(vp[l].second-j));
                    }
                    ans = min(ans, tmp+1);
                }
            }
        }
//        solve(vis1, can1);
//        solve(vis2, can2);

        printf("Case #%d: %d\n", ++cas, ans*ans-k*k);
        //        int ans1 = k*k;
//        for(int i = k; ; i ++){
//            if(can1[i]) can1[i+2] = true;
//            if(can2[i]) can2[i+2] = true;
//            if(can1[i] && can2[i]){
//                //                printf("%d\n", i);
//                printf("%d\n", i*i-k*k);
//                break;
//            }
//        }
    }
    return 0;
}

