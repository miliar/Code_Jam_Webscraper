#include <iostream>
#include <fstream>
#include <stdio.h>
#include <cmath>
#include <string.h>

using namespace std;

ifstream fin("A-small.in");
ofstream fout("A-small.out");

int main(){
    int a1,a2,b1,b2,i,j,ma,mi;
    int N;
    fin>>N;
    int tmp=N;
    while (N!=0){
        N--;
    int count=0;
    fin>>a1>>a2>>b1>>b2;
    for (i=a1;i<=a2;i++)
    for (j=b1;j<=b2;j++){
        ma=max(i,j);
        mi=min(i,j);
    if (ma>=2*mi) count++;
    else {
        int cc=0;
        int tmp;
        while (ma>0 && mi>0){
            tmp=ma-mi;
            ma=mi;
            mi=tmp;
            cc++;
        }
        if (cc%2==0) count++;
        }
    }
    fout<<"Case #"<<tmp-N<<": "<<count<<endl;
    }
    return 0;
}
