#include <cstdio>
#include <set>
using namespace std;
int v[20], v_len;
int nd[20], d_len;
set<int> sv;

void get_nd(int x) {
    //int len = 0;
    int t;
    while (x) {
        t = x % 10;
        nd[d_len++] = t;
        x /= 10;
        //len++;
    }
    
    //for (int i = 0; i < d_len; i++) printf("%d ",nd[i]);
    //printf("\n");
    
    
    return ;       
}

int pow_10(int v) {
    int res = 1;
    for (int i = 1; i <= v; i++) {
        res *= 10;
    }    
    return res;
}


void get_r(int n) {
     int x, y, i, j, tmp;
     get_nd(n);
     for (i = 0; i < (d_len - 1); i++) {
         x = 0;
         y = 0;
         for (j = i; j >= 0; j--) {
             x = x * 10 + nd[j];
         }
         
         for (j = d_len - 1; j > i; j--) {
             y = y * 10 + nd[j];
         }
         
         tmp = pow_10(d_len - i - 1) * x + y;
        // printf("%d %d %d\n",x, y, tmp);
         //if (x != 0) v[v_len++] = tmp;
         //if (x != 0) {
               //printf("%d %d %d\n",x, y, tmp);
                sv.insert(tmp);
         //}
     }
}

void test(int x) {
     v_len = 0;
     d_len = 0;
     get_r(x);
}

int main() {

freopen("C-small-attempt2.in", "r", stdin);
freopen("C-small-attempt2.out", "w", stdout);
    int T, ct, cnt, i, a, b, j;
    scanf("%d",&T);
    
    //while (scanf("%d",&a)) { test(a); }
    
    for (ct = 1; ct <= T; ct++) {
        scanf("%d %d",&a, &b);
        //printf("%d %d\n",a, b);
        cnt = 0;
        for (i = a; i < b; i++) {
            //v_len = 0;
            d_len = 0;
            sv.clear();
            get_r(i);
            
            //if (v > i) cnt++;
           /*
            for (j = 0; j < v_len; j++) {
                if (v[j] > i && ( v[j] >= a && v[j] <= b) ) {
                          cnt++;    
                          printf("%d %d\n",i, v[j]);
                }
            }
            */
            //printf("%d\n",sv.size());
            for (set<int>::iterator it = sv.begin(); it != sv.end(); it++) {
                int t = *it;
               // printf("%d\n",t);
                if (t > i && ( t > a && t <= b) ) {
                          cnt++;    
                          //printf("%d %d\n",i, t);
                }
            }
            
            
        }
        printf("Case #%d: %d\n",ct, cnt);
        
        
    }
    return 0;
}