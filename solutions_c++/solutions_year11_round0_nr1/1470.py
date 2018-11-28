#include <iostream>
#include <cstdlib>

int main(){
    int nbcase;
    std::cin >> nbcase;
    for(int i=1; i<=nbcase; ++i){
        int n;
        std::cin >> n;
        int b=1;
        int o=1;
        int dO=0, dB=0;
        int ttmv=0;

        std::cout << "Case #" << i << ": ";
        for(int j=0; j<n; ++j){
            std::cin.ignore(1, ' ');
            char robot;
            int target;
            std::cin >> robot >> target;
            if(robot=='B'){
                if(dB<std::abs(target-b)){
                    ttmv+=std::abs(target-b)-dB+1;
                    dO+=std::abs(target-b)-dB+1;
                } else { // On a eut le temps d'y aller
                    ttmv++;
                    dO++;
                }
                b=target;
                dB=0;
            } else{
                if(dO<std::abs(target-o)){
                    ttmv+=std::abs(target-o)-dO+1;
                    dB+=std::abs(target-o)-dO+1;
                } else { // On a eut le temps d'y aller
                    ttmv++;
                    dB++;
                }
                o=target;
                dO=0;
            }
        }
        std::cout << ttmv << std::endl;
    }
}
