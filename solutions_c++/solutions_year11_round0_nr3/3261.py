#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream in("C-large.in");
    ofstream out("c.out");
    int Z, N;
    
    in >> Z;
    for(int z = 0; z < Z; z++) {
        in >> N;
        out << "Case #" << z+1 << ": ";
        int tmp;
        int minN = 99999999; 
        int total = 0;
        int cando = 0;
        for(int i = 0; i < N; i++) {
            in >> tmp;
            cando ^= tmp;
            total += tmp;
            if(tmp < minN) minN = tmp;
        }
        if(cando == 0){
            out << total - minN << endl;
        }
        else {
            out << "NO" << endl;
        }
    }
    //cin.get();
    
    return 0;
}
