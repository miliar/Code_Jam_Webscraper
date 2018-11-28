/* 
 * File:   The Next Number.cpp
 * Author: Administrator
 *
 * Created on 2009年9月13日, 上午12:09
 */

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <iostream>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <string>
#include <complex>
#include <functional>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <fstream>
using namespace std;

int main() {
    int t;
    string ss, ans;
            freopen("E:/B-small-attempt1.in", "r", stdin);
           freopen("E:/B-small-attempt1.out", "w", stdout);
    while (scanf("%d", &t) != EOF) {
        for (int k = 1; k <= t; k++) {
            cin >> ss;
            int label = 0;
            int x;
            for (int i = ss.size() - 1; i >= 0; i--) {
                for (int j = i - 1; j >= 0; j--) {
                    if (ss[j] < ss[i]) {
                        char c = ss[j];
                        ss[j] = ss[i];
                        ss[i] = c;
                        x = ++j;
                        label = 1;
                        break;
                    }
                }
                if (label)break;
            }
            if (label)sort(ss.begin() + x, ss.end());
            else {
                sort(ss.begin(), ss.end());
                if(ss[0]=='0')label=2;
            }
            printf("Case #%d: ", k);
            if (label==1)cout << ss << endl;
            else if(!label){
                printf("%c0", ss[0]);
                for (int i = 1; i < ss.size(); i++)
                    printf("%c", ss[i]);
                printf("\n");
            }
            else {
                int loc;
                for(int i=0;i<ss.size();i++)
                    if(ss[i]!='0'){loc=i;break;}
                string ans;
                ans.push_back(ss[loc]);
                ans.push_back('0');
                for(int i=0;i<ss.size();i++)
                    if(i!=loc)ans.push_back(ss[i]);
                ss=ans;
                cout<<ss<<endl;
            }
        }
    }
    return 0;
}






