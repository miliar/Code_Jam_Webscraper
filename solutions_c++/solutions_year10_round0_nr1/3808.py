#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
    int t,n,k;
    ifstream fin;
    ofstream fout;
    fin.open("A-large.in");
    fout.open("A-large.out");
    fin>>t;
    for(int ti=1;ti<=t;ti++){
        fin>>n>>k;k++;
        fout << "Case #"<<ti<<": ";
        if(k%int(pow(2,n)))
            fout<<"OFF";
        else
            fout<<"ON";
        fout<<endl;
    }
    fout.close();
    fin.close();
    return 0;
}
