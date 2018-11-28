#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int a[105][105];
int b[105][105];
int qx[105];
int qy[105];
int l, r;
int w, h;
int t;

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

void put(int x, int y){
//cout << x << " " << y << " " << b[x][y] << endl;
   qx[r] = x;
   qy[r] = y;
   ++r;
}
void get(int &x, int &y){
   x = qx[l];
   y = qy[l];
   ++l;
}
char c[30];

bool check(int x, int y, int x1, int y1){
     int ansx = -1;
     int ansy = -1;
     for (int k = 0; k < 4; ++k) 
         if (0 <= x + dx[k] && x + dx[k] < w && 0 <= y + dy[k] && y + dy[k] < h){
            if (a[x][y] > a[x + dx[k]][y + dy[k]]){
               if (ansx == -1 || a[ansx][ansy] > a[x + dx[k]][y + dy[k]]){
                  ansx = x + dx[k];
                  ansy = y + dy[k];
               }
            }
         }
//cout <<"!" << x << " " << y << " " << ansx <<  " " << ansy << endl;
     if (x1 == ansx && y1 == ansy) return true;
     return false;
}


int main(){
    cin >> t;
    for (int _i = 0; _i < t; ++_i){
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
        memset(c, 0, sizeof(c));
        memset(qx, 0, sizeof(qx));
        memset(qy, 0, sizeof(qy));

        cin >> w >> h;
        for (int i = 0; i < w; ++i)
            for (int j = 0; j < h; ++j){
                cin >> a[i][j];
            }

        l = 0;
        r = 0;
        int z = 1;

        for (int i = 0; i < w; ++i)
            for (int j = 0; j < h; ++j){
                int q = 0;
                for (int k = 0; k < 4; ++k){

                    if (0 <= i + dx[k] && i + dx[k] < w && 0 <= j + dy[k] && j + dy[k] < h){
                       if (a[i][j] <= a[i + dx[k]][j + dy[k]]) ++q;
                    }
                    else ++q;
                }
                if (q == 4){
                   b[i][j] = z;
                   put(i, j);
                   ++z;
                }


            }
        while(l <= r){
//cout <<"!" << l << " " << r << endl;
           int x, y;
           get(x, y);
           for (int k = 0; k < 4; ++k) 
               if (0 <= x + dx[k] && x + dx[k] < w && 0 <= y + dy[k] && y + dy[k] < h && b[x + dx[k]][y +dy[k]] == 0){
                  if (check(x + dx[k], y + dy[k], x, y)){
                     b[x + dx[k]][y + dy[k]] = b[x][y];
                     put(x + dx[k], y + dy[k]);
                  }
               }
        }
        char cc = 'a';
        cout << "Case #" << _i + 1 << ":\n";
        for (int i = 0; i < w; ++i){
            for (int j = 0; j < h; ++j){
                if (c[b[i][j]] != 0) cout << c[b[i][j]] << " ";
                else{
                   c[b[i][j]] = cc;
                   cout << c[b[i][j]] << " ";
                   ++cc;
                }
            }
            cout << endl;
        }
    }
    return 0;
}
