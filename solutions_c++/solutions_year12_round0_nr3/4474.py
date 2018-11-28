#include<cstdio>
#include<cstdlib>
#include<climits>
#include<cfloat>
#include<utility>
#include<set>
#include<memory>
#include<functional>
#include<sstream>
#include<complex>
#include<stack>
#include<queue>
#include<iostream>
#include<vector>
#include<list>
#include<string>
#include<cmath>
#include<map>
#include<algorithm>
#include<fstream>
using namespace std;

int main() {
    //ifstream ifs("C-test-in.txt");
    //ofstream ofs("C-test-out.txt");
    ifstream ifs("C-small-attempt0.in");
    ofstream ofs("C-small-out.txt");


    int num;
    ifs >> num;

    string hoge;
    getline(ifs,hoge);
    for(int i=0;i < num;i++) {
        stringstream ss;
        ss << (i+1);
        string s_num = ss.str();


        int A,B;
        string res="Case #" + s_num  + ": ";
        ifs >> A >> B;
        cout << A << " " << B  << endl;
        int count = 0;
        vector<int> tmp;
        for(int j=A;j <= B;j++) {
            stringstream ss2;
            ss2 << j;
            string s = ss2.str();
            
            for(int k=1;k<s.size();k++) {
                string tmp_s = "";
                string h_s = "";
                for(int z=s.size()-k;z<s.size();z++) {
                    tmp_s += s[z];
                }
                h_s += tmp_s;
                for(int z=0;z<s.size() - tmp_s.size();z++) {
                    h_s += s[z];
                }
                stringstream istr(h_s.data());
                int num;
                istr >>num;
                
                if(j < num && B >= num) {
                    count++;
                    //cout << j << ":" << num << endl;
                }
            }


        }

        cout << count << endl;
        stringstream res_ss;
        res_ss << count;
        string res_s = res_ss.str();
        res += res_s;
        ofs << res << endl; 

    }

}
