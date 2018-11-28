#include <iostream>
#include <string>
using namespace std;

int c[110][110];
int b[110][110];
char a[110][110];
int n, m;
int si, sj;
int M = 100000000;
char an;

class point {
public:
      int x, y;
      point(){x=y=0;}
      point(int xx, int yy) {x = xx; y = yy;}
      point (const point &p) {x=p.x; y=p.y;}
      point n() {return  point(x-1,y);}
      point w() {return  point(x,y-1);}
      point e() {return  point(x,y+1);}
      point s() {return  point(x+1,y);}
      int h() {return c[x][y];}
      int same(const point &p) {return x == p.x&& y == p.y;}
};
int ok(const point &p) {
    //cout << p.x << " " << p.y << endl;
    return p.x>=0 && p.x<n && p.y>=0 && p.y<m;
}
point toone(point t) {
     point p, rp = t;
     //cout << t.x << " " << t.y << endl;
     int l = t.h();
     p = t.n(); if (ok(p) && p.h() < l) {l=p.h(); rp = p;}
     p = t.w(); if (ok(p) && p.h() < l) {l=p.h(); rp = p;}
     p = t.e(); if (ok(p) && p.h() < l) {l=p.h(); rp = p;}
     p = t.s(); if (ok(p) && p.h() < l) {l=p.h(); rp = p;}
     //cout << n << " " << m << " " <<t.x <<" " << t.y << "->"<< rp.x <<  " "<<rp.y<<endl;
     return rp;
}
point towhere(point t) {
     //n w e s
     point p = t;
     //cout << p.x << " " << p.y << endl;
     point q = toone(p);
     while(!p.same(q)) {
        p = q;
        q = toone(p);
        
     }
     return q;
}
void gotoanywhere(point t) {
     if (a[t.x][t.y]!=0) return;
     a[t.x][t.y]=an;
     point p;
     p = t.n(); if (ok(p) && toone(p).same(t)) gotoanywhere(p);
     p = t.w(); if (ok(p) && toone(p).same(t)) gotoanywhere(p);
     p = t.e(); if (ok(p) && toone(p).same(t)) gotoanywhere(p);
     p = t.s(); if (ok(p) && toone(p).same(t)) gotoanywhere(p);
     
}
void done(){
    memset(a, 0, sizeof(a));
    an = 'a';
    for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) if (a[i][j] == 0) {
        point source = towhere(point(i, j));
        gotoanywhere(source);
        an++;
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (j) cout << " ";
            cout << a[i][j];
        }
        cout << endl;
    }
    
}
int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
       cout << "Case #" << i + 1 << ":" << endl;
       cin >>n >> m;
       for (int j = 0; j < n; ++j) for (int k = 0; k < m; ++k) cin >> c[j][k];
       done();
    }
    return 0;
}
     
