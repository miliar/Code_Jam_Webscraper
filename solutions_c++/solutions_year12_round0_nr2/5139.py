#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int main(int argc, char* argv[]) {
    int t = 0;
    std::string line;
    std::getline(std::cin, line);
    
    char* temp = 0;
    t = strtol(line.c_str(), &temp, 0);
    
    for(int i = 0; i < t; i++){
        std::getline(std::cin, line);
        std::istringstream src(line);
        
        int n, s, p;
        src >> n >> s >> p;
        
        int ans = 0;
        
        for(int j = 0; j < n; j++){
            int score;
            src >> score;
            int min = score / 3;
            int max = (score % 3 == 0)? min : min+1;
            if(max >= p){
                ans++;
            }else if(s > 0 && (score > 0 || p == 0)){
                min = score / 3;
                switch(score % 3){
                    case 0 :
                        // 3x = x-1 + x + x+1
                        max = min+1;
                        break;
                    case 1 :
                        // 3x+1 = x+1 + x+1 + x-1
                        max = min+1;
                        break;
                    case 2 :
                        // 3x+2 = x+2 + x + x
                        max = min+2;
                        
                        break;
                    default :
                        break;
                }
                if(max >= p){
                    ans++;
                    s--;
                }
            }
        }
        std::cout << "Case #" 
                << (i+1)
                << ": "
                << ans
                << std::endl;                
    }
    return 0;
}
