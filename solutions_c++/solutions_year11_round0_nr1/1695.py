#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

struct Ins{
    char op;
    int bn;
};

int min_seconds(const vector<Ins>& sq)
{

    int sec = 0;
    int cur_op(1), cur_bp(1);
    for(size_t k=0; k<sq.size(); ++k){
        int spend_sec;
        if(sq[k].op == 'O'){
            spend_sec = fabs(sq[k].bn - cur_op) + 1;
            cur_op = sq[k].bn;
            for(size_t j=k+1; j<sq.size(); ++j){
                if(sq[j].op == 'B'){
                    int _spend_sec = fabs(sq[j].bn - cur_bp) + 1;
                    if( _spend_sec <= spend_sec){
                        cur_bp = sq[j].bn;
                    }else{
                        if(sq[j].bn < cur_bp) cur_bp -= spend_sec;
                        else cur_bp += spend_sec;
                    }
                    break;
                }
            }
        }else if(sq[k].op == 'B'){
            spend_sec = fabs(sq[k].bn - cur_bp) + 1;
            cur_bp = sq[k].bn;
            for(size_t j=k+1; j<sq.size(); ++j){
                if(sq[j].op == 'O'){
                    int _spend_sec = fabs(sq[j].bn - cur_op) + 1;
                    if(_spend_sec <= spend_sec){
                        cur_op = sq[j].bn;
                    }else{
                        if(sq[j].bn < cur_op) cur_op -= spend_sec;
                        else cur_op += spend_sec;
                    }
                    break;
                }
            }
        }
        sec += spend_sec;
        // cout << "cur O: " << cur_op << endl;
        // cout << "cur B: " << cur_bp << endl;
        // cout << "spend sec: " << spend_sec << ": " << sec << endl;
    }

    return sec;
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
        int ins_num;
        fin >> ins_num;
        vector<Ins> sq(ins_num);
        for(size_t i=0; i<sq.size(); ++i){
            fin >> sq[i].op >> sq[i].bn;
        }
        //        if(k != 6) continue;
        int res = min_seconds(sq);
        fout << "Case #" << k+1 <<": " << res << endl;
    }
    fout.close();
    fin.close();
    return 0;
}
