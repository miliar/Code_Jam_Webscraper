#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<queue>
#include<cstdlib>
#include<time.h>
#include<string.h>
#include<list>
#include<sstream>
#include<algorithm>
#include<math.h>
using namespace std;
#define ps system("pause")
struct node {
    int start,end;
    int w;

};
int x,s,r,n;
double rest;
double eps = 1e-6;
bool cmp(node x1,node x2) {
    return x1.w < x2.w;
    double len1 = x1.end - x1.start;
    double len2 = x2.end = x2.start;
    double ans1 = len1/(x1.w + s) - len1/(x1.w + r);
    double ans2 = len2/(x2.w + s) - len2/(x2.w + r);
    return ans1 > ans2;
}
bool cmp2(node x1,node x2) {
    return x1.start < x2.start;
}
int main()
{
    int t;
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    cin >> t;
    vector<node> p;
    for (int cas = 1; cas <= t; cas ++) {
        
        
        cin >> x >> s >> r >> rest >> n;
        p.clear();
        while(n--) {
            node a;
            cin >> a.start >> a.end >> a.w;
//            a.w += s;
            p.push_back(a);
        }
        double ans = 0.0;        
        sort(p.begin(),p.end(),cmp2);
        int pre = 0;
        n = p.size();
        for (int i = 0; i < n; i ++) {
            if (p[i].start != pre) {
                node a;
                a.start = pre;
                a.end = p[i].start;
                a.w = 0;
                p.push_back(a);
                
            }
            pre = p[i].end;
        }
        node a ;
        a.start = pre;
        a.end = x;
        a.w = 0;
        p.push_back(a);
        sort(p.begin(),p.end(),cmp);
        /*
        for (int i = 0; i < p.size(); i ++){
            cout << p[i].start << " " << p[i].end <<endl;
        }
        */

        double len = 0.0;
        double dist = 0.0;
        double tmp;
        ans = 0.0;
        for (int i = 0; i < p.size(); i ++ ){
            len = p[i].end - p[i].start;
            if (fabs(rest) > eps) {
                dist = rest * (p[i].w + r);
                if (dist > len) {
                    tmp = len/(p[i].w + r);
                    rest -= tmp;
                    ans += tmp;
                } else {
                    len -= (p[i].w + r) * rest;
                    ans += rest;
                    rest = 0.0;
                    ans += len / (p[i].w + s);
                }
            } else {
                ans += len/double(p[i].w + s);
            }
//            cout << ans << " " << rest <<endl;
            
        }
        printf("Case #%d: %.9lf\n",cas,ans);
        
    }
    return 0;
}
