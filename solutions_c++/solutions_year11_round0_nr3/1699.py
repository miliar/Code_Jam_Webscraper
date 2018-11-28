#include <iostream>
#include <fstream>
using namespace std;

bool Crying(int x)
{
    while(x){
        int b = x%2;
        if(b==1) return true;
        x = x/2;
    }
    return false;
}

int main(int argc, char** argv)
{
    if(argc < 3) {
        cerr << "Usage: ./a input-file-name output-file-name" << endl;
        return -1;
    }
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    int case_num;
    fin >> case_num;
    for(int k=0; k<case_num; ++k){
        int n;
        fin >> n;
        int v, x=0,sum_v(0), min_v(10000000);        
        for(int j=0; j<n; ++j){
            fin >> v;
            x = x^v;
            if(v < min_v) min_v = v;
            sum_v += v;
        }
        fout << "Case #"<<k+1<<": ";
        if(Crying(x)){
            fout << "NO" << endl;
        }else{
            fout << sum_v - min_v << endl;
        }
    }
    fout.close();
    fin.close();
    return 0;
}
