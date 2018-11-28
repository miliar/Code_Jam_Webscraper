#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
#include <stdlib.h>

int Solve(std::vector<int>& scores, int S, int p) {
//    std::cout << "S: " << S << " p: " << p << " size: " << scores.size() << std::endl;
    sort(scores.begin(), scores.begin()+scores.size(), std::greater<int>());
    int answer = 0;
    for(int i=0; i<scores.size(); i++) {
        int div = scores[i]/3;
        int mod = scores[i]%3;
        if( (div >= p) || (div >= p-1 && div+mod >= p) ) {
            answer++;
            continue;
        }
        if(S>0) {
            if(div >= p-1 && scores[i] > (3*p)-4 && scores[i] > 0 ) {
                answer++;
                S--;
                continue;
            }
            if(div >= p-2 && scores[i]%3 > 1) {
                answer++;
                S--;
                continue;
            }
        }
        break;
    }
    return answer;
}

int main(int argc, char** argv){
    int T, N, S, p, temp;
    std::vector<int> scores;
    scanf("%d\n", &T);
    int test_case = 0;
    while(T--){
        scanf("%d %d %d ", &N, &S, &p);
        scores.clear();
        for(int i=0; i<N; i++) {
            scanf("%d", &temp);
            scores.push_back(temp);
        }

        std::cout << "Case #" << ++test_case << ": " << Solve(scores, S, p) << std::endl;
    }
}
