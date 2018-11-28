#include<algorithm>
#include<cstdio>
#include<set>
#include<cmath>
using namespace std;

set<pair<int,int> > h;

int mp(int len) {
    int r=1;
    while(len--) r*=10;
    return r;
}

int digitLen(int v) {
    int r=0;
    while(v) v/=10 , r++;
    return r;
}

int getNext(int& v,int& len) {
    int t = v/10 + (v%10*mp(len-1));
    v=t;
    return v;
}

int main() {

    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++) {
        int a,b,len;
        scanf("%d %d\n",&a,&b); 
        len = digitLen(a);
        h.clear();
        for(int i=a;i<=b;i++) {
            int ta = i;
            for(int j=0;j<len-1;j++) {
                int tb = getNext(ta, len);
                if(digitLen(tb)==len && tb<=b && i<tb) {
                    h.insert(make_pair(i,tb) );
//                    printf("%d %d\n",i,tb );
                }
            } 
        }
        printf("Case #%d: %d\n",t,h.size());
    }
}

