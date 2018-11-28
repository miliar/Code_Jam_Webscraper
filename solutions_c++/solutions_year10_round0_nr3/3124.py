#include <cstdlib>
#include <memory>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int a[1001];
int b[1001];

int main(){
    string fname = "C-small-attempt0";
    freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int i, j, k, t;
	int caseNum;
	cin >> caseNum;
	for (i = 1; i <= caseNum; i++){
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
        int R, cap, N;
        int res = 0;
        cin >> R >> cap >> N;
        for (j = 0; j < N; j++)
            cin >> a[j];
        int sum = 0;
        for (j = 0; j < R; j++){
            for (t = 0; t < N; t++){
                sum += a[t];
                b[t] = a[t];
                if (sum > cap){
                    res += sum - a[t];
                    for (k = t; k < N; k++)
                        a[k-t] = a[k];
                    for (k = 0; k < t; k++)
                        a[N - t + k] = b[k];
                    sum = 0;
                    break;
                }
            }
            if (t == N){
                res += sum;
                sum = 0;
            }
        }
        cout << "Case #" << i << ": ";
        cout << res << endl;
    }
}
