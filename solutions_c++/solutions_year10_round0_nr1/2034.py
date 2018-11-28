#include <cstdlib>
#include <vector>
#include <queue>
#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#include <map>
#include <cmath>
#include <cstdlib>
#include <list>
#include <set>

using namespace std;


int main(int argc, char** argv) {
     freopen("in.txt", "r", stdin);
     freopen("out.txt", "w", stdout);




        int T;
        cin >> T;
        int test = 0;
        while (test++ < T) {
            int N,K;
            cin >> N >> K;
            if (K == 0) {
                cout << "Case #" << test << ": " << "OFF" << endl;
                continue;
            }

            K = (K+1) % (1<<N);


            cout << "Case #" << test << ": " << (K  == 0 ? "ON" : "OFF") << endl;
        }

        



    return (EXIT_SUCCESS);
}

