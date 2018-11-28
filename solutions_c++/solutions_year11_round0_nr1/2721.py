#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <math.h>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

int N;
vector<int> b1, b2;
vector<pair<string,int> > seq;
int main() {
    int T;
    fin>>T;
    for(int k = 1;k<=T;++k) {
        fin>>N;
        b1.clear();
        b2.clear();
        seq.clear();
        for(int i = 0;i<N;++i) {
            string s;
            int button;
            fin>>s>>button;
            if(s == "O") b1.push_back(button);
            else b2.push_back(button);
            seq.push_back(make_pair(s,button));
        }
        int res = 0, curr1 = 1, curr2 = 1, target1 = 1, target2 = 1, dir1 = 1, dir2 = 1, task1 = 0, task2 = 0;
        if(!b1.empty()) target1 = b1[0];
        if(!b2.empty()) target2 = b2[0];
        for(int i = 0;i<N;++i) {
            while(true) {
                if(seq[i].first == "O") {
                    if(curr1 == target1) {
                        if(curr1 != target1) curr1 += dir1;
                        if(curr2 != target2) curr2 += dir2;
                        ++task1;
                        int temp = 0;
                        if(task1<b1.size()) temp = b1[task1];
                        if(temp>target1) dir1 = 1;
                        else dir1 = -1;
                        target1 = temp;
                        ++res;
                        break;
                    }
                }
                else {
                    if(curr2 == target2) {
                        if(curr1 != target1) curr1 += dir1;
                        if(curr2 != target2) curr2 += dir2;
                        ++task2;
                        int temp = 0;
                        if(task2<b2.size()) temp = b2[task2];
                        if(temp>target2) dir2 = 1;
                        else dir2 = -1;
                        target2 = temp;
                        ++res;
                        break;
                    }
                }
                if(curr1 != target1) curr1 += dir1;
                if(curr2 != target2) curr2 += dir2;
                ++res;
            }
        }
        
        fout<<"Case #"<<k<<": "<<res<<endl;
    }
    return 0;
}
