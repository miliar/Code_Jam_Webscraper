#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <complex>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <climits>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;
//typedef long long LL;
typedef complex<double> tComp;

char field[50][50];

int main(int argc, char **argv) {
    //freopen("A.in", "r", stdin);

//      freopen("A-small-attempt0.in","r",stdin);
//      freopen("A-small-attempt0.out","w",stdout);

    //      freopen("A-small-attempt1.in","r",stdin);
    //      freopen("A-small-attempt1.out","w",stdout);

    //     freopen("A-small-attempt2.in","r",stdin);
    //     freopen("A-small-attempt2.out","w",stdout);

      freopen("A-large.in","r",stdin);
      freopen("A-large.out","w",stdout);

    int ntestcases = 0;
    scanf("%d\n", &ntestcases);

    int testcase = 0;
    while (testcase < ntestcases) {

        int N = 0;
        int K = 0;
        scanf("%d %d", &N, &K);

        string str;
        getline(cin, str);

        memset(field, '.', sizeof(field));

        for (int i = 0; i < N; ++i) {
            string str;
            getline(cin, str);
            int pos = 0;
            for (int j = N; j > 0; --j) {
                if (str[j-1] != '.') {
                    field[i][N-pos-1] = str[j-1];
                    ++pos;
                }
            }

        }

//        for (int i = 0; i < N; ++i) {
//            for (int j = 0; j < N; ++j) {
//                printf("%c", field[i][j]);
//            }
//            printf("\n");
//        }

        bool redbool = false;
        bool bluebool = false;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                for (int dir = -1; dir <= 1; dir += 2) {
                    int blue = 0;
                    int red = 0;
                    for (int curr = j; curr >= 0 && curr < N && curr < j + K * dir; curr += dir) {
                        if (field[i][curr] == 'R') {
                            ++red;
                        }
                        if (field[i][curr] == 'B') {
                            ++blue;
                        }
                    }
                    if (blue >= K) {
                        bluebool = true;
                    }
                    if (red >= K) {
                        redbool = true;
                    }

                    blue = 0;
                    red = 0;
                    for (int curr = i; curr >= 0 && curr < N && curr < i + K * dir; curr += dir) {
                        if (field[curr][j] == 'R') {
                            ++red;
                        }
                        if (field[curr][j] == 'B') {
                            ++blue;
                        }
                    }
                    if (blue >= K) {
                        bluebool = true;
                    }
                    if (red >= K) {
                        redbool = true;
                    }

                    blue = 0;
                    red = 0;
                    for (int curr = i, curr2 = j; curr >= 0 && curr < N && curr < i + K * dir && curr2 >= 0 && curr2 < N && curr2 < j + K * dir; curr += dir, curr2 += dir) {
                        if (field[curr][curr2] == 'R') {
                            ++red;
                        }
                        if (field[curr][curr2] == 'B') {
                            ++blue;
                        }
                    }
                    if (blue >= K) {
                        bluebool = true;
                    }
                    if (red >= K) {
                        redbool = true;
                    }

                    blue = 0;
                    red = 0;
                    for (int curr = i, curr2 = j; curr >= 0 && curr < N && curr < i + K * dir && curr2 >= 0 && curr2 < N && curr2 < j + K * dir; curr += dir, curr2 -= dir) {
                        if (field[curr][curr2] == 'R') {
                            ++red;
                        }
                        if (field[curr][curr2] == 'B') {
                            ++blue;
                        }
                    }
                    if (blue >= K) {
                        bluebool = true;
                    }
                    if (red >= K) {
                        redbool = true;
                    }

                }
            }
        }

//        cout << redbool << endl;
//        cout << bluebool << endl;

        printf("Case #%d: ", testcase + 1);

        if (redbool && bluebool) {
            cout << "Both";
        } else if (!redbool && !bluebool) {
            cout << "Neither";
        } else if (bluebool) {
            cout << "Blue";
        } else {
            cout << "Red";
        }

        printf("\n");

        ++testcase;
    }

    return 0;
}
