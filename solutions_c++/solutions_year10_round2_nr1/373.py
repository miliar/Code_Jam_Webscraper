/*************************************************************************
Author: aMR
Created Time: 2010/5/23 0:06:16
File Name: a.cpp
Description: 
************************************************************************/
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>
#include <queue>
using namespace std;
#define out(x) (cout<<#x<<": "<<x<<endl)
const int maxint=0x7FFFFFFF;
typedef long long lint;
template<class T>void show(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void show(T a, int r, int l){for(int i=0; i<r; ++i)show(a[i],l);cout<<endl;}

struct node {
    node() {}
    node(string s) : name(s) {}
    string name;
    vector<int> son;
}vec[100010];
int cnt;

int n, m;

void insert(string str) {
    for(int i=0; i<(int)str.size(); ++i) {
        if(str[i] == '/') {
            str[i] = ' ';
        }
    }
    stringstream input(str);
    string s;
    int p = 0;
    while(input >> s) {
        bool ok = false;
        for(int i=0; i< (int)vec[p].son.size(); ++i) {
            int v = vec[p].son[i];
            if(vec[v].name == s) {
                p = v;
                ok = true;
                break;
            }
        }
        if(ok) continue;
        vec[cnt].son.clear();
        vec[cnt].name = s;
        vec[p].son.push_back(cnt);
        p = cnt;
        ++cnt;
    }
}

int main()
{
    int z;
    scanf("%d", &z);
    for(int ca=1; ca<=z; ++ca) {
        cnt = 1;
        vec[0].son.clear();
        scanf("%d%d", &n, &m);
        string str;
        for(int i=0; i<n; ++i) {
            cin >> str;
            insert(str);
        }
        int ans = cnt;
        for(int i=0; i<m; ++i) {
            cin >> str;
            insert(str);
        }
        ans = cnt - ans;
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}

