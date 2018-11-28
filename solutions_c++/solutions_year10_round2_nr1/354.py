/* 
 * File:   A.cc
 * Author: GongZhi
 * Problem:
 * Created on 2010年5月22日, 下午11:54
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

/*
 *
 */
map<string, int> hash;
vector<int> A[200];
string str;
string temp;
int totle;

void insert(int k) {
    cin >> str;
    str+="/";
    temp = "";
    for (int j = 0; j < str.size(); j++) {
        if (str[j] == '/') {
            if (temp == "")continue;
            if (hash.count(temp) == 0)hash[temp] = totle++;
            A[k].push_back(hash[temp]);
            //cout << temp << endl;
            temp="";
        } else temp += str[j];
    }
//    printf("A[%d]=%d %d %d %d\n",k,A[k].size(),A[k][0],A[k][1],A[0][2]);
}
int find(int k){
    int best=A[k].size();
    for(int i=0;i<k;i++){
        int t=A[k].size();
        for(int j=0;j<A[i].size();j++)
            if(t && A[i][j]==A[k][j])t--;
            else break;
        best=min(best,t);
    }
    //cout << best << endl;
    return best;
}
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out", "w", stdout);
    int kases, kase = 1;
    cin >> kases;
    while (kases--) {
        int ans = 0;
        totle = 0;
        int n, m;
        cin >> n >> m;
        for (int i = 0; i < n + m; i++)A[i].clear();
        hash.clear();
        for (int i = 0; i < n; i++) insert(i);
        for (int i = 0; i < m; i++) {
            insert(i + n);
            ans += find(i + n);
        }
        printf("Case #%d: %d\n", kase++, ans);
    }
    return 0;
}

