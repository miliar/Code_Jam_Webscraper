#include <stdio.h>
#include <iostream>

using namespace std;
#define maxn 101

int ntest, n, ds[maxn], nearest1[maxn], nearest2[maxn], lntest;

void open_file() {
    freopen("A-large.in", "r",stdin);
    freopen("A.outs", "w", stdout);    
}

void init(int ds[], int n) {
    nearest1[n] = -1;
    nearest2[n] = -1;
    for (int i = n-1; i >= 0; i--) {
        nearest1[i] = nearest1[i+1];
        nearest2[i] = nearest2[i+1];        
        if (ds[i] > 0) nearest1[i] = ds[i];   
        if (ds[i] < 0) nearest2[i] = -ds[i];           
    }    
}

void move(int &x, int &y, int &d) {
    if (ds[d] > 0) {
        
        if (y < nearest2[d]) y++;   
        if (y > nearest2[d]) y--;
        
        if (x == ds[d]) d++;
        else{
            if (x < nearest1[d]) x++;   
            if (x > nearest1[d]) x--;
        }
    } else  
    if (ds[d] < 0) {
        
        if (x < nearest1[d]) x++;   
        if (x > nearest1[d]) x--;        
        
        if (y == -ds[d]) d++;
        else{
            if (y < nearest2[d]) y++;   
            if (y > nearest2[d]) y--;
        }            
    }    
}

void process() {
    int t = 0, x = 1, y = 1, d = 0;
    while (1) {
        t++;
        move(x, y, d);       
        if (d == n) {
            cout << "Case #" << lntest - ntest << ": " << t << endl;
            return;               
        }
    }    
}

int main () {
    open_file();
    cin >> ntest;
    lntest = ntest;
    while (ntest--) {
        char ch;
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> ch;   
            if (ch == 'O') cin >> ds[i];
            if (ch == 'B') {
                cin >> ds[i];            
                ds[i] = -ds[i];
            }
        }
        init(ds, n);
        process();               
    }
    return 0;   
}
