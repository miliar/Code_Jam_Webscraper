#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <ctime>


//#define DEBUG

using namespace std;

int main(){
	#ifndef DEBUG
		freopen("B-large.in", "r", stdin);
		freopen("B-large.out", "w", stdout);
	#endif
    int T;
    cin >> T;
    for (int test = 0; test < T; test++) {
        int N, S, p;
        int count = 0;
        cin >> N >> S >> p; 
        int* scores = new int[N];
        for (int i = 0; i < N; i++) {
            cin >> scores[i];
            //cout << scores[i] << " " << p*3 << endl;
            if(scores[i] >= p*3)
                count ++;
            else if (scores[i] != 0){
                float a = (scores[i] - p)/2.0;
                //cout << p - a << endl;
                if(p - a <= 1)
                    count++;
                else if(S && p - a <= 2){
                    count++;
                    S--;
                }
            }
        }
        cout << "Case #" << test+1 << ": " << count << endl;//Output Answer:
    }
	return 0;
}
