#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>

using namespace std;

int main(){
    int n_cases;
    cin >> n_cases;

    string N;
    char C[256];

    for(int n_case = 1; n_case <= n_cases; n_case++){
        cin >> N;

        //find rightest i such that N[i] < N[i+1] (if it does exist)
        int i = N.length()-2;
        while (i >= 0){
            if (N[i] < N[i+1])
                break;
            i--;
        }

        cout << "Case #" << n_case << ": ";

        if (i >= 0){
            //search smallest N[j] > N[i], with j > i
            int j;
            int best_j = -1;
            unsigned char best = 255; //INF

            for (j = i+1; j < N.length(); j++)
                if (N[j] > N[i] && best > N[j]){
                    best_j = j;
                    best = N[j];
                }

            //print N[0..(i-1)]
            for (int k = 0; k <= i-1; k++)
                cout << N[k];

            //print N[best_j]
            cout << N[best_j];

            //print remaining characters in ascending order
            int count = 0;
            for (int k = i; k < N.length(); k++)
                if (k != best_j){
                    C[count] = N[k];
                    count++;
                }
            sort(C, C + count);

            for (int k = 0; k < count; k++)
                cout << C[k];
            cout << endl;
        } else {
            //need to add a 0

            //search smallest N[j] != '0'
            int j;
            int best_j = -1;
            unsigned char best = 255; //INF

            for (j = 0; j < N.length(); j++)
                if (N[j] != '0' && best > N[j]){
                    best_j = j;
                    best = N[j];
                }

            //print N[best_j]
            cout << N[best_j];

            cout << '0';

            //print remaining characters in ascending order
            int count = 0;
            for (int k = 0; k < N.length(); k++)
                if (k != best_j){
                    C[count] = N[k];
                    count++;
                }
            sort(C, C + count);

            for (int k = 0; k < count; k++)
                cout << C[k];
            cout << endl;
        }
    }

    return 0;
}
