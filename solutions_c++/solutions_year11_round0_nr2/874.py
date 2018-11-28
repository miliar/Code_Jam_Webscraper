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
        std::string result = "";
        int contains[256];
        for(int j = 0;j < 256;j++) contains[j] = 0;
        unsigned char last = 0;
        int combine;
        input >> combine;
        unsigned char combines[65536];
        for(int j = 0;j < 65536;j++) combines[j] = 0;
        for(int j = 0;j < combine;j++){
            unsigned char a,b,c;
            input >> a >> b >> c;
            combines[a*256+b] = c;
            combines[b*256+a] = c;
        }
        int oppose;
        input >> oppose;
        std::vector<unsigned char> opposes[256];
        for(int j = 0;j < oppose;j++){
            unsigned char a,b;
            input >> a >> b;
            opposes[a].push_back(b);
            opposes[b].push_back(a);
        }
        int length;
        input >> length;
        for(int j = 0;j < length;j++){
            unsigned char n;
            input >> n;
            char c = combines[n*256+last];
            if(c != 0){
                contains[last]--;
                result[result.length()-1] = c;
                n = c;
            }
            contains[n]++;
            for(int k = 0;k < opposes[n].size();k++){
                if(contains[opposes[n][k]] > 0){
                    result = "";
                    for(int ii = 0;ii < 256;ii++){
                        contains[ii] = 0;
                    }
                    last = 0;
                    n = 0;
                    break;
                }
            }
            last = n;
            if(c == 0 && n != 0) result += n;
        }
        output << "Case #" << i << ": [";
        bool isfirst = true;
        for(int i = 0;i < result.length();i++){
            if(!isfirst) output << ", ";
            else isfirst = false;
            output << result[i];
        }
        output << "]\n";
    }
    output.flush();
    output.close();
    return 0;
}
