#include <iostream>
#include <fstream>
#include <string>
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
        bool O = false;
        bool first = true;
        int bPos = 1;
        int oPos = 1;
        int oTime = 0;
        int bTime = 0;
        for(int j = 0;j < N;j++){
            char Oc;
            int V;
            input >> Oc;
            input >> V;
            bool nO = (Oc == 'O');
            if(nO == O){
                if(nO){
                    oTime = oTime + abs(oPos - V) + 1;
                    oPos = V;
                }else{
                    bTime = bTime + abs(bPos - V) + 1;
                    bPos = V;
                }
            }else{
                if(nO){
                    oTime = max(oTime + abs(oPos - V),bTime) + 1;
                    oPos = V;
                }else{
                    bTime = max(bTime + abs(bPos - V),oTime) + 1;
                    bPos = V;
                }
            }
            O = nO;
            first = false;
        }
        output << "Case #" << i << ": " << max(bTime,oTime) << "\n";
    }
    output.flush();
    output.close();
    return 0;
}
