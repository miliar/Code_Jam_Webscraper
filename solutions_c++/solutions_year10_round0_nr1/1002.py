#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");
int n,k,t;

int main()
{
    fin>>t;
    int tmp=t;
    while (t!=0){
        fin>>n>>k;
        fout<<"Case #"<<tmp-t+1<<": ";
        if ((k+1)%(1<<n)==0) fout<<"ON "<<endl;
        else fout<<"OFF"<<endl;
        t--;
    }
    return 0;
}
