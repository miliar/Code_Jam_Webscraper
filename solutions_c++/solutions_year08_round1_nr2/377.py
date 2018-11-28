/*
ID: kazastankas
PROG: saving_the_universe
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;
ifstream fin("1AB-small.in");
ofstream fout("1AB-small.out");
struct p {
       short num;
       bool malt;
};
struct customer {
       short numpref;
       p preferences[2000];
       short forced;
};
bool operator<(const customer& a, const customer& b) {
     if (a.numpref == -1) return false;
     else if (b.numpref == -1) return true;
     else return a.numpref < b.numpref;
}
bool operator<(const p& a, const p& b) {
     return a.malt < b.malt;
}
customer fanbase[2000];
short shakestate[2000];
int cases, curcase, customers, shakes, forceswitch;
int recursive_solve(int level) {
    if (level==customers) {
       fout << "Case #" << curcase+1 << ":";
       for (int i=0;i<shakes;i++) {
           if(shakestate[i]==-1) fout << " 0";
           else fout << " " << shakestate[i];
       }
       fout << endl;
       return -2;
    }
    for (int i=0;i<fanbase[level].numpref;i++) {
        if (shakestate[fanbase[level].preferences[i].num-1] == -1) {
           shakestate[fanbase[level].preferences[i].num-1] = fanbase[level].preferences[i].malt;
           fanbase[level].forced=i;
           forceswitch=0;
        }
        else if (shakestate[fanbase[level].preferences[i].num-1] != fanbase[level].preferences[i].malt) {
             continue;
        }
        if (forceswitch==1) continue;
        int checker=recursive_solve(level+1);
        if (checker==-2) return -2;
        else if (checker==-1) {
             if (fanbase[level].forced==i) shakestate[fanbase[level].preferences[i].num-1] = -1;
             else forceswitch=1;
        }           
    }
    if (level == 0) fout << "Case #" << curcase+1 << ": IMPOSSIBLE\n";
    return -1;
}
int main() {
    fin >> cases;
    for (int i=0;i<cases;i++) {
        curcase=i;
        forceswitch=0;
        fin >> shakes >> customers;
        for (int j=0;j<customers;j++) {
            fin >> fanbase[j].numpref;
            for (int k=0;k<fanbase[j].numpref;k++) {
                fin >> fanbase[j].preferences[k].num >> fanbase[j].preferences[k].malt;
            }
            fanbase[j].forced=-1;            
            sort(fanbase[j].preferences,fanbase[j].preferences+fanbase[j].numpref);
        }
        for (int l=0;l<shakes;l++) shakestate[l]=-1;
        for (int m=customers;m<2000;m++) fanbase[m].numpref=-1;
        sort(fanbase,fanbase+customers);
        recursive_solve(0);
    }
    return 0;
}

