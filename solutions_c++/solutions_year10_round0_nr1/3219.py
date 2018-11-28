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

int main(){
    //string fname = "A-small-attempt3";
    string fname = "A-large";
    freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
    int T;
    cin >> T;
    int c, i, j;
    for (c = 1; c <= T; c++){
        int n, k;
        cin >> n >> k;
        int sat = 1;
        for (i = 0; i < n; i++)
            sat *= 2;
        int r = (k + 1) % sat;
        if (r == 0){
            cout << "Case #" << c << ": ";
            cout << "ON" << endl;
        }
        else{
            cout << "Case #" << c << ": ";
            cout << "OFF" << endl;
        }
    }
    //system("pause");
    return 0;
}
