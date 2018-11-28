#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

int unsurprising(int total)
{
    if(total == 0) return 0;
    switch(total % 3){
        case 0:
            return (total / 3);
        case 1:
            return ((total - 1) / 3 + 1);
        case 2:
            return ((total - 2) / 3 + 1);
    }
}

int surprising(int total)
{
    if(total == 0) return 0;
    switch(total % 3){
        case 0:
            return (total / 3 + 1);
        case 1:
            return ((total - 1) / 3 + 1);
        case 2:
            return ((total - 2) / 3 + 2);
    }
}

int main()
{
    int t;
    std::cin >> t;
    
    std::ofstream out("b_out.txt");
    for(int i = 0; i < t; ++i){
        int n, s, p;
        std::cin >> n >> s >> p;
        
        std::vector<int> total(n);
        for(int j = 0; j < n; ++j){
            int a;
            std::cin >> a;
            total[j] = a;
        }
        
        std::sort(total.rbegin(), total.rend());
        int count = 0;
        for(int j = 0; j < n; ++j){
            //std::cout << unsurprising(total[j]) << " " << surprising(total[j]) << std::endl;
            if(unsurprising(total[j]) >= p){
                ++count;
            }else if((s > 0) && (surprising(total[j]) >= p)){
                ++count;
                --s;
            }
        }
        
        out << "Case #" << i + 1 << ": " << count << std::endl;
    }
}

