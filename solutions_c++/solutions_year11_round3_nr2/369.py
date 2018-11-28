#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

int l, n, cn;
long long t;
long long d[1000005], c[1000005];
long long minTime()
{
    long long sd=0;
    int idx(-1);
    for(int i=0; i<n; ++i) {
        sd += d[i]*2;
        if(sd >= t) {idx = i; break;}
    }
    if(idx == -1) {
        //        cout << idx << endl;
        return sd;
    }

    //    cout << sd << " " << idx << endl;
    long long pred;
    if(idx == 0) pred = 0;
    else pred = sd - d[idx]*2;
    vector<long long> rd;
    rd.push_back(d[idx] - (t - pred)/2);
    for(int j=idx+1; j<n; ++j) rd.push_back(d[j]);

    // cout << "rd: "; 
    // for(size_t k=0; k<rd.size(); ++k){
    //     cout << rd[k] << " ";
    // }
    // cout << endl;
    
    sort(rd.begin(), rd.end());
    long long rt = 0;
    for(int k=(int)rd.size()-1; k>=0 && l>0; --k, --l){
        rt += rd[k];
    }
    long long td=0;
    for(int i=0; i<n; ++i) td += d[i] *2;
    //    cout << td << " " << rt << endl;
    return td - rt;
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
        fin >> l >> t >> n >> cn;
        for(int i=0; i<cn; ++i) fin >> c[i];
        for(int i=0; i<n;){
            for(int j=0; j<cn && i<n; ++j, ++i) d[i] = c[j];
        }
        // cout << "Case #" << k+1 << "d : " << endl;
        // cout << l << " " << t << " " << n <<" " << cn << endl;
        // for(int i=0; i<n; ++i) cout << d[i] << " ";
        // cout << endl;
        fout << "Case #" << k+1 <<": " << minTime() << endl;
    }
    fout.close();
    fin.close();

    return 0;
}
    
