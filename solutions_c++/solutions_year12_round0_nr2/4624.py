#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
#define MAXN 100

using namespace std;

int points[MAXN];

int maxBestResult(int S, int p, int N){
    int sobra, prom, count=0;
    for(int i = 0; i < N; ++i){
        sobra = points[i] % 3;
        prom = points[i] / 3;
        if(prom >= p || (sobra > 0 && p-prom == 1 )){
            count++;
        }else{
            if(S>0 && ((sobra > 1 && p-prom ==2)||(sobra == 0 && prom>0 && p-prom ==1))){
                count++;
                S--;
            }
        }
    }
    return count;
}

int main(){
    int T, N, S, p;
    cin >> T;
    for(int j=0; j<T; ++j){
        cin >> N >> S >> p;
        for(int i=0; i<N; ++i){
            cin >> points[i];
        }
        cout << "Case #" << j+1 << ": " << maxBestResult(S, p, N) <<endl;
    }
    return 0;
}
