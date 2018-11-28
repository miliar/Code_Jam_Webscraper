// Website  :
// Contest  :
// Problem  :
// Language : C/C++

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string.h>
#include <math.h>
#include <algorithm>

// Bangke Style (DARKSTALKER)
int temp, i, j, k, T;
    // DEFINE
#define KASE while(T--)
#define REP(I, J, K) for((I)=(J);(I)<(K);(I)++)
#define HOLD {fflush(stdin); getchar ();}
#define INPUT(A) freopen(A, "r", stdin);
#define OUTPUT(A) freopen(A, "w", stdout);
#define reset(A, I) memset(A, I, sizeof A);
#define ll long long
#define INF 1000000000
#define MIN -1000000000
#define MAX 1000000
    // GRAPH DIRECTION
int x8[] = {1,1,0,-1,-1,-1, 0, 1};
int y8[] = {0,1,1, 1, 0,-1,-1,-1};
int x4[] = {1,0,-1, 0};
int y4[] = {0,1, 0,-1};
using namespace std;
// Bangke Style (DARKSTALKER)

typedef struct haha {
    int maks;
    int maks2;
};

int cek(int A, int B, int C) {
    return abs(A-B) + abs(B-C);          
}

//MAIN CODE
int main()
{
    haha google[2000];
    int n, s, p, point[2000], z, jawaban, kasus = 0, c;
    bool udah[2000];
    INPUT("B-large.in");
    OUTPUT("out.txt");
    cin >> T;
    KASE {
        kasus++;
        cin >> n >> s >> p;
        REP(i, 0, n)
            cin >> point[i];
        REP(i, 0, 2000) {
            google[i].maks = -1;
            google[i].maks2 = -1;
        }
        REP(z, 0, n)
            REP(i, 0, 11)
                REP(j, 0, 11)
                    REP(k, 0, 11) {
                            c = max(i, max(j, k));
                            if (i + j + k == point[z] && cek(i, j, k) < 2) {
                                if (google[z].maks < c)
                                    google[z].maks = c;
                            } else if (i + j + k == point[z] && cek(i, j, k) == 2) {
                                if (google[z].maks2 < c)
                                    google[z].maks2 = c;
                            }
                        }
        jawaban = 0;
        reset(udah, false);
        REP(i, 0, n) {
            if (google[i].maks >= p) {
                //cout << google[i].maks << endl;
                udah[i] = true;
                jawaban++;
            }
        }
        for(i=0;i<n && s > 0;i++) {
            //cout << i << " " << google[i].maks2 << endl;
            if (google[i].maks2 >= p && udah[i] == false) {
                //cout << google[i].maks2 << "@" << endl;
                jawaban++;
                s--;
                udah[i] = true;
            }
        }
        cout << "Case #" << kasus << ": ";
        cout << jawaban << endl;
    }
    return 0;
}
//END OF MAIN CODE
