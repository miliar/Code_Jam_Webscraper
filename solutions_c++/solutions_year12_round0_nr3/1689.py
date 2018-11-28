#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

int b[2000010], f[2000010], ans[110];
class Node {
    public:
        int a, b, c;
};
Node a[110], temp;
int mm;

int Lowbit(int t)
{
    //return t & (~t);
    return t & ( t ^ ( t - 1 ) );
}

void add(int i) {
    while (i <= mm) {
        f[i]++;
        i += Lowbit(i);
    }
}

int find(int i) {
    int f1 = 0;
    while (i > 0) {
        //cout << i << endl;
        f1 += f[i];
        i -= Lowbit(i);
    }
    return f1;
}


int main() {
  //  freopen("input.txt", "r", stdin);
   // freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    memset(b, -1, sizeof(b));
    memset(ans, 0, sizeof(ans));
    memset(f, 0, sizeof(f));
    for (int i = 0; i < t; i++) {
        int j,k;
        cin >> j >> k;
        a[i * 2].a = j - 1; a[i * 2 + 1].a = k;
        a[i * 2].b = k; a[i * 2 + 1].b = j - 1;
        a[i * 2].c = i; a[i * 2 + 1].c = i;
        //b[j - 1] = k; b[k] = j - 1;
        if (k > mm) mm = k;
    }
    int nn = t * 2;
    for (int i = 0; i < nn; i++) {
        for (int j = i + 1; j < nn; j++) {
            if (a[i].a > a[j].a) {
                temp = a[i]; a[i] = a[j]; a[j] = temp;
            }
        }
        //cout << a[i].a << ' ' << a[i].b << ' ' << a[i].c << endl;
    }
    mm = mm + 1;
    int ll = 0;
    while (a[ll].a == 0 && ll < nn) {
        ll++;
    }
    for (int i = 1; i <= mm; i++) {
        char s[10] = "";
        sprintf(s, "%d", i); int l = 1;
        char d[10][10];
        for (int j = 1; j < strlen(s); j++) {
             l = l * 10;
            if (i % l != 0) {
            sprintf(d[j], "%d%d", i % l,i / l);
            bool u = true;
            for (int k = j - 1; k >= 1; k--) {
                if (strcmp(d[j], d[k]) == 0) {u = false;}
            }
            if (u && strlen(d[j]) == strlen(s))
            if (int(atof(d[j])) < i) {
                /*if (i > 1111 && int(atof(d[j])) > 1111) { if (i <= int(atof(d[j]))) cout << "!!!!!!!";
                check++;
                cout << "HH" << check << ' ' << i << ' ' << int(atof(d[j])) << endl;
                }*/
                add(int(atof(d[j]))); }
            }
        }

       // cout << b[i] << endl;
        //if (b[i] >= 0) {
          //  int l1 = find(i), l2 = find(b[i]);
          //  cout << 'h' << l1 << ' ' << l2 << endl;
           // b[i] = fabs(l1 - l2);
          //  cout << b[i] << endl;}
        while (ll < nn && a[ll].a == i) {
            int l1 = find(a[ll].a), l2 = find(a[ll].b);
            //cout << l1 <<  ' ' << l2 << ' ' << fabs(l1 - l2) << endl;
            ans[a[ll].c] = fabs(ans[a[ll].c] - fabs(l1 - l2));
            ll++;
        }
    }
    b[0] = 0;
    for (int i = 0; i < t; i++)
        cout << "Case #" << i + 1 << ": " << ans[i] << endl;
}
