#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

int n, l, h;
int f[128];
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
        fin >> n >> l >> h;
        for(int i=0; i<n; ++i) fin >> f[i];

        int res = -1;
        for(int i=l; i<=h; ++i){
            bool flag = true;
            for(int j=0; j<n; ++j){
                if(i%f[j] !=0 && f[j]%i !=0){
                    flag = false; break;
                }
            }
            if(flag == true){
                res = i; break;
            }
        }
        fout << "Case #" << k+1 <<": " ;
        if(res == -1) fout << "NO" << endl;
        else fout << res << endl;
    }
    fout.close();
    fin.close();

    return 0;
}
    
