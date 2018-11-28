/*
 * Author: WHHeV
 * Created Time:  2010/5/8 13:09:16
 * File Name: \Users\WHHeV\Desktop\c.cpp
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
using namespace std;

int r, k, n, g[1010], t, nstate, price[1010];
list<int> state[1010];
long long ans;
list<int> tmp, in;

int find() {
    int i, j;
    bool flag;
    for (i = 1; i < nstate; i++) {
        list<int>::iterator it1;
        list<int>::iterator it2;
        flag = 1;
        for (it1 = state[i].begin(), it2 = tmp.begin(); it1 != state[i].end(); it1++, it2++) {
            if (*it1 != *it2) {
                flag = 0;
                break;
            }
        }
        if (flag)
            return i;
    }
    return 0;
}

int main() {
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    int i, j, c, temp, flag, tc = 0, round, nround, ends;
    long long sum;
    scanf("%d", &t);
    while(t--) {
        scanf("%d %d %d", &r, &k, &n);
        ans = 0;
        tmp.clear();
        nstate = 1;
        for (i = 1; i <= n; i++) {
            scanf("%d", &g[i]);
            tmp.push_back(g[i]);
        }
        state[nstate] = tmp;
        flag = 0;
        for (i = 1; i <= r; i++) {
            c = k;
            in.clear();
            while(tmp.front() <= c) {
                temp = tmp.front();
                c -= temp;
                tmp.pop_front();
                in.push_back(temp);
            }
            tmp.splice(tmp.end(), in);
            /*list<int>::iterator it2;
            for (it2 = tmp.begin(); it2 != tmp.end(); it2++)
                printf("%d  ", *it2);*/
            //flag = find();
            state[++nstate] = tmp;
            price[nstate-1] = k - c;
            ans += (k - c);
            //printf("\n   %lld\n", ans);
            /*if (flag) {
                break;
            }*/
        }
        /*if (flag) {
            round = i - flag;
            nround = (r - i) / round;
            sum = 0;
            for (j = flag; j < i; j++)
                sum += price[j];
            ans += (sum * nround);
            sum = 0;
            ends = r - (i + nround * round) + flag - 1;
            for (j = flag; j <= ends; j++)
                sum += price[j];
            ans += sum;
        }*/
        tc++;
        printf("Case #%d: %lld\n", tc, ans);
    }
    return 0;
}
