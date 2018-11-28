#include <iostream>
#include <vector>

int main(){
    int T;
    std::cin >> T;
    for(int t=1; t<=T; ++t){
        std::cout << "Case #" << t << ": ";
        int n;
        std::cin >> n;
        std::vector<unsigned> bits(20, 0);
        std::vector<unsigned> c(n);
        unsigned check=0;
        unsigned min=1<<30;
        unsigned tt=0;
        for(int i=0; i<n; ++i){
            std::cin >> c[i];
            check^=c[i];
            if(c[i]<min) min=c[i];
            tt+=c[i];
        }

        if(check)
            std::cout << "NO" << std::endl;
        else 
            std::cout << tt-min << std::endl;
    }
}
