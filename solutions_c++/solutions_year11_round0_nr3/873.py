#include <iostream>
#include <fstream>
#include <string>
#include <vector>
int abs(int a){
    if(a>0) return a;
    return -a;
}
int max(int a,int b){
    if(a>b) return a;
    return b;
}
int main()
{
    std::string filename;
    std::cout << "Filename: ";
    std::getline(std::cin,filename);
    std::ifstream input(filename.c_str(),std::ios::in);
    std::ofstream output("output.txt",std::ios::out);
    int T;
    input >> T;
    for(int i = 1;i<=T;i++){
        int N;
        input >> N;
        int* candies = new int[N];
        int total = 0; //Patrick's total
        int realtotal = 0;
        int least = 10000000;
        for(int j = 0;j < N;j++){
            input >> candies[j];
            total = total ^ candies[j];
            realtotal += candies[j];
            if(candies[j] < least) least = candies[j];
        }
        if(total == 0){
            output << "Case #" << i << ": "  << (realtotal-least) << "\n";
        }else{
            output << "Case #" << i << ": NO\n";
        }
    }
    output.flush();
    output.close();
    return 0;
}
