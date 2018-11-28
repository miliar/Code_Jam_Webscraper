#include <iostream>
#include <queue>

typedef unsigned long long uint;

struct letter_frequency {
    
    int letter;
    int frequency;
    
    bool operator< (const letter_frequency& o) {
        
        return frequency < o.frequency;
    }
};

int main () {
    
    int cases;
    std::cin >> cases;
    
    for (int case_num=1; case_num<=cases; ++case_num) {
        
        uint P, K, L;
        std::cin >> P >> K >> L;
        
        std::priority_queue<uint> frequencies;
        
        for (int i=0; i<L; ++i) {
            
            uint freq;
            std::cin >> freq;
            frequencies.push (freq);
        }
        
        uint p = 1;
        uint keypresses = 0;
        uint key = 0;
        while (!frequencies.empty()) {
            
            keypresses += p * frequencies.top();
            
            ++key;
            if (key == K) {
                ++p;
                key = 0;
            }
            
            frequencies.pop();
        }
        
        std::cout << "Case #" << case_num << ": " << keypresses << std::endl;
    }
}
