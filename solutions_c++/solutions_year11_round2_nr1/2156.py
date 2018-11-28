#include <fstream>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

vector<double> CalWP(const vector<string>& sch)
{
    vector<double> wp_vec(sch.size());
    for(size_t k=0; k<sch.size(); ++k){
        const string& str = sch[k];
        int wn = count(str.begin(), str.end(), '1');
        int fn = count(str.begin(), str.end(), '0');
        if(wn+fn==0) wp_vec[k] = 1.0;
        else wp_vec[k] = wn*1.0/(wn+fn);
    }
    return wp_vec;
}

vector<double> CalOWP(const vector<string>& sch)
{
    vector<double> owp_vec(sch.size());
    for(size_t i=0; i<sch.size(); ++i){
        const string& str = sch[i];
        double wp(0);
        int op_num=0;
        for(size_t j=0; j<str.length(); ++j){
            if(str[j] == '.') continue;
            const string& ostr = sch[j];
            int wn(0), fn(0);
            for(size_t k=0; k<ostr.length(); ++k){
                if(k==i) continue;
                if(ostr[k] == '1') ++wn;
                else if(ostr[k] == '0') ++fn;
            }
            wp += wn*1.0/(wn+fn);
            ++op_num;
        }
        owp_vec[i] = wp/op_num;
    }

    return owp_vec;
}

vector<double> CalRPI(const vector<string>& sch)
{
    vector<double> wp_vec = CalWP(sch);
    vector<double> owp_vec = CalOWP(sch);
    vector<double> oowp_vec(sch.size());
    for(size_t k=0; k<sch.size(); ++k){
        const string& str = sch[k];
        int no=0;
        double owp=0;
        for(size_t i=0; i<str.length(); ++i){
            if(str[i] != '.'){
                owp += owp_vec[i];
                ++no;
            }
        }
        if(no == 0) { oowp_vec[k] = 0; }
        else oowp_vec[k] = owp/no;
    }
    // cout << "WP: ";
    // for(size_t k=0; k<wp_vec.size(); ++k) cout << wp_vec[k] <<" ";
    // cout << endl;

    // cout << "OWP: ";
    // for(size_t k=0; k<owp_vec.size(); ++k) cout << owp_vec[k] <<" ";
    // cout << endl;

    // cout << "OOWP: ";
    // for(size_t k=0; k<oowp_vec.size(); ++k) cout << oowp_vec[k] << " ";
    // cout << endl;
    vector<double> ret(sch.size());
    for(size_t k=0; k<ret.size(); ++k){
        ret[k] = 0.25*wp_vec[k] + 0.5*owp_vec[k] + 0.25*oowp_vec[k];
    }
    return ret;
}

int main(int argc, char** argv)
{
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    vector <string> sch;
    int case_num, sch_num;
    fin >> case_num;
    for(int k=0; k<case_num; ++k){
        fin >> sch_num;
        sch.resize(sch_num);
        for(size_t i=0; i<sch_num; ++i){
            fin >> sch[i];
        }
        vector<double> res = CalRPI(sch);
        fout << "Case #" << k+1 <<": "<<endl;
        for(size_t k=0; k<res.size(); ++k) fout << res[k] << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
