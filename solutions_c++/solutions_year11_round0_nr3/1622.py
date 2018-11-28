
#include <fstream>

using namespace std;

int main() {
    
    ifstream fin;
    ofstream fout;
    int t, n;
    unsigned int sum, min, xored;
    
    fin.open("C-small.in", ios_base::in);
    fout.open("C-small.out", ios_base::out);
    
    fin >> t;
    for (int i = 0; i < t; i++) {
        fin >> n;
        
        sum = 0;
        min = 
        xored = 0;
        
        fin >> min;
        sum = min;
        xored = min;
        
        for (int j = 1; j < n; j++) {
            unsigned int tmp;
            fin >> tmp;
            sum += tmp;
            min = (tmp<min)?tmp:min;
            xored ^= tmp;            
        }
        
        fout << "Case #" << i+1 << ": ";
        if (xored == 0) {
            fout << sum-min << endl;
        } else {
            fout << "NO" << endl;
        }
        
    }
    
    fin.close();
    
    fout.close();
}
