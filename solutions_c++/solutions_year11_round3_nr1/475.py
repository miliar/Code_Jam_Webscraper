#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <queue>
#include <map>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
using namespace std;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef vector<double> vd;
typedef queue<int> qi;

#define fori(i, n) for(i=0;i<n;i++)
#define fordi(i, n) for(int i=0;i<n;i++)
#define INF 0x7fffffff

char sc() {char r; if (scanf("%c", &r) != 1) {printf("-1"); exit(0);} return r;}
int si() {int r; if (scanf("%d", &r) != 1) {printf("-1"); exit(0);} return r;}
long long sli() {long long r; if (scanf("%lld", &r) != 1) {printf("-1"); exit(0);} return r;}
double sf() {double r; if (scanf("%lf", &r) != 1) {printf("-1"); exit(0);} return r;}

void red(vii &pic, int r, int c) {
    fordi(i, r-1) {
        fordi(j,c-1) {
            if (pic[i][j] == 1) {
                if (pic[i][j+1] !=1 || pic[i+1][j] !=1 || pic[i+1][j+1]!=1) {
                    printf("Impossible\n");
                    return;
                }
                pic[i][j] = 2;
                pic[i][j+1] = 3;
                pic[i+1][j] = 3;
                pic[i+1][j+1] = 2;
            }
        }
    }

    fordi(i,r) {
        if(pic[i][c-1]==1) {
                    printf("Impossible\n");
                    return;
                }
    }
    fordi(i,c) {
        if(pic[r-1][i]==1) {
                    printf("Impossible\n");
                    return;
                }
    }
    fordi(i, r) {
        fordi(j,c) {
            switch (pic[i][j]) {
                case 0: printf("."); break;
                case 2: printf("/"); break;
                case 3: printf("\\"); break;
            }
        }
        printf("\n");
    }

}

main() {
    int t=si();
    fordi(ii,t) {
        printf("Case #%d:\n",ii+1 );
        int r =si(); int c=si();
        vii pic;
        pic.resize(r);
        fordi(j,r) {
            string s;
            cin >> s;
            pic[j].resize(c);
            fordi(k,c) {
                if (s[k]=='.') pic[j][k] = 0;
                if (s[k]=='#') pic[j][k] = 1;
            }
        }
        red(pic,r,c);
    }
}
