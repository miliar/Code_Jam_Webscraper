#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int
main(void)
{
    int N, T, NA, NB;
    int i, j, ts, ta, t;
    string s;
    vector<int> va;
    vector<int> vb;
    int sum_a, sum_b;
    int req_a, req_b;
    int va_s_i;
    int va_a_i;
    int vb_s_i;
    int vb_a_i;

    cin >> N;
    for(i=1;i<=N;i++) {
        cin >> T >> NA >> NB;
        va.clear();
        vb.clear();
        for(j=0;j<NA;j++) {
            cin >> s;
            ts = (s[0]-'0')*10 + (s[1]-'0');
            ts *= 60;
            ts += (s[3]-'0')*10 + (s[4]-'0');
            va.push_back(ts*2+1);

            cin >> s;
            ta = (s[0]-'0')*10 + (s[1]-'0');
            ta *= 60;
            ta += (s[3]-'0')*10 + (s[4]-'0');
            ta += T;
            vb.push_back(ta*2);
        }
        
        for(j=0;j<NB;j++) {
            cin >> s;
            ts = (s[0]-'0')*10 + (s[1]-'0');
            ts *= 60;
            ts += (s[3]-'0')*10 + (s[4]-'0');
            vb.push_back(ts*2+1);

            cin >> s;
            ta = (s[0]-'0')*10 + (s[1]-'0');
            ta *= 60;
            ta += (s[3]-'0')*10 + (s[4]-'0');
            ta += T;
            va.push_back(ta*2);
        }

        sort(va.begin(), va.end());
        sort(vb.begin(), vb.end());

        int va_a, va_s;
        int vb_a, vb_s;

        sum_a = sum_b = 0;
        req_a = req_b = 0;
        va_a  = va_s = 0;
        vb_a  = vb_s = 0;

        for(j=0;j<va.size();j++) {
            if (va[j] % 2) {
                va_s++;
            } else {
                va_a++;
            }
            req_a = max(req_a, va_s-va_a);
        }
        for(j=0;j<vb.size();j++) {
            if (vb[j] % 2) {
                vb_s++;
            } else {
                vb_a++;
            }
            req_b = max(req_b, vb_s-vb_a);
        }
        
        cout << "Case #" << i << ": " << req_a << " " << req_b << endl;
        
    }
    
    return 0;
}
