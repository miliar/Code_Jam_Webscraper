#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define debug(args...) fprintf(stderr,args);

typedef long long lint;
typedef pair<int,int> pii;

const int INF = 0x3f3f3f3f;
const lint LINF = 0x3f3f3f3f3f3f3f3fll;
const int MAXN = 1010;

struct per {
    int i;
    lint r,x,y;
    void read(int x) {
        scanf("%lld",&r);
        i = x;
    }        
    bool operator< (per that) const {
        return r > that.r;
    }
};

bool cmp(per a,per b) { return a.i < b.i; }

int n,w,l;
per p[MAXN];

bool inter(int a,int b) {
    if( (p[a].x-p[b].x)*(p[a].x-p[b].x) + (p[a].y-p[b].y)*(p[a].y-p[b].y) < (p[a].r+p[b].r)*(p[a].r+p[b].r) ) return true;
    return false;
}

int main() {
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;++t) {
        printf("Case #%d:",t);
        scanf("%d%d%d",&n,&w,&l);
        swap(w,l);
        int ow = w;
        for(int a=0;a<n;++a) p[a].read(a);
        int cnt=1;
        while(1) {
            debug("Test case %d, try #%d...\n",t,cnt++);
            w = ow;
            random_shuffle(p,p+n);
            int cur=0;
            //top
            lint curx=0,lim=l,maxh=0;
            while(cur<n) {
                if(curx==0) {
                    p[cur].x = 0; p[cur].y = w;
                    curx += p[cur].r;
                    maxh = p[cur].r;
                    ++cur;
                }
                else if(lim==l && curx <= l-p[cur].r) {
                    p[cur].x = l; p[cur].y = w;
                    lim -= p[cur].r;
                    maxh = max(maxh,p[cur].r);
                    ++cur;
                }
                else {
                    if(curx + 2*p[cur].r > lim) break;
                    p[cur].x = curx+p[cur].r;
                    p[cur].y = w;
                    curx += 2*p[cur].r;
                    maxh = max(maxh,p[cur].r);
                    ++cur;
                }
            }
            w -= maxh;
            //bottom
            curx=0,lim=l,maxh=0;
            while(cur<n) {
                if(curx==0) {
                    p[cur].x = 0; p[cur].y = 0;
                    curx += p[cur].r;
                    maxh = p[cur].r;
                    ++cur;
                }
                else if(lim==l && curx <= l-p[cur].r) {
                    p[cur].x = l; p[cur].y = 0;
                    lim -= p[cur].r;
                    maxh = max(maxh,p[cur].r);
                    ++cur;
                }
                else {
                    if(curx + 2*p[cur].r > lim) break;
                    p[cur].x = curx+p[cur].r;
                    p[cur].y = 0;
                    curx += 2*p[cur].r;
                    maxh = max(maxh,p[cur].r);
                    ++cur;
                }
            }
            //middle
            while(cur<n) {
                int curx=0, lim=l;
                while(cur<n) {
                    if(curx==0) {
                        p[cur].x = 0; p[cur].y = w-p[cur].r;
                        curx += p[cur].r;
                        maxh = 2*p[cur].r;
                        ++cur;
                    }
                    else if(lim==l && curx <= l-p[cur].r) {
                        p[cur].x = l; p[cur].y = w-p[cur].r;
                        lim -= p[cur].r;
                        maxh = max(maxh,2*p[cur].r);
                        ++cur;
                    }
                    else {
                        if(curx + 2*p[cur].r > lim) break;
                        p[cur].x = curx+p[cur].r;
                        p[cur].y = w-p[cur].r;
                        curx += 2*p[cur].r;
                        maxh = max(maxh,2*p[cur].r);
                        ++cur;
                    }
                }
                w -= maxh;
            }
            if(cur<n) {
                debug("failed!\n");
                continue;
            }
            //verify
            bool flag=0;
            for(int a=0;a<n;++a) {
                if(p[a].x > l || p[a].y > ow || p[a].x < 0 || p[a].y < 0) flag = 1;
                for(int b=a+1;b<n;++b)  {
                    if(inter(a,b)) flag = 1;
                }
            }
            if(flag) continue;
            else break;
        }
        sort(p,p+n,cmp);
        for(int a=0;a<n;++a) printf(" %lld %lld",p[a].x,p[a].y);
        printf("\n");
    }
    return 0;
}
