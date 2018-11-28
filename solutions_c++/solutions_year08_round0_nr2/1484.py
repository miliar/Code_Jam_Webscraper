/*
ID: kazastankas
PROG: saving_the_universe
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
using namespace std;
ifstream fin("B-large.in");
ofstream fout("B-large.out");
int cases, turntime, a_trains, aneeded, b_trains, bneeded;
string query;
int main() {
    fin >> cases;
    for (int i=0;i<cases;i++) {
        fin >> turntime >> a_trains >> b_trains;
        aneeded=a_trains;
        bneeded=b_trains;
        int a[a_trains][2];
        int b[b_trains][2];
        int cache[2];
        // parse train times into ints
        for (int j=0;j<a_trains;j++) {
            fin >> query;
            sscanf(query.c_str(),"%d:%d",&cache[0],&cache[1]);
            a[j][0]=cache[0]*60+cache[1];
            fin >> query;
            sscanf(query.c_str(),"%d:%d",&cache[0],&cache[1]);
            a[j][1]=cache[0]*60+cache[1]+turntime;
        }
        for (int k=0;k<b_trains;k++) {
            fin >> query;
            sscanf(query.c_str(),"%d:%d",&cache[0],&cache[1]);
            b[k][0]=cache[0]*60+cache[1];
            fin >> query;
            sscanf(query.c_str(),"%d:%d",&cache[0],&cache[1]);
            b[k][1]=cache[0]*60+cache[1]+turntime;
        }
        // search for proper attachments for a-trains to b-trains
        for (int l=0;l<a_trains;l++) {
            int mindiff=1440;
            int mindifftrain=-1;
            for (int m=0;m<b_trains;m++) {
                if (b[m][0]!=-1) {
                    int diff=b[m][0]-a[l][1];
                    if (diff>=0&&diff<mindiff) {
                       mindiff=diff;
                       mindifftrain=m;
                    }
                }
            }
            if (mindifftrain!=-1) {
               b[mindifftrain][0]=-1;
               bneeded--;
            }
        }
        // search for proper attachments for b-trains to a-trains
        for (int n=0;n<b_trains;n++) {
            int mindiff=1440;
            int mindifftrain=-1;
            for (int o=0;o<a_trains;o++) {
                if (a[o][0]!=-1) {
                    int diff=a[o][0]-b[n][1];
                    if (diff>=0&&diff<mindiff) {
                       mindiff=diff;
                       mindifftrain=o;
                    } 
                }
            }
            if (mindifftrain!=-1) {
               a[mindifftrain][0]=-1;
               aneeded--;
            }
        }
        fout << "Case #" << i+1 << ": " << aneeded << " " << bneeded << endl;
    }
    return 0;
}

