/* 
 * File:   A.cpp
 * Author: Kimi
 *
 * Created on 2009年9月27日, 上午12:18
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#include <unistd.h>
#define Fill(A,n) memset(A,n,sizeof(A))
#define pb push_back

using namespace std;

int f[50],rst,st[50],n;


/*
 *
 */

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large_t.out","w",stdout);
    int tt;
    scanf("%d",&tt);
    for (int t=0; t<tt; t++) {
        scanf("%d",&n);
        for (int i=0; i<n; i++) {
            string s;
            cin >> s;
            f[i]=0;
            for (int tp=0; tp<s.size(); tp++)
                if (s[tp]=='1') f[i]=tp;
        }
        for (int i=0; i<n; i++) st[i]=i;
        rst=0;
        for (int i=0; i<n; i++) {
            for (int j=i; j<n; j++)
                if (f[st[j]]<=i) {
                    rst+=j-i;
                    int temp=st[i];
                    for (int tp=j; tp>i; tp--) st[tp]=st[tp-1];
                    st[i]=temp;
                    break;
                }
        }
        printf("Case #%d: %d\n",t+1,rst);
    }
    return (EXIT_SUCCESS);
}
