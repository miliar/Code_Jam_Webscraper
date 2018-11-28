/* 
 * File:   Problem_B.cpp
 * Author: Kimi
 *
 * Created on 2009年9月13日, 上午12:55
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
#define Fill(A,n) memset(A,n,sizeof(A))
#define pb push_back

using namespace std;

/*
 *
 */
int app[10];

int main() {
    int tt;
    scanf("%d",&tt);
    for (int t=0; t<tt; t++) {
        string s;
        cin >> s;
        printf("Case #%d: ",t+1);
        Fill(app,0);
        app[s[s.size()-1]-'0']=1;
        for (int i=s.size()-1; i>=0; i--) {
            if (i==0) {
                app[0]++;
                char h;
                for (int ch=1; ch<10; ch++)
                    if (app[ch]) {
                        app[ch]--;
                        h=ch+'0';
                        break;
                    }
                s=h;
                break;
            }
            app[s[i-1]-'0']++;
            if (s[i]>s[i-1]) {
                char h;
                for (int ch=s[i-1]-'0'+1; ch<10; ch++)
                    if (app[ch]) {
                        app[ch]--;
                        h=ch+'0';
                        break;
                    }
                s=s.substr(0,i-1)+h;
                break;
            }
        }
        cout << s;
        for (int i=0; i<10; i++) {
            for (int j=0; j<app[i]; j++)
                cout << i;
        }
        cout << endl;
    }
    return (EXIT_SUCCESS);
}

