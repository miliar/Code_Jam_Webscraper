#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<vector>
#include<map>
#include<string>
#include<iostream>
#define int64 long long
using namespace std;

int t;
string s;

int64 getnum(string st) {
    int tl;
    int64 res = 0;
    for(int i=0;i<st.size();i++) {
        tl = (st[i]-'0');
        res = res*10LL+(int64)tl;
    }
    return res;
}

int main() {
    scanf("%d",&t);
    for(int z=0;z<t;z++) {
        cin>>s;
        int l = s.size()-1;
        int ret = 0, op = 1;
        int64 sum = 0LL;
        string cs = "";
        for(int i=0;i<(int)pow(3.0,(double)l);i++) {           
            cs = s[0];
            sum = 0LL;
            op = 1;
            int tmp = i;
            for(int j=0;j<l;j++) {
                if(tmp%3 == 0) cs += s[j+1];
                else {
                    if(op == 1) sum += getnum(cs);
                    else sum -= getnum(cs);
                    cs = s[j+1];
                    op = tmp%3;
                }
                tmp /= 3;
            }
            if(op == 1) sum += getnum(cs);
            else sum -= getnum(cs);
            if(sum%2LL == 0 || sum%3LL == 0 || sum%5LL == 0 || sum%7LL == 0) ret++;
            //if(ret == 531441) break;
        }
        printf("Case #%d: %d\n",z+1,ret);
    }
    return 0;
}
                 
            
            
            
