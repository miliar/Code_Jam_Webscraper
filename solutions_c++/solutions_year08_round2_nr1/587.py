#include <iostream>
#include <vector>
#include <algorithm>

struct Point {
    unsigned long long x, y;
};

int main () {
    
    int cases;
    std::cin >> cases;
    
    for (int case_num = 1; case_num <= cases; ++case_num) {
        
        unsigned long long N, A, B, C, D, M;
        std::cin >> N >> A >> B >> C >> D;
        
        std::vector<Point> trees (N);
        
        std::cin >> trees[0].x >> trees[0].y;
        std::cin >> M;
        
        for (unsigned long long i=1; i<N; ++i) {
            trees[i].x = (A*trees[i-1].x + B) % M;
            trees[i].y = (C*trees[i-1].y + D) % M;
        }
        
        int triangles = 0;
        for (int i=0; i<N-2; ++i) {
            for (int j=i+1; j<N-1; ++j) {
                for (int k=j+1; k<N; ++k) {
                    if ((trees[i].x + trees[j].x + trees[k].x) % 3 == 0 &&
                        (trees[i].y + trees[j].y + trees[k].y) % 3 == 0) {
                        ++triangles;
                    }
                }
            }
        }
        
        std::cout << "Case #" << case_num << ": " << triangles << std::endl;
    }
}