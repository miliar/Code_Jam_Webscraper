#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
int main()
{    
    ifstream ifs("c:/io.txt");
    ofstream ofs("c:/out.txt");
    int num;
    ifs >> num;
    for(size_t i = 0; i < num; ++i){
        int p_num, p, s, sum = 0;
        ifs >> p_num >> s >> p;
        for(size_t j = 0; j < p_num; ++j){
            int aa;
            ifs >> aa;
            if(3 * p <= aa)
                 sum++;
            else{
                 aa -= p;
                 if(aa < 0)
                        continue;
                 int bb = aa/2;
                 if((bb + 2) == p && s > 0){
                        s--;
                        sum++;
                 }
                 else if((bb + 2) > p)
                        sum++;
            }
        }
        ofs << "Case #" << i+1 << ": " << sum << endl;
    }
    ifs.close();
    ofs.close();
    return 0;
}
